#adieu using inflect
import inflect

names =[]
p = inflect.engine()

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break
result = p.join(names)
print(f"Adieu, adieu, to {result}")
