from __future__ import annotations
from types import CellType

from typing import Any, Dict, List, Tuple, Union, Optional, Iterator
from typing_extensions import Literal

from .util import ObjectId
from .heap_object_tracking import HeapObjectTracker

from .helper import printDebug

object_id_to_heap_element_map: Dict[Union[ObjectId, int, str], HeapElement] = {}
def getHeapElement(concrete: Any, heap_object_tracker: HeapObjectTracker, nameStr: str = "") -> HeapElement:
  if heap_object_tracker.is_heap_object(concrete):
    key = ObjectId(heap_object_tracker.get_object_id(concrete))
  else:
    key = concrete
  if key not in object_id_to_heap_element_map:
    object_id_to_heap_element_map[key] = HeapElement(concrete, heap_object_tracker, nameStr)
  return object_id_to_heap_element_map[key]


class HeapElement(object):
  object_id: Union[ObjectId, int, str]
  collection_heap_elems: Union[SymbolicElement, List[SymbolicElement], Dict[SymbolicElement, SymbolicElement]]
  collection_counter: int
  collection_prefix: str
  metadata: Any #Currently used for storing closure information. only allocated by make_function

  def __init__(self, concrete: Any, heap_object_tracker: HeapObjectTracker, namePrefix: str = "") -> None:
    assert not isinstance(concrete, HeapElement), "Did not expect a HeapElement here"
    if heap_object_tracker.is_heap_object(concrete):
      self.object_id = ObjectId(heap_object_tracker.get_object_id(concrete))
      if isinstance(concrete, (list, tuple)):
        self.collection_heap_elems = []
        self.collection_counter = 0
        if namePrefix == "": #Top level variable, need a global count for them
            namePrefix = "hpo%05d|"%self.object_id.id 
        self.collection_prefix = namePrefix + "\'\'nameless%05d"
        for i, e in enumerate(concrete):
                   
            nameStr = namePrefix + "\'\'nameless%05d"%i
            self.collection_counter += 1
            self.collection_heap_elems.append(SymbolicElement(nameStr, getHeapElement(e, heap_object_tracker, nameStr + "|")))
      elif isinstance(concrete, slice):
        self.collection_heap_elems = []
        self.collection_heap_elems.append(SymbolicElement("slice%05d_start"%self.object_id.id , getHeapElement(concrete.start, heap_object_tracker, "slice%05d_start|"%self.object_id.id )))
        self.collection_heap_elems.append(SymbolicElement("slice%05d_stop"%self.object_id.id , getHeapElement(concrete.stop, heap_object_tracker, "slice%05d_stop|"%self.object_id.id )))
        self.collection_heap_elems.append(SymbolicElement("slice%05d_step"%self.object_id.id , getHeapElement(concrete.step, heap_object_tracker, "slice%05d_step|"%self.object_id.id )))
      elif isinstance(concrete, CellType):
        self.collection_heap_elems = []
        pass #Nothing done for Cells
      elif isinstance(concrete, dict):
        self.collection_heap_elems = {}
        printDebug(concrete)
        raise Exception("Not handled HeapElements for dicts")
      else:
        self.collection_heap_elems = [] # For type matching
    else:
      self.collection_heap_elems = [] # For type matching
      assert isinstance(concrete, (int, str)), "Unhandled data type"
      self.object_id = concrete #int or str

  def list_append(self, to_append: StackElement, heap_object_tracker: HeapObjectTracker) -> SymbolicElement:
    currentSize = len(self.collection_heap_elems)
    namePrefix = "hpo%05d|"%self.object_id.id 
    nameStr = namePrefix + "\'\'nameless%05d"%(currentSize)
    self.collection_counter += 1 #Adding one element to the collection
    symbVal = SymbolicElement(nameStr, getHeapElement(to_append, heap_object_tracker, nameStr + "|"))
    self.collection_heap_elems.append(symbVal)
    return symbVal

  def __hash__(self) -> int:
      return self.object_id.__hash__()

  def __eq__(self, other) -> bool:
      return self.object_id.__eq__(other.object_id)

class SymbolicElement(object):
  var_name: str
  heap_elem: HeapElement
  version: int
  is_const: bool

  def __init__(self, var_name: str, elems: Union[HeapElement, StackElement, None], version = 0) -> None:
    if isinstance(elems, HeapElement):
      self.var_name = var_name
      self.heap_elem = elems
      self.version = version #Starting version of any symbolic element is zero
      self.is_const = False #Default behavior
    elif isinstance(elems, StackElement):
      self.var_name = var_name
      self.heap_elem = elems.heap_elem 
      self.version = elems.version + 1
      self.is_const = elems.is_const
    elif elems is None: # Allowed for cell and free variables for a code object
      self.var_name = var_name
      self.heap_elem = elems
      self.version = version 
      self.is_const = False
    else:
      raise Exception("Unexpected type")

  def populate(self, elems: Union[HeapElement, StackElement, None]) -> None:
    assert self.heap_elem is None, "Cannot overwrite HeapElement corresponding to a SymbolicElement if it is not already None"
    self.heap_elem = elems

  def set_const(self) -> None:
    self.is_const = True
    for item in self.heap_elem.collection_heap_elems:
      item.set_const()

stackElementCount = 0

class StackElement(object):
  heap_elem: HeapElement
  version: int
  var_name: str
  is_const: bool

  def __init__(self, elems: Union[HeapElement, SymbolicElement], version = 0) -> None:
    global stackElementCount
    stackElementCount += 1
    self.var_name = "st_el%d"%stackElementCount
    if isinstance(elems, HeapElement):
      self.heap_elem = elems
      self.version = version #Starting version of any stack element is the same as parent object
      self.is_const = False #Default behavior
    elif isinstance(elems, SymbolicElement):
      self.heap_elem = elems.heap_elem
      self.version = elems.version + 1
      self.is_const = elems.is_const
    elif elems is None:
      raise Exception("Cell var not initialized before bringing onto stack")
    else:
      raise Exception("Unexpected type")

  def set_const(self) -> None:
    self.is_const = True
    for item in self.heap_elem.collection_heap_elems:
      item.set_const()

  def duplicate(self) -> StackElement:
      return StackElement(self.heap_elem, self.version)
