############
# Comments #
############

# ❌ Java

# // Single line comments start with two slashes (//)
# /* Multi line comment */

# ✅ Python

# Single line comments start with a hash (#)
"""
Multi line comments can be
written with triple quotes
"""

########################
# Primitive data types #
########################

# Numbers
3

# Math is what you would expect
1 + 1  # => 2
5 * 3  # => 15

# Exponentiation
2 ** 3  # => 8

# Enforce precedence with parentheses
(1 + 3) * 2  # => 8

# Floating numbers
3.14 + 1.0  # => 4.14

# Division is a bit tricky. It is integer division and floors the results
10 / 2  # => 5.0

# Boolean values are primitives
True  # => True

# Negate with not
not True  # => False

# Boolean Operators
True and False  # => False
True or False  # => True

# True and False are actually 1 and 0 but with different keywords
True + True  # => 2
False - 2 * True  # => -2

# None is an object
None  # => None

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added, too
"Hello " + "world!"  # => "Hello world!"

########################
# Variables and typing #
########################

# ❌ Java

# String variable;  // Java is a strongly typed language; you must declare the type of the variable before using it
# variable = "Hola Mundo";  // you can assign a value to a variable at any time
# System.out.println(variable);

# ✅ Python

variable = "Hola Mundo"  # the variable "variable" is being assigned a string "Hola Mundo"
print(variable)  # => "Hola Mundo"

type(variable)  # checkin the type of variable
print(isinstance(variable, str))  # => True

age = "3"
print(isinstance(age, int))  # => False

age = int(age)  # casting; convert a string to an integer
print(isinstance(age, int))  # => True

##########
# Naming #
##########

# ❌ Java

# String newSeparator;  // Java convention is to use camelCase for variables and methods
# Float userAge;

# ✅ Python

new_separator = ""  # Python convention is to use snake_case
user_age = 0

########################
# Arithmetic operators #
########################

# ❌ Java

# int a = 1;
# int b = 2;
# int c = a + b;
# a += 1; // a = a + 1

# ✅ Python

a = 1
b = 2
c = a + b
a += 1  # a = a + 1
a = c ** 2

########################
# Comparison operators #
########################

# ❌ Java

# int a = 1;
# int b = 2;
# boolean c = a == b; // False

# ✅ Python

a = 1
b = 2
c = a == b  # False
d = a > b

#####################
# Logical operators #
#####################

# ❌ Java

# boolean a = true;
# boolean b = false;
# boolean c = a && b; // False

# ✅ Python

a = True
b = False
c = a and b  # => False
d = None or int(3.5)  # => 3

##########
# Indent #
##########

# ❌ Java

# if (true) {
#     System.out.println("Hola Mundo");
# }

# ✅ Python

if True:
    print("Hola Mundo")  # indentation is important in Python; it is used to define blocks of code

################
# Conditionals #
################

# ❌ Java

# if (a == 1) {
#     System.out.println("Hola Tierra");
# } else if (a == 2) {
#     System.out.println("Hola Marte");
# } else {
#     System.out.println("Hola Venus");
# }

# ✅ Python

if a == 1:
    print("Hola Tierra")
elif a == 2:
    print("Hola Marte")
else:
    print("Hola Venus")

#########
# Loops #
#########

# ❌ Java

# for (int i = 0; i < 10; i++) {
#     System.out.println("Hola Mundo");
# }

# ✅ Python

for l in "hello":
    print(l + ", ")  # => h, e, l, l, o,

for i in range(10):
    print("Hola Mundo")

# ❌ Java

# int i = 0;
# while (i < 10) {
#     System.out.println("Hola Mundo");
#     i++;
# }

# ✅ Python

i = 0
while i < 10:
    print("Hola Mundo")
    i += 1


#######################
# Classes and methods #
#######################

# ❌ Java

# public class User {
#     private String name;
#     private String lastName;
#     private Integer age;
#
#     public User(String name, String lastName, Integer age) {
#         this.name = name;
#         this.lastName = lastName;
#         this.age = age;
#     }
#     public String getName() {
#         return name;
#     }
# }

# User my_user = new User("Juan", "Perez", 20);

# ✅ Python

class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def get_name(self):
        """
        Returns the name of the user.
        """
        return self.name


my_user = User("Juan", "Perez", 20)


#############
# Functions #
#############

def say_hi(name):
    """
    Prints a greeting message.
    """
    print("Hola " + name)


say_hi("Juan")


def get_greeting(name):
    """
    Returns a greeting message.
    """
    return "Hola " + name


greeting = get_greeting("Juan")
print(greeting)  # => Hola Juan


def get_greeting_with_default(name="Juan", surname="Perez"):
    """
    Returns a greeting message.
    """
    return "Hola " + name + " " + surname


greeting = get_greeting_with_default()
greeting = get_greeting_with_default("Juan", "Pérez")  # same as above, specifying argument by position
greeting = get_greeting_with_default(name="Juan", surname="Pérez")  # same as above, specifying argument by name
# greeting = get_greeting_with_default(name="Juan", "Pérez")  # positional argument after keyword argument (not allowed)
print(greeting)  # => Hola Juan Pérez

##########################
# Data structures: Lists #
##########################

# ❌ Java

# List<Integer> my_list = new ArrayList<>();
# my_list.add(1);
# my_list.add(2);
# my_list.add(3);
# my_list.add(4);
# my_list.add(5);

# ✅ Python

my_empty_list = []
my_list = [1, 2, 3, 4, 5]
my_list_b = [1, 2, 3, 4, 5, "hola", -1, True, None]  # mixed types
my_list_c = my_list + my_list_b  # concatenation
print(my_list)  # => [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list)  # => [1, 2, 3, 4, 5, 6]

my_list.remove(1)
print(my_list)  # => [2, 3, 4, 5, 6]

my_list.insert(0, 1)
print(my_list)  # => [1, 2, 3, 4, 5, 6]

my_list.reverse()
print(my_list)  # => [6, 5, 4, 3, 2, 1]

my_list.sort()
print(my_list)  # => [1, 2, 3, 4, 5, 6]

if 2 in my_list:
    print("2 is in my_list")

length = len(my_list)

for i in range(length):
    print(my_list[i])

for item in my_list:  # same as above
    print(item)

#################################
# Data structures: Dictionaries #
#################################

# ❌ Java

# HashMap<String, String> my_dict = new HashMap<String, String>();
# my_dict.put("name", "Juan");
# my_dict.put("last_name", "Perez");
# my_dict.put("age", "20");
# System.out.println(my_dict.get("name"));

# ✅ Python

my_empty_dict = {}  # empty dictionary

my_dict = {"name": "Juan", "last_name": "Perez", "age": 20}
print(my_dict)  # => {'name': 'Juan', 'last_name': 'Perez', 'age': 20}

# from the above, my_dict is a dictionary, which contains key-value pairs inside the { }
# here the keys are name, last_name and age

# access the value of the key "name"
print(my_dict["name"])  # => Juan
print(my_dict.get("first_name"))  # note that my_dict["first_name"] raises an error!

my_dict["age"] = 21  # update the value of the key "age"
print(my_dict)  # => {'name': 'Juan', 'last_name': 'Perez', 'age': 21}

del my_dict["last_name"]  # delete the key-value pair with key "last_name"
print(my_dict)  # => {'name': 'Juan', 'age': 21}

# updating existing key of the dictionary
my_dict.update({'name': "Francisco"})  # => {'name': 'Francisco', 'age': 21}

for key in my_dict:
    print(key)  # => name age

for key in my_dict.values():
    print(key)  # => Francisco 21

for key, value in my_dict.items():
    print(key, ",", value)  # => name , Francisco age , 21

if "name" in my_dict:
    print("name is in my_dict")

a = {1: "one", 2: "two", 3: "three"}
b = {4: "four", 5: "five", 6: "six"}

for key in b:
    if key not in a:
        a[key] = b[key]

length = len(a)
print(length)  # => 6

#################################
# Mutable and immutable objects #
#################################

my_list = [1, 2, 3, 4, 5]
my_list_b = my_list
my_list_b.append(6)
print(my_list)  # => [1, 2, 3, 4, 5, 6]
print(my_list_b)  # => [1, 2, 3, 4, 5, 6]

# List and dictionary are mutable objects, which means that when you assign a variable to another variable,
# both variables will point to the same object in memory.
# This is different from immutable objects, like strings, integers, etc.
