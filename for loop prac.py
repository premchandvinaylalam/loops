'''
*
**
***
****
*****'''

n = 5
for i in range(1,n+1):
    print("*"*i)


'''
  *
 ***
*****'''

n = 3
for i in range(1,n+1):
    print(" "*(n-i)+"*"*((2*i)-1))

'''
*****
****
***
**
*'''

n = 5
for i in range(1,n+1):
    print("*"*((n+1)-i)+" "*(i-1))

'''
1
1 2
1 2 3 
1 2 3 4
1 2 3 4 5'''

n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end = " ")
    print(" ")


'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1'''



n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

n = int(input("enter the number"))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
        if i>500:
            break
        if i>150:
            continue
        elif i%5==0:
            print(i)
        