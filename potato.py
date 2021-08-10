def potato():
    n = 0
    while True:
        if n != 100:
            print(n)
            n += 1
        else:
            break
def NotPotato():
    while True:
        for num in range(100):
            if num%5 ==0:
                print(num)
        break
potato()
print("\n\n\n")
NotPotato()

