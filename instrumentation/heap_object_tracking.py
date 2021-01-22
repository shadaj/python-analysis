class HeapObjectTracker(object):
  def __init__(self, *args, **kwargs):
    self.objects_to_id = {} #WeakKeyDictionary() does not support list, dict
    self.id_to_objects = {} #WeakValueDictionary() does not support list, dict
    self.next_object_id = 0

  def is_heap_object(self, obj):
    for tpe in [int, str]:
      if isinstance(obj, tpe):
        return False
    
    return True
  
  def get_object_id(self, obj):
    if id(obj) in self.objects_to_id:
      return self.objects_to_id[id(obj)]
    else:
      self.objects_to_id[id(obj)] = self.next_object_id
      self.id_to_objects[self.next_object_id] = obj
      
      self.next_object_id += 1
      return self.objects_to_id[id(obj)]

  def get_by_id(self, id):
    return self.id_to_objects[id]
