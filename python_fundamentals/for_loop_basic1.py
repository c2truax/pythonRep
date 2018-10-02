#1. Basic
for count in range(0,151):
    print(count)

#2.Multiples of Five
for count in range(5,1000000):
    if count%5 == 0:
        print(count)

#3. Counting the Dojo way
for count in range(1,101):
    if count%10 == 0:
        print("Coding Dojo")
    elif count%5 == 0:
        print("Coding")
    else:
        print(count)

#4. Whoa. That Sucker's Huge
x = 0
for count in range(1,500001,2):
    x += count

print(x)

#5 Countdown by Fours
for count in range(2018,0,-4):
    print(count)

#6 Flexible Countdown
lowNum = 2
highNum = 9
mult = 3

for count in range(lowNum,highNum+1):
    if count%mult == 0:
        print(count)

# a common mistake
list = [3,5,1,2]
for i in list:
    print(i)

#print: 
#3
#5
#1
#2

list = [3,5,1,2]
for i in range(list):
    print(i)

# error

list = [3,5,1,2]
for i in range(len(list)):
    print(i)

#print
#0
#1
#2
#3

    
