from typing import List
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)

new_vector = scale("Yeah, wrong", [1.0, -4.2, 5.4])
print(new_vector)

"""
This returns a TypeError: can't multiply sequence by non-int of type 'float'
The reason is though Python does not force you type innotation, num values of vector
are float, then it can not multiply with a string or anything except numerical 
data 
The error shows up at runtime
"""