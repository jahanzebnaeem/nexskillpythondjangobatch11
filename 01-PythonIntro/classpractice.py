# pay = 100000
# taxAmount = 100000*16/100
# print(pay - taxAmount)

# seq = [1, 2, 3, 4, 5]

# for item in seq:
#     print(item)

ages = {"Sam": 3, "Frank": 4, "Dan": 29}

# for key in ages:
#     print("This is the key")
#     print(key)
#     print("This is the value")
#     print(ages[key])
#     print("\n")

# print(ages["Frank"])

# mypairs = [(1, 10), (3, 30), (5, 50)]

# # Normal
# for tup in mypairs:
#     print(tup)

# # Tuple un-packing
# for item1, item2 in mypairs:
#     print(item1)
#     print(item2)

# list(range(5))

# for i in range(5):
#     print(i)

# print(list(range(1, 10)))

# x = [1, 2, 3, 4]

# out = []
# for item in x:
#     out.append(item**2)
# print(out)

# out = [item**2 for item in x]
# print(out)


# def my_func(param1='default'):
#     """
#     Docstring goes here.
#     """
#     print(param1)


# my_func('Jahanzeb')

# def giveMeHello():
#     return "hello"


# result = 'ali'
# print(result)
# result = giveMeHello()
# print(result)

def evenCheck(num):
    print("I'm checking to see if {} is even!".format(num))

    # Experienced way: (Don't need an if statement)
    print(num % 2 == 0)


evenCheck(41)
