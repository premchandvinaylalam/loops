a = [1,2,3,4,5,6,7,8]
for i in a:
    for j in range(1 , i + 1):
        print("*", end = "")
    print(" ")

#TO iterate for loop in dictionary
#=================================================
dict = {'J':'Java','P':'Python'}

for i in dict.keys():
    print(i,dict[i])

for i,j in dict.items():
    print(i,j)

#5. Python for loop using the zip() function for parallel iteration
#=======================================================================
a1 = ['prem','Chand','vinay']
b1 = ['cricket','volleyball','football']
for i,j in zip(a1,b1):
    print(i,j)

#Using else statement inside a for loop in Python
#====================================================
for i in a1:
    print(i)
else:
    print("done")

'''for i in a1:
    if i == 'prem':
        continue
        print(i) -- print statment should me under continue
else:
    print("done")'''


a1 = ['prem','Chand','vinay']

for i in a1:
    if i == 'prem':
        continue
    print(i)
else:
    print("done")
'''output will be:
Chand
vinay
done'''

#nested for loop
for i in a1:
    for j in b1:
        print(i,j)

#Python for loop to copy elements from one list to another
list2 = []
for i in a1:
    list2.append(i)
    print(list2)

'''output will be 
['prem']
['prem', 'Chand']
['prem', 'Chand', 'vinay']
'''

marks = [50,70,95,99,33,44]
for i in marks:
    if i > 50:
        print(f"{i} - pass")
    else:
        print(f"{i} - fail")

n = 5
'''for i in range(1,n+1):
    for j in range(1,i):
        print(" "*(n-j)+"*"*j)'''

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

'''output:
    *
   **
  ***
 ****
*****'''

n = 4
'''for i in range(1,n+1):
    for j in range(1,n+3):
        print(" "*(n-j)+"*"*i+" "*(n-j))'''

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

'''output
   *
  ***
 *****
*******
'''


#while loop

txt = ""
while txt!= 'exit':
    txt = input("enter the txt")
    print(f"you have entered {txt}")


n = 5
while n>=1:
    print(n)
    n = n-1
print("time is up")