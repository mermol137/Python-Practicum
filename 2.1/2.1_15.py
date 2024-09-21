n = int(input())
m = int(input())
t = int(input())
summ = ((n * 60 + m + t) // 60) % 24
sum1 = (n * 60 + m + t) % 60
if summ >= 10 and sum1 >= 10:
    print(f'{summ}:{sum1}')
elif summ >= 10 and sum1 < 10:
    print(f'{summ}:0{sum1}')
elif summ < 10 and sum1 >= 10:
    print(f'0{summ}:{sum1}')
elif summ < 10 and sum1 < 10:
    print(f'0{summ}:0{sum1}')
