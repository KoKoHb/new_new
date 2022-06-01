'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на
стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
'''
n = int(input())
l = []
for i in range(1, n + 1):
    l.append(input().split(";"))
teams = set()
for i in range(len(l)):
    teams.add(l[i][0])
    teams.add(l[i][2])
out = {i: [0, 0, 0, 0, 0] for i in teams}
out_keys = [i for i in out.keys()]
for i in l:
    for j in range(len(out_keys)):
        if out_keys[j] in i:
            out[out_keys[j]][0] += 1
            if int(i[1]) == int(i[3]):
                out[out_keys[j]][2] += 1
                out[out_keys[j]][4] += 1
        if out_keys[j] == i[0]:
            if int(i[1]) > int(i[3]):
                out[out_keys[j]][1] += 1
                out[out_keys[j]][4] += 3
            if int(i[1]) < int(i[3]):
                out[out_keys[j]][3] += 1
        elif out_keys[j] == i[2]:
            if int(i[1]) < int(i[3]):
                out[out_keys[j]][1] += 1
                out[out_keys[j]][4] += 3
            if int(i[1]) > int(i[3]):
                out[out_keys[j]][3] += 1
for j in range(len(out)):
    print(f"{out_keys[j]}:{out[out_keys[j]][0]} {out[out_keys[j]][1]} {out[out_keys[j]][2]} {out[out_keys[j]][3]} {out[out_keys[j]][4]}")
