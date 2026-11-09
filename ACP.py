import math

angle = float(input("Enter an angle in degrees: "))

radians = math.radians(angle)

sine = math.sin(radians)
cosine = math.cos(radians)
tangent = math.tan(radians)

print("Sine:", sine)
print("Cosine:", cosine)
print("Tangent:", tangent)