# Лесенка Марио из курса cs50_2015
n = int(input())
while n < 0 or n > 24:
    n = int(input())
range_n = n
for i in range(n // 2 + 2):
    if i > 1:
        a = i * '#'
        print(a.rjust(range_n))
