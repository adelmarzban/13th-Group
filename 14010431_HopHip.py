
#### Hope Game by Applying LIST ######
Adad = int(100)
a = [*range(1, Adad+1)]
for i in range(0, len(a)):
    if a[i] % 3 == 0 and a[i] % 5 == 0:
        a[i] = "Hope Hip"
    elif a[i] % 5 == 0:
        a[i] = "hope"
    elif a[i] % 3 == 0:
        a[i] = "hip"
print(a)



#### Simple Hope Game ######

Adad = int(100)
for i in range(1, Adad + 1):
    if i % 5 == 0 and i % 3 == 0:
        i = "Hope Hip"
    elif i % 5 == 0:
        i = "Hope"
    elif i % 3 == 0:
        i = "Hip"
    print(i)