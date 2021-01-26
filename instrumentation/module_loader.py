import sys
from importlib.abc import MetaPathFinder, Loader
from importlib.machinery import ModuleSpec

from .instrument_nested import extract_all_codeobjects, instrument_extracted

from typing import List, Optional, Sequence, Union
from types import ModuleType

_Path = Union[bytes, str]

_active_receivers = []

def add_receiver(receiver):
  _active_receivers.append(receiver)
  return lambda: _active_receivers.remove(receiver)

class PatchingLoader(Loader):
  name: str
  existing_loader: Loader
  finder: "PatchingPathFinder"

  def __init__(self, name: str, existing_loader: Loader, finder: "PatchingPathFinder") -> None:
    self.name = name
    self.existing_loader = existing_loader
    self.finder = finder

  def get_filename(self, fullname):
    return self.existing_loader.get_filename(fullname)

  def is_package(self, fullname):
    return self.existing_loader.is_package(fullname)

  def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
    return self.existing_loader.create_module(spec)

  def load_module(self, fullname: str) -> ModuleType:
    return self.existing_loader.load_module(fullname)

  def module_repr(self, module: ModuleType) -> str:
    return self.existing_loader.module_repr(module)

  def exec_module(self, module: ModuleType) -> None:
    if hasattr(self.existing_loader, "get_code"):
      module_code = self.existing_loader.get_code(self.name) # type: ignore
      if module_code:
        print("[Python Analysis] Instrumenting module " + self.name)
        [id_to_bytecode, code_to_id] = extract_all_codeobjects(module_code)
        id_to_bytecode_new_codeobjects = instrument_extracted(id_to_bytecode, code_to_id)

        instrumented = id_to_bytecode_new_codeobjects[code_to_id[module_code]]

        def common_receiver(stack, opcode, arg, opindex, code_id, is_post):
          for receiver in _active_receivers:
            receiver(stack, opcode, arg, opindex, code_id, is_post, id_to_bytecode)

        # TODO(shadaj): use an immutable overlay instead
        module.__dict__["py_instrument_receiver"] = common_receiver
        exec(instrumented.to_code(), module.__dict__)
        self.finder.patched_modules.append(module.__name__)
      else:
        self.existing_loader.exec_module(module)
    else:
      self.existing_loader.exec_module(module)

modules_to_skip: List[ModuleType] = []

class PatchingPathFinder(MetaPathFinder):
  existing_importers: List[MetaPathFinder]
  current_path: Optional[Sequence[_Path]]
  patched_modules: List[str]

  def __init__(self):
    self.existing_importers = sys.meta_path.copy()
    self.patched_modules = []

  def install(self):
    sys.meta_path.insert(0, self)

  def uninstall(self):
    sys.meta_path.remove(self)
    for module in self.patched_modules:
      del sys.modules[module]
    self.patched_modules = []

  def find_module(self, fullname: str, path: Optional[Sequence[_Path]]) -> Optional[Loader]:
    existing_loader = None
    for importer in self.existing_importers:
      existing_loader = importer.find_module(fullname, path)
      if existing_loader is not None:
        break

    if existing_loader is not None and fullname not in modules_to_skip:
      return PatchingLoader(fullname, existing_loader, self)
    else:
      return None
