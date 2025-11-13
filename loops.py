#for loops only works for data structure things, i wont work for integers

#for i in 36:
#    print(i) # it wont work

a=[36]
for i in a:
    print(i) # it will work

#for has two things 1)iterable -- which we will define or data needs to be iterated
#2)temparoray variable -- we use this to iterate

#syntax
#for temp in iterable:
#    print(temp)

for i in range(1,51):
    print(i)
 #   print(i,end="")


type(range(5))

for i in range(10,21):
    print(i)

for i in range(1,8):
    print("I love python")

a = [5,4,3,2,1]
for i in a:
    print(i)
print("finished")




import time
print("start")
print("Analyzing.............")
time.sleep(3)
print("your data is ready")
time.sleep(5)
for i in range(5,0,-1):  #range(start,end+1,step) -- to move forward , range(start,end-1,step in minus(-1 0r -2))
    print(i)
print("finished")


for i in range(1,6):
        for j in range(1,i+1):
            print("*",end = "")
        print()

'''n = int(input("enter the number: "))
for i in range(1, n):
     for j in range(1, i + 1):
          print(j, end="")
    print(" ")'''


n = int(input("Enter the number: "))
for i in range(1, n):
    for j in range(1, i + 1):
        print(j, end="")
    print(" ")

'''a = [10,20,30,40,50,60]
sum = 0
for i in a:
    sum = sum+i
    print(sum)
print("total sum is :" sum)'''

a = [10, 20, 30, 40, 50, 60]
sum = 0
for i in a:
    sum = sum + i
    print(sum)
print("total sum is:", sum)


b = [10,20,30,40]
sum = 0
for i in b:
    sum = sum + i
    print(sum)
print()


