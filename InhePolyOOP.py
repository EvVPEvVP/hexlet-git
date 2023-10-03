class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        if len(self.values) != len(other.values):
            return 

        result_values = []
        for i in range(len(self.values)):
            if isinstance(self.values[i], (int, float)) and isinstance(other.values[i], (int, float)):
                result_values.append(self.values[i] + other.values[i])
            else:
                return None  

        return Vector(result_values)
