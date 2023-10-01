# 1. The method is public in the parent class A and public in its descendant B:   

class Parent:
    def public_method(self):
        print("This is a public method in the Parent class.")

class Child(Parent):
    def child_method(self):
        print("This is a method in the Child class.")

obj = Child()
obj.public_method()  # Accessing the public method from the Parent class
obj.child_method()   # Accessing the method from the Child class


# 2. The method is public in the parent class A and hidden in its descendant B:

class Parent:
    def public_method(self):
        print("This is a public method in the Parent class.")

class Child(Parent):
    def _child_method(self):
        print("This method is hidden in the Child class.")

obj = Child()
obj.public_method()  # Accessing the public method from the Parent class
obj._child_method()  # Accessing the hidden method from the Child class
  

# 3. The method is hidden in the parent class A and public in its descendant B 

#         Not applicable for Python


# 4. The method is hidden in the parent class A and public in its descendant B 

class Parent:
    def __hidden_method(self):
        print("This method is hidden in the Parent class.")

class Child(Parent):
    def __hidden_method(self):
        print("This method is hidden in the Child class.")



