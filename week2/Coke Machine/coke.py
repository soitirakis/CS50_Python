cash = 50

while cash > 0:
    print(f"Amount Due: {cash}")
    cent = int(input("Amount Due: "))
    if cent == 10 or cent == 25 or cent == 5:
        cash -= cent


print(f"Change Owed: {abs(cash)}")
