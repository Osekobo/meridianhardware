input1 = (input("Enter input 1: "))
input2 = (input("Enter input 2: "))
input3 = (input("Enter input 3: "))
input4 = (input("Enter input 4: "))

if input1 > input2 and input1 > input3 and input1 > input4:
    print("Input 1 is the largest!")
elif input2 > input1 and input2 > input3 and input2 > input4:
    print("Input 2 is the largest!")
elif input3 > input1 and input3 > input2 and input3 > input4:
    print("Input 3 is the largest!")
elif input4 > input1 and input4 > input3 and input4 > input2:
    print("Input 4 is the largest!")
elif input1 or input2 or input3 or input4 == float:
    print("Enter a number please!")
else:
  print("Wrong input!")

input1 = int(input("Enter temperature: "))
if input1 > 30:
    print("Temperature is too high")
elif input1 >= 15 and input1 <= 30:
    print("Normal temperature")
else:
    print("Cold temperature")

age = int(input("Enter Age: "))
if age >= 18:
    lisence = str(input("Do you have a driving license?")).lower()
    if lisence == "yes":
        print("Allowed to drive")
    else:
        print("Not allowed to drive")
else:
    print("You are too young to drive")

x = [10,20,30,40]
i = 0
for e in x:
  i = i + e
  print(i)

x = list(range(10, 51))
for e in x:
  if e % 2!=0:
   print(len(e)==10)


# using formated strings
n = int(input("Enter number: "))
a = list(range(0, 11))
for e in a:
    f = n * e
    print(f"{n} * {e} = {f}")
