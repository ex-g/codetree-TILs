money = int(input())

max_object = "no"

if money >= 3000:
    max_object = "book"
elif money >= 1000:
    max_object = "mask"

print(max_object)