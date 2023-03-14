flag = True

while flag:

    side_1 = int(input("enter first side of triangle: "))
    side_2 = int(input("enter second side of triangle: "))
    side_3 = int(input("enter third side of triangle: "))

    if side_1 + side_2 <= side_3 or side_2 + side_3 <= side_1 or side_1 + side_3 <= side_2:
        print("Incorrect sides, there's cannot be such triangle! Try again!") 
    elif side_1 == side_2 == side_3:
        output_string = "All sides of triangle are equal!"
        flag = False
    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
        output_string = "This is an isosceles triangle!"
        flag = False
    else: 
        output_string = "Just an ordinary triangle.."
        flag = False

print(output_string)
