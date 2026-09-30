porog = float(input())
n = int(input())

err = 0
count_bigger = 0
maxx = 0

for i in range(n):
    znach = input()
    if znach == "error":
        err += 1
    else: 
        temp = float(znach)
        if temp > porog:
            count_bigger += 1
            if maxx == 0 or temp > maxx:
                maxx = temp

print(n)
print(err)
print(count_bigger)
print(f"{maxx:.1f}")