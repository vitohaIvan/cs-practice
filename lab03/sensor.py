porog = float(input())
n = int(input())

err = 0
count_bigger = 0
maxx = 0
sr_znach = 0
count = 0

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
        sr_znach += temp
        count += 1
sr_znach = sr_znach/count

print(n)
print(err)
print(count_bigger)
print(f"{maxx:.1f}")
print(f"{sr_znach:.1f}")