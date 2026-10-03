#Program 1 : Find whether a number is +ve or -ve
num=int(input("Enter any number"))
if(num==0):
    print("Entered Zero")
elif(num > 0 ):
    print("Positive")
else:
    print("Negative")
#Program 2: Sum of given numbers
numbers=[12,5,8,20,15]
sum=0
for i in numbers:
    sum=sum+i
print("Sum of given numbers is ",sum)
#Program 3: Count even and odd numbers
nums = [10, 15, 22, 31, 44, 57, 60, 73]
oddCount=0
evenCount=0
for i in nums:
    if(i%2==0):
        evenCount=evenCount+1
    else:
        oddCount=oddCount+1
print("Number of Even numbers:",evenCount)
print("Number of Odd numbers:",oddCount)
#Program 4: Find the largest number
numList = [23, 7, 45, 12, 89, 34, 56]
large=numList[0]
print(large)
for i in range(len(numList)):
  if(large < numList[i]):
      large=numList[i]
print(large)
#print("Largest Number is",large)
#Program 5: Calculate Average
marks = [80, 75, 90, 85, 70]
sum=0
avg=0
len=marks.len()
for i in marks:
    sum=sum+i;
    avg=sum/len
print("average is", avg)