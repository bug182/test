from random import randint

def rand_num(n):
    print(randint(0, n))

while True:
    try:
        number = int(input("Highest numeber: "))
    except NameError:
        print("Enter a number")
    except ValueError:
        print("Enter a number")
    else:
        rand_num(number)
        break
