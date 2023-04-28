f = open('spiski/file.txt')

zagolovok = f.readline()
print(zagolovok)

names = []


for i in f:
    data = i.split()
    name = data[0]
    names.append(name)
    try:
        age = int(data[1])
    except:
        age = None
    city = data[2]
    print(
        "Name", name,
        "Age", age,
        "City", city
    )


print('-'*50)
print(names)