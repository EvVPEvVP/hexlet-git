from typing_extensions import final

class BaseClass:
    @final
    def closed_method(self):
        print("This method cannot be overridden in subclasses")

class SubClass(BaseClass):
    def closed_method(self):
        print("This method is overridden in the subclass")

base_instance = BaseClass()
sub_instance = SubClass()

base_instance.closed_method()  # Output: This method cannot be overridden in subclasses
sub_instance.closed_method() # Output: TypeError: overriding final method

