porog = float(input())
n = int(input())

err = 0

for i in range(n):
    znach = input()

    if znach == "error":
        err += 1

print(n)
print(err)