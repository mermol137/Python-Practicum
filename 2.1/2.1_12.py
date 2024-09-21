a = input()
b = input()
c = ''
if len(a) > len(b):
    b = '0' + b
else:
    a = '0' + a
for i in range(1, min(len(a), len(b)) + 1):
    c = str((int(a[-i]) + int(b[-i])))[-1] + c
print(c)
