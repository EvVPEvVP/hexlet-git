import copy
import json


class General(MainClass):
    def __init__(self, value):
        self.value = value

    def copy_object(self, other):
        self.value = other.value

    def clone_object(self):
        return copy.deepcopy(self)

    def compare_objects(self, other):
        return self.__dict__ == other.__dict__

    def serialize_object(self):
        return json.dumps(self.__dict__)

    def deserialize_object(self, json_str):
        data = json.loads(json_str)
        return self.__class__(**data)
        
    def print_object(self):
        return f"Object of type"

    def is_instance_of(self, class_type):
        return isinstance(self, class_type)

    def get_real_type(self):
        return type(self).__name__

class Any(General):
    pass

