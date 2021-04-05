# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return f'Hi, {name}'


def function_args_positional(x,y, z=3):
    print(x, y, z)


def function_args_kwargs(x,y, **kwargs):
    age = kwargs.get("age")
    print("age", 12)


def function_args_arbitraty(*args):
    print(args)


def unpacking():
    ages =[32,25,34,65,12]
    for i, a in enumerate(ages):
        print(i, a)

def return_age_and_sex():
    return 21, "M"

if __name__ == '__main__':
    # function_args_positional(1,2,4)
    # function_args_kwargs(1,2,age=12)
    # function_args_arbitraty(1,2,3,4)
    # age , __ = return_age_and_sex()

    letters = ['s', 'p', 'a', 'm']
    word = ''.join(letters)
    print(word)


    print("a"+" b")
    print("My name is {}".format("Ashok"))