#Q1
from operator import indexOf, le


a ="Hello WOrld"
b ="Wehlr lldoo"
character = input("Enter the character")
character.lower()
ch =input("enter the character to replace")
   
for i in a:
    if i == character:
        idx = a.index(i)
        print(a[0:idx]+a[idx+1:])
    else:
        print ("")

# #Q2


#cnt =0
for i in a:
    if i == character:
        cnt+=1
print(cnt)

# #Q3
emptyDict = {}
for i in a:

# #Q4
 c = a[::-1]
if c == a:
    print("Palindrome")
else:
    print("Not Palindrome")  

#Q5

if (character =='a' or character=='e'  or character=='i'  or character=='o'  or character=='u'):
    print("Vowel")
else:
    print("consonant") 

# Q6
if (ord(character) <=48 and ord(character)>=57):
    print("digit")
else:
    print("Not Digit")

# #Q7

if character.isdigit():
    print("digit")
else:
    print("NOt digit")

# #Q8
str=""
for c in a:
    if c ==' ':
        str+=ch
    else:
        str+=c
print(str)

# #Q9

print(a.replace(' ',ch))

# #Q10
print(a.upper())

# #Q11
str1=""
for i in a:
    if (i=='a' or i=='e' or i=='i' or i=='u' or i=='o' or i=='A' or i=='E' or i=='I' or i=='U' or i=='O'):
        if i.isupper():
            str1+=i.lower()
        else:
            str1+=i.upper()
    else:
        str1+=i

print(str1)   
   
# #Q12
arr=[1,2,3,4,6,7,8,]
arr1 =[4,6,5,23,11,89,76,4,23,11,6]
for i in range[0:len(arr)]:
    if arr[i]<0:
        print(i+1)
        break
    arr[i]=-1*arr[i]

#@13



#Q14

#Q15
print(len(arr)==len(arr1))

#Q16
arr1.sort()
print("smallest number =")
print(arr[0])
print("largest number =")
print(arr[len(arr1)-1])

#Q17
print("Second highest number in the array =")
print(arr[len(arr)-2])

#Q18
print(arr[len(arr)-1])
print(arr[len(arr)-2])


#Q19

thisset =[]
for i in arr1:
    thisset.append(i)
print(thisset)

#Q20
print(arr[len(arr)-1])
print(arr[len(arr)-2])

#Q21
for i in range(len(arr)-1,-1,-1):
    print(arr[i])

#Q22

def reverse(arr):
    return [i for i in reversed(arr)]
print(reverse(arr))

l=[]
for i in arr:
    l.insert(0,i)
print(l)

#Q23
print(len(arr))

#Q24
arr.append(9)
print(arr)


     
    