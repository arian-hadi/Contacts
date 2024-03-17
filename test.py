try:
    f = open("random.txt", "r")
    content = f.read()
    print(content)
    f.close

except ZeroDivisionError:
    print("You cannot dvide a number by zero")
except ValueError:
    print("Only enter an integer value")
except FileNotFoundError:
    print("The file location does not exist")


