a = [23,27,1,15,34]
for i in a:
    if i%5!=0:
        continue
    elif i%5==0:
        print(i)
        break
print("stop")


for i in range(1,11):
    n = int(input("enter the number"))
    if n<0:
        print("stopped at negative number")
        break
    else:
        print(n)
print("END")


'''n = input("enter the word")
for i in n:
    if list(n)=="a" or "e" or "i" or "o" or "u":
        break
    else:
        print(n)'''

n = input("enter the word: ")

for i in n:
    if i in ("a", "e", "i", "o", "u"):
        break
    else:
        print(i)


for i in range(1,21):
    if i==13:
        break
    elif i%2==0:
        continue 
    #    elif i%2!=0:
    print(i)

'''outputs:
15
stop

enter the number-1
stopped at negative number
END

enter the word: python
p
y
t
h


1
3
5
7
9
11
'''

#ATM PIN NEEDS TO ENTERED, IF PIN WAS INCORRECTLY ENTERED 3 TIMES PRINT CARD BLOCK AND IF HE ENTERED CORRECT PRINT ACCESS GRANTED
max_attempts = 3
for i in range(1,max_attempts+1):
    n = int(input("enter your four digit pin"))
    if n == 1234:
        print("access granted")
        break
    elif i == max_attempts:
        print("card blocked")
    else:
        print("entered incorrect pin")
        print("enter again pin")

correct_pin = 1234
attempts = 0
while attempts<3:
    pin = int(input("enter your four digit pin"))
    if pin == correct_pin:
        print("access granted")
        break
    else:
        print("wrong pin")
        attempts = attempts+1
else:
    print("card blocked")



'''
enter your four digit pin1234
access granted

enter your four digit pin3456
entered incorrect pin
enter again pin
enter your four digit pin5566
entered incorrect pin
enter again pin
enter your four digit pin666
card blocked
'''

