
import numpy as np

arrayA = np.array([1,2,3])
arrayB = np.array([4,5,6])

sumAB = arrayA + arrayB
print("Sum of A and B:",sumAB)


subAB = arrayA - arrayB
print("Subtraction of A and B:",subAB)

# Note: In math, this can not happen cause 1x3 multiply 1x3 but in numpy, it will happen
mulAB = arrayA * arrayB
print("Multiplication of A and B:",mulAB)

divAB = arrayA / arrayB
print("Division of A and B:",divAB)

broadcast = 5
print("Broadcasting:",broadcast + arrayA)
