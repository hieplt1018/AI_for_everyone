# define and call function
def point():
    print("Physics: 4.0")
    print("Math: 4.0")
    print("English: 4.0")
point()

#pass argument
def get_name(name):
    print("Your name: " + name)
get_name("Hiep")

#default argument
def say_oh_year(name = "Sky"):
    print(name + " say OH, YEAH!")
say_oh_year()
say_oh_year("Hiep")

#return function
def sum(num1, num2):
    return num1 + num2
sum = sum(3, 4)
print(sum)