from __future__ import annotations

from typing import Any, Dict, List, Tuple, Union, Optional
from typing_extensions import Literal

from .util import ObjectId
from .heap_object_tracking import HeapObjectTracker


object_id_to_heap_element_map: Dict[Union[ObjectId, int, str], HeapElement] = {}
def getHeapElement(concrete: Any, heap_object_tracker: HeapObjectTracker, nameStr: str = "") -> HeapElement:
  if heap_object_tracker.is_heap_object(concrete):
    key = ObjectId(heap_object_tracker.get_object_id(concrete))
  else:
    key = concrete
  if key not in object_id_to_heap_element_map:
    object_id_to_heap_element_map[key] = HeapElement(concrete, heap_object_tracker, nameStr)
  return object_id_to_heap_element_map[key]


namelessSymbolicElementCount = 0

class HeapElement(object):
  object_id: Union[ObjectId, int, str]
  collection_heap_elems: Optional[Union[List[SymbolicElement], Dict[SymbolicElement, SymbolicElement]]] 
  collection_counter: int
  collection_prefix: str

  def __init__(self, concrete: Any, heap_object_tracker: HeapObjectTracker, namePrefix: str = "") -> None:
    global namelessSymbolicElementCount
    assert not isinstance(concrete, HeapElement), "Did not expect a HeapElement here"
    if heap_object_tracker.is_heap_object(concrete):
      self.object_id = ObjectId(heap_object_tracker.get_object_id(concrete))
      if isinstance(concrete, list):
        self.collection_heap_elems = []
        self.collection_counter = 0
        for i, e in enumerate(concrete):
            if namePrefix == "": #Top level variable, need a global count for them
                namelessSymbolicElementCount += 1
                nameStr = "\'\'nameless%05d"%namelessSymbolicElementCount
                self.collection_counter = namelessSymbolicElementCount
            else:
                nameStr = namePrefix + "\'\'nameless%05d"%i
                self.collection_counter = i
            self.collection_prefix = namePrefix + "\'\'nameless%05d"
            self.collection_heap_elems.append(SymbolicElement(nameStr, getHeapElement(e, heap_object_tracker, nameStr + "|")))
      elif isinstance(concrete, slice):
        self.collection_heap_elems = []
        self.collection_heap_elems.append(SymbolicElement("slice%05d_start", getHeapElement(concrete.start, heap_object_tracker, "slice%05d_start|")))
        self.collection_heap_elems.append(SymbolicElement("slice%05d_stop", getHeapElement(concrete.stop, heap_object_tracker, "slice%05d_stop|")))
        self.collection_heap_elems.append(SymbolicElement("slice%05d_step", getHeapElement(concrete.step, heap_object_tracker, "slice%05d_step|")))
      elif isinstance(concrete, dict):
        raise Exception("Not handled HeapElements for dicts")
    else:
      assert isinstance(concrete, (int, str)), "Unhandled data type"
      self.object_id = concrete #int or str

class SymbolicElement(object):
  var_name: str
  heap_elem: HeapElement
  version: int

  def __init__(self, var_name: str, elems: Union[HeapElement, StackElement], version = 0) -> None:
    if isinstance(elems, HeapElement):
      self.var_name = var_name
      self.heap_elem = elems
      self.version = version #Starting version of any symbolic element is zero
    elif isinstance(elems, StackElement):
      self.var_name = var_name
      self.heap_elem = elems.heap_elem 
      self.version = elems.version + 1
    else:
      raise Exception("Unexpected type")

stackElementCount = 0

class StackElement(object):
  heap_elem: HeapElement
  version: int
  var_name: str

  def __init__(self, elems: Union[HeapElement, SymbolicElement], version = 0) -> None:
    global stackElementCount
    stackElementCount += 1
    self.var_name = "st_el%d"%stackElementCount
    if isinstance(elems, HeapElement):
      self.heap_elem = elems
      self.version = version #Starting version of any symbolic element is zero
    elif isinstance(elems, SymbolicElement):
      self.heap_elem = elems.heap_elem
      self.version = elems.version + 1
    else:
        raise Exception("Unexpected type")
