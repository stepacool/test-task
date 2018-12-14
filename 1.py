from xml.etree import ElementTree as ET
import sys
from datetime import datetime

"""
Программа читает файл, название которого можно передать при вызове, либо ввести.
Подразумевается, что работники не остаются на ночь (время прихода и ухода всегда в один день).
"""


def processPerson(person):
    """
    Получает <person>........</person>, возвращает извлеченную дату и время прибывания человека за эту дату.
    """
    children = list(person)
    start = children[0].text
    end = children[1].text
    date = start.split()[0]
    frmt = '%H:%M:%S'
    start_time = start.split()[1]
    end_time = end.split()[1]
    tdelta = datetime.strptime(end_time, frmt) - datetime.strptime(start_time, frmt)
    return date, tdelta


def main(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    people = root.findall('.//person[@full_name]')  # Нахожу все теги <person>.....</person>
    ans = {}

    for person in people:
        date, timedelta = processPerson(person)
        if date in ans:
            ans[date] += timedelta
        else:
            ans[date] = timedelta

    for date, time, in ans.items():  # Вывод ответа, построчно пишет дату - время
        print(str(date) + " — " + str(time))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Введите имя xml файла: ")

    main(filename)
