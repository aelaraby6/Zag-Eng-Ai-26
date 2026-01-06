# name = "abdelrahman"
# age = 20
# height = 176.5
# is_student = True

# print(f"{type(name)} {type(age)} {type(height)} {type(is_student)}")


################################

# while True:
#     try:
#         num1 = int(input("Enter First Number : "))
#         num2 = int(input("Enter Second Number : "))  

#         print(f"Sum : {num1+num2}")
#         print(f"Difference : {abs(num1-num2)}")
#         print(f"Product : {num1*num2}")
#         print(f"Division : {num1/num2}")

#         break
#     except ValueError:
#         print("Please enter number")

#     except ZeroDivisionError:
#         print("Please enter number > 0 on second input")


#####################################

# while True:
#     try:
#         num = int(input("Enter Number : "))

#         if num > 0:
#             print("Positive")
#         elif num < 0:
#             print("Negative")
#         else:
#             print("Zero")

#         break

#     except ValueError:
#             print("Please Enter Number")



########################################

# for i in range(1,21):
#     if i%2==0:
#         print(i, end=" ")


#################################

# secret = 7
# while True:
#     try:
#         num = int(input("Guess Number :"))
#         if num == secret:
#             print("Right !!!")
#             break

#     except ValueError:
#         print("please write number")

################################################

# with open("data.txt","w") as f:
#     f.write("Hello,\n")
#     f.write("I am abdelrahman,\n")

# with open("data.txt" , "r") as f:
#     content = f.read()
#     print(content)

##################################################

# lst = [1,1,1,1,2]

# print(f"Sum : {sum(lst)}")
# print(f"Max : {max(lst)}")

# lst.reverse()
# print(f"{lst}")


#################################################

# cities = ("New York", "London", "Paris", "Tokyo", "Sydney")

# print(f"First : {cities[0]}")
# print(f"Second : {cities[-1]}")


#################################################
