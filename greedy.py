# cs50_2015
# жадный алгоритм, найти наименьшее количество монет, которыми пожно выдать сдачу
def greedy(n):
    cents = n * 100
    quarter, dime, nickel, penny = 25, 10, 5, 1
    coins = 0
    coins += cents // quarter
    cents = cents % quarter
    coins += cents // dime
    cents = cents % dime
    coins += cents // nickel
    cents = cents % nickel
    coins += cents // penny
    return coins


def greegy2(n):
    cents = n * 100
    coins = 0
    for i in (25, 10, 5, 1):
        coins += cents // i
        cents = cents % i
    return coins
