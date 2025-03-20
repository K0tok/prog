a, b = str(input()), str(input())
maxLen = max(len(a), len(b))
minLen = min(len(a), len(b))
s = ""
for i in range(maxLen - minLen):
    if len(a) > len(b):
        b = "0" + b
    elif len(b) > len(a):
        a = "0" + a

for j in range(maxLen):
    x = (int(a[j]) + int(b[j])) % 10
    s += str(x)

print(s)
