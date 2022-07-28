### How to Revers Alphabetic String?? ###


## Method 1 ##
alphabetstring = "abcdefghijklmnopqrstuvwxyz"
a = list(reversed(alphabetstring))
print(a)

## Method 2 ##

lst = []
alphabetstring = "abcdefghijklmnopqrstuvwxyz"
for i in alphabetstring:
    lst.append(i)
lst.reverse()
print(lst)