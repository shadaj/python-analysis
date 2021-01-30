from bytecode import Bytecode

from typing import Any, Dict, List, Union
from typing_extensions import Literal

class EventReceiver(object):
  current_exit_func = None
  def on_event(self, stack: List[Any], opcode: Union[Literal["JUMP_TARGET"], int], arg: Any, opindex: int, code_id: int, is_post: bool, id_to_orig_bytecode: Dict[int, Bytecode]):
    pass

  def __enter__(self):
    assert self.current_exit_func == None
    self.current_exit_func = add_receiver(self)
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.current_exit_func()
    self.current_exit_func = None

_active_receivers: List[EventReceiver] = []

def add_receiver(receiver: EventReceiver):
  _active_receivers.append(receiver)
  return lambda: _active_receivers.remove(receiver)

def call_all_receivers(stack: List[Any], opcode: Union[Literal["JUMP_TARGET"], int], arg: Any, opindex: int, code_id: int, is_post: bool, id_to_orig_bytecode: Dict[int, Bytecode]):
  for receiver in _active_receivers:
    receiver.on_event(stack, opcode, arg, opindex, code_id, is_post, id_to_orig_bytecode)
