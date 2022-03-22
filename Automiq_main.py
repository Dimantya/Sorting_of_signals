# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import Tk, Frame
from tkinter import messagebox
import logging

# # Создание Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание обработчик для записи данных в файл
logger_handler = logging.FileHandler('python_logging.log')
logger_handler.setLevel(logging.INFO)

# Создание Formatter для форматирования сообщений в логе
logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Добавление Formatter в обработчик
logger_handler.setFormatter(logger_formatter)

# Добавление обработчика в Logger
logger.addHandler(logger_handler)
# Формирование информационного сообщения для записи в логи программы
logger.info('Настройка логгирования окончена, программа запущена')

# Добавление переменных для создания соотношения Green<Blue<Red
Green = 1
Blue = 2
Red = 3
# Оздание заданного списка неотсортированных сигналов согласно ТЗ
list1 = [Blue, Blue, Green, Blue, Red, Green, Green, Green, Red, Red, Blue, Green, Blue, Blue, Red, Green]
# Пересчитываем количество элементов списка для дальнейшего сравнения с итоговым списком
numbers_of_unsorted_elements = len(list1)

# Сортировка списка в порядке возрастания присвоенных переменных
list1_sorted = sorted(list1)
# Пересчитываем количество элементов итогового списка
numbers_of_sorted_elements = len(list1_sorted)

# # Попытка генерации своего списка
# a = [Blue, Green, Red]
# b = random.choices(a, k=6)
#
# print(b)


# Функция закрытия окна программы
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        logger.info('Программа закрыта\n\n\n')
        root.destroy()


root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
# Название окна
root.title("Сортировка сигналов")
# Размер окна
root.minsize(width=1000, height=600)
# Заголовок-надпись в окне
header = "Эта программа поможет тебе упорядочить \n цвета в следующем порядке Green - Blue - Red\n"
# Форматирование текста надписи
lbl = Label(root, text=header, font=("Arial Bold", 20))
# Размещение надписи
lbl.pack()


# Функция для добавления в окно программы неотсортированного набора сигналов
def unsorted_elements():
    logger.info('Нажатие кнопки добавления набора сигналов')
    logger.info('Добавление предустановленного набора сигналов')
    # Начальная позиция сигнала по оси Х
    xos = 20
    # Счетчик числа сигналов
    count = 0
    # Перебор всех элементов списка и их добавление в окно программы
    for element in list1:
        if element == Green:
            # Добавление фрейма сигнала и его размещение в окне программы
            frame1 = Frame(master=root, width=50, height=50, bg="green")
            frame1.pack(side=LEFT, padx=10, pady=10)
            frame1.place(x=xos, y=175)
            # Смещение начальной позиции по оси Х для добавления следующего сигнала
            xos += 60
            # Логирование добавления сигнала
            logger.info('Добавлен зеленый сигнал')
            # Приращение счетчика
            count += 1
        elif element == Blue:
            frame1 = Frame(master=root, width=50, height=50, bg="blue")
            frame1.pack(side=LEFT, padx=10, pady=10)
            frame1.place(x=xos, y=175)
            xos += 60
            logger.info('Добавлен синий сигнал')
            count += 1
        elif element == Red:
            frame1 = Frame(master=root, width=50, height=50, bg="red")
            frame1.pack(side=LEFT, padx=10, pady=10)
            frame1.place(x=xos, y=175)
            xos += 60
            logger.info('Добавлен красный сигнал')
            count += 1
        else:
            break
        logger.info('Общее количество сигналов = ' + str(count))


# Кнопка добавления неотсортированного набора данных в окно программы
btn = Button(root, text="Добавить предустановленный набор", font=("Arial Bold", 20), command=unsorted_elements)
btn.pack()


# Функция для добавления в окно программы отсортированного набора сигналов, логика аналогична предыдущей функции
def sorted_elements():
    xos = 20
    logger.info('Нажатие кнопки сортировки сигналов')
    logger.info('Сортировка полученного набора сигналов!')
    count = 0
    for element in list1_sorted:
        if element == Green:
            frame1 = Frame(master=root, width=50, height=50, bg="green")
            frame1.pack(side=LEFT, padx=10, pady=10)
            frame1.place(x=xos, y=325)
            xos += 60
            count += 1
            logger.info('Добавлен зеленый сигнал')
        elif element == Blue:
            frame1 = Frame(master=root, width=50, height=50, bg="blue")
            frame1.pack(side=LEFT, padx=10, pady=10)
            frame1.place(x=xos, y=325)
            xos += 60
            count += 1
            logger.info('Добавлен синий сигнал')
        elif element == Red:
            frame1 = Frame(master=root, width=50, height=50, bg="red")
            frame1.pack(side=LEFT, padx=10, pady=10)
            frame1.place(x=xos, y=325)
            xos += 60
            count += 1
            logger.info('Добавлен красный сигнал')
        else:
            break

        logger.info('Общее количество сигналов = ' + str(count))


# Кнопка для добавления отсортированного списка сигналов в окно программы
btn2 = Button(root, text="Отсортировать сигналы", font=("Arial Bold", 20), command=sorted_elements)
btn2.pack()
btn2.place(x=325, y=250)

# Главный цикл запуска окна в Tkinter
root.mainloop()