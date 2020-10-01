def great_customer(special):
   return "our special today is " + special


#print(great_customer("bananna yogurt"))



def add_one_if_odd(num):
    if num % 2 != 0:
        return num + 1
    else: 
        return num

def add_two(num):
    return num + 2

def square_point_plus_ten(x, y):
    z = 10
    print(z)
    x_2 = x*x
    y_2 = y*y
    return x_2, y_2
    

square_point_plus_ten(1, 2)
x_squarded, y_squared = square_point(2, 4)
print(str(x_squarded) + " " + str(y_squared))


x = add_two(add_one_if_odd(13))
y = add_two(2)
#print(x)
