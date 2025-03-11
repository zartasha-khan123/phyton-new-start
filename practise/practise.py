# my_error = 15

# try:
#   print(my_error / 0)

# except IndexError:
#     print("index error")
# except ZeroDivisionError:
#     print("division by zero error")

# print("hello error handling")



# my_name = input("Enter your name: ")
# try:
# 	my_name = int(my_name)
# except ValueError:
# 	print("Invalid input, not a number")
# except Exception as e:
#     print("An error occured: ", {e})
    
# my_name = input("Enter your name: ")

# import math
# print(math.pi)

# class object 00p

class Human():
 def __init__(self , bhar_wala:str,age_bharwala:int):
    self.name=bhar_wala
    self.age = age_bharwala
    
    
def walk(self,isAlive:bool):
    print(f"{self.name} is now walking")
    print(isAlive)
      
  

    human=Human("zara khan",20)
    print(human.name)
    print(human.age)
    human.walk(True)
    human.walk(False)

