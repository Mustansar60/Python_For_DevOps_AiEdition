num = int(input("Enter a number you want table for: "))
#string formatting
name = input("Enter the your friend's name: ")
print(f"AsslamoAllaikum Dost,{name}")

#for loop to print multiplication table
for i in range(10):
    print(f"{num} x {i+1} = {num*(i+1)}")
    
    #while loop
   # suraj = "chand"
   # while suraj == "chand":
   #     print("Allah Pak ka nam rahay ga!") #infinite loop
  
  #real world example of while loop
choice = input("Enter the choice (press q to quit): ")

while choice !="q":
    num = int(input("Enter a number you want table for: "))
    
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
        choice = input("Enter the choice (press q to quit): ")
        