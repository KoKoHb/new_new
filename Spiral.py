'''
Выведите таблицу размером n×n, заполненную числами от 1 до n**2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
def spiral(n):
    lst = [[j * 0 for j in range(n)] for i in range(n)]
    c, nums, n2 = 0, 1, n
    while nums < n ** 2 + 1:
        for i in range(c, n2):
            lst[c][i] = nums
            nums += 1
        for i in range(c + 1, n2):
            lst[i][n2 - 1] = nums
            nums += 1
        for i in range(n2 - 2, c - 1, -1):
            lst[n2 - 1][i] = nums
            nums += 1
        for i in range(n2 - 2, c, -1):
            lst[i][c] = nums
            nums += 1
        c += 1
        n2 -= 1
    for i in lst:
        print(*i)

spiral(int(input()))
