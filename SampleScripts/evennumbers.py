# Python program to print Even Numbers in a List

# list of numbers
# list1 = [10, 21, 4, 45, 66, 93]

# # iterating each number in list
# for num in list1:

# 	# checking condition
# 	if num % 2 == 0:
# 		print(num, end=" ")


# Python program to print Even Numbers in given range

firstnumber = int(input("please enter start number: "))
lastnumber = int(input("please enter end number: "))

for num in range(firstnumber, lastnumber +1):
    if num % 2 == 0:
        print(num, end=" ")
