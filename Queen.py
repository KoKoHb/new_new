import requests
'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''
word = 'we'
adress = 'https://stepic.org/media/attachments/course67/3.6.3/'
url = str()

with open('dataset_3378_3.txt', 'r') as f:
    for line in f:
        url = str(line.strip())

r = requests.get(url)
url = adress + r.text
while True:
    q = requests.get(url)
    if word in q.text:
        print(q.text)
        break
    url = adress + q.text

