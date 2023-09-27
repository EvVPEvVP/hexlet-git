class General:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

class Any(General):
    pass

def assignment_attempt(target, source):

    if isinstance(target, type(source)):
        target.value = source.value
    else:
        target.value = None


if __name__ == "__main__":

    general_obj = General(42)
    any_obj = Any("Hello")

    # Attempt to assign 'any_obj' to 'general_obj'
    assignment_attempt(general_obj, any_obj)



