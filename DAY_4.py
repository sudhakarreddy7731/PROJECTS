#Smart List filter for separating strings and numbers from a Common list
n=int(input("Enter the length data list: "))
print("if you want to stop adding elements.. Type END to ")
data = []*n
for i in range(n):
    x = input("Enter Data into the list: ")
    if x == "END":
        break
    data.append(x)

numbers = []
strings = []
Numcount = 0
Strcount = 0

for item in data:
    isnumber = True

    if item == "":
        isnumber = False
    else:
        for ch in item:
            if ch < "0" or ch > "9":
                isnumber = False
                break

    if isnumber:
        numbers.append(int(item))
        Numcount = Numcount + 1

    elif item != "":
        strings.append(item)
        Strcount = Strcount + 1
print("Numbers List : ", numbers)
print("Strings List: ", strings)


name = input("Enter your name: ")

Namelen = 0
for c in name:
    Namelen = Namelen + 1
#if even length
if Namelen % 2 == 0:

    if len(numbers) > 0:
        temp = []
        for i in range(1, len(numbers)):
            temp.append(numbers[i])
        numbers = temp
        Numcount = Numcount - 1

    if len(strings) > 0:
        temp = []
        for i in range(1, len(strings)):
            temp.append(strings[i])
        strings = temp
        Strcount = Strcount - 1


#if odd length,
else:

    if len(numbers) > 0:
        temp = []
        for i in range(len(numbers)-1):
            temp.append(numbers[i])
        numbers = temp
        Numcount = Numcount - 1

    if len(strings) > 0:
        temp = []
        for i in range(len(strings)-1):
            temp.append(strings[i])
        strings = temp
        Strcount = Strcount - 1

print("Numbers List After performing option 2:", numbers)
print("Strings List After performing option 2:", strings)
print("Total Numbers:", Numcount)
print("Total Strings:", Strcount)
