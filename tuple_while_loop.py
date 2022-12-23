tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)

sum = 0
index = 0

while index < len(tuple1):
    sum = sum + tuple1[index]
    # increment index
    index = index + 1

print(sum)