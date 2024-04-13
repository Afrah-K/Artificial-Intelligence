#How do you reverse a string?
x = "Hello World"[::-1]

#How do you determine if a string is a palindrome 
s = "Hello World"
def isPalindrome(s):
    return s == s[::-1]

if isPalindrome(s):
    print('yes')
else:
    print('no')
    
#How do you calculate the number of numerical digits in a string?

string = 'Python2334'

total_digits = 0
total_letters = 0

for numeric in string:
    if numeric.isnumeric():
        total_digits += 1
    else:
        total_letters += 1
        
print(total_digits)
print(total_letters)

#Count the occurence of a character

string = "GeeksforGeeks"

count = 0

for i in string:
    if i == 'e':
        count += 1 
        
print(count)

test1 = "Hekko"
test2 = "Hello"

unique_val = []
unique_val2 = []
for char1, char2 in zip(test1, test2):
    if char1 != char2:
        unique_val += char1
        unique_val2 += char2

print(unique_val)
print(unique_val2)

#Check if the two strings are annagram
str1 = "silent"
str2 = "listen"

def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    
anagram(str1, str2)

#Matching integer elements in an array
int = 3
array = [1,2,2,5,6,3,3]
sum = 0

for x in array:
    if int == array[x]:
        sum += 1
    
#reverse an array
print(array[::-1])

#How do you find the max value in an array?
array = [1,4,5,6,3,2,7]

max = array[0]

for i in array:
    if array[i] > max:
        max = array[i]
        print(max)
        
#How do you sort an array of integers in ascending order?
arr = [3,5,6,7,2,1]
arr.sort()
print(arr)
            
 
#Check if theres a prime number
num = 3
if num == 1:
    print("Not a prime number")
elif num > 1:
    for i in range(2, num):
        if(num % i)==0:
            print(num, "isnt a prime number")
            break
    print(num, "is a prime number")
    
      
#Create a fibonacci sequence using recursion
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return( recur_fibo(n-1)+ recur_fibo(n-2))

nterms = 10
if nterms <= 0:
    print("Please enter a positive integer")
else: 
    for i in range(nterms):
        print(recur_fibo(i))
        
#sum of two integers
def two_sum(first, second):
    return(first + second)
    
x = two_sum(3,4)
print(x)

#How do you find the average of number in a list
arrs = [1,3,5,6,7]
avg = sum(arrs)/len(arrs)

#How do you check if an integer is even or odd?
num = int(input("Enter any number if its odd or even:"))

if(num%2) == 0:
    print("The number is even")
else: 
    print("The number is odd")
    
#How do you find the middle element of a linked list?
