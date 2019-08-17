num1 = int(input())
# initialize sum
sum1 = 0
# find the sum of the cube of each digit
temp1 = num1
while temp1 > 0:
   digit1 = temp1 % 10
   sum1 += digit1 ** 3
   temp1 //= 10
# display the result
if num1== sum1:
   print("yes")
else:
   print("no")
