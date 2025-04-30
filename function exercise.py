def calculate_area(base, height):
    area = (1/2) * base * height
    return area

base_value = int(input("Enter the base value: "))
height_value = int(input("Enter the height value: "))
triangle_area = calculate_area(base_value, height_value)
print("Area of the triangle:", triangle_area)

def calculate_area(base, height, shape_type):
    if shape_type.lower() == "triangle":
        area = 0.5 * base * height
    elif shape_type.lower() == "rectangle":
        area = base * height
    else:
        raise ValueError("Invalid shape_type. Use 'triangle' or 'rectangle'.")
    return area
#data added in the 1st file and create the changes 

print(calculate_area(10, 5, "triangle"))   # Output: 25.0
print(calculate_area(10, 5, "rectangle"))  # Output: 50
