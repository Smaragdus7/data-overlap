one = open("file1.txt", "r")
list1 = one.readlines()

two = open("file2.txt", "r")
list2 = two.readlines()

result = [int(num.strip()) for num in list1 if num in list2]
# Write your code above 👆

print(result)


