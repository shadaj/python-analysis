import sys
from importlib.abc import MetaPathFinder, Loader
from importlib.machinery import ModuleSpec, SourceFileLoader

from .instrument_nested import extract_all_codeobjects, instrument_extracted

from typing import List, Optional, Sequence, Union
from types import ModuleType

_Path = Union[bytes, str]

_active_receivers = []

def add_receiver(receiver):
  _active_receivers.append(receiver)
  return lambda: _active_receivers.remove(receiver)

class PatchingLoader(SourceFileLoader):
  existing_loader: Loader

  def __init__(self, fullname: str, path: str, existing_loader: Loader) -> None:
    self.existing_loader = existing_loader
    super(SourceFileLoader, self).__init__(fullname, path)

  def create_module(self, spec: ModuleSpec) -> Optional[ModuleType]:
    return self.existing_loader.create_module(spec)

  def exec_module(self, module: ModuleType) -> None:
    if hasattr(self.existing_loader, "get_code"):
      module_code = self.existing_loader.get_code(self.name) # type: ignore
      
      [id_to_bytecode, code_to_id] = extract_all_codeobjects(module_code)
      id_to_bytecode_new_codeobjects = instrument_extracted(id_to_bytecode, code_to_id)

      instrumented = id_to_bytecode_new_codeobjects[code_to_id[module_code]]

      def common_receiver(stack, opcode, arg, opindex, code_id, is_post):
        for receiver in _active_receivers:
          receiver(stack, opcode, arg, opindex, code_id, is_post, id_to_bytecode)

      # TODO(shadaj): use an immutable overlay instead
      module.__dict__["py_instrument_receiver"] = common_receiver
      exec(instrumented.to_code(), module.__dict__)
    else:
      self.existing_loader.exec_module(module)

class PatchingPathFinder(MetaPathFinder):
  existing_importers: List[MetaPathFinder]
  current_path: Optional[Sequence[_Path]]

  def __init__(self):
    self.existing_importers = sys.meta_path.copy()

  def install(self):
    sys.meta_path.insert(0, self)

  def uninstall(self):
    sys.meta_path.remove(self)

  def find_module(self, fullname: str, path: Optional[Sequence[_Path]]) -> Optional[Loader]:
    path_to_module = None
    module_name = fullname.split('.')[-1]
    if path:
      path_to_module = str(path[0]) + "/" + module_name + ".py"
    else:
      path_to_module = module_name + ".py"

    existing_loader = None
    for importer in self.existing_importers:
      existing_loader = importer.find_module(fullname, path)
      if existing_loader is not None:
        break

    if existing_loader is not None:
      return PatchingLoader(fullname, path_to_module, existing_loader)
    else:
      return None
