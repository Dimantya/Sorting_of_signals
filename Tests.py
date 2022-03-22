import unittest

import Automiq_main


class ListTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Старт набора тестов\n')

    @classmethod
    def tearDownClass(cls):
        print('Набор тестов пройден')

    def setUp(self):
        print("Запуск теста")

    def tearDown(self):
        print("Тест завершён\n")

    def test_green_value(self):
        print("Проверка значения переменной Green. id функции: " + self.id())
        self.assertEqual(Automiq_main.Green, 1)

    def test_blue_value(self):
        print("Проверка значения переменной Blue. id функции: " + self.id())
        self.assertEqual(Automiq_main.Blue, 2)

    def test_red_value(self):
        print("Проверка значения переменной Red. id функции: " + self.id())
        self.assertEqual(Automiq_main.Red, 3)

    def test_green_list1(self):
        print("Проверка количества элементов Green в списке неотсортированных сигналов. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1.count(Automiq_main.Green), 6)

    def test_blue_list1(self):
        print("Проверка количества элементов Blue в списке неотсортированных сигналов. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1.count(Automiq_main.Blue), 6)

    def test_red_list1(self):
        print("Проверка количества элементов Red в списке неотсортированных сигналов. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1.count(Automiq_main.Red), 4)

    def test_green_list1sorted(self):
        print("Проверка количества элементов Green в списке отсортированных сигналов. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1_sorted.count(Automiq_main.Green), 6)

    def test_blue_list1sorted(self):
        print("Проверка количества элементов Blue в списке отсортированных сигналов. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1_sorted.count(Automiq_main.Blue), 6)

    def test_red_list1sorted(self):
        print("Проверка количества элементов Red в списке отсортированных сигналов. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1_sorted.count(Automiq_main.Red), 4)

    def test_unsorted_list_true(self):
        print("Проверка соответствия всех элементов неотсортированного списка. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1, [2, 2, 1, 2, 3, 1, 1, 1, 3, 3, 2, 1, 2, 2, 3, 1])

    def test_sorted_list_true(self):
        print("Проверка соответствия всех элементов отсортированного списка. id функции: " + self.id())
        self.assertEqual(Automiq_main.list1_sorted, [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3])

    def test_unsorted_numbers(self):
        print("Проверка количества элементов неотсортированного списка. id функции: " + self.id())
        self.assertEqual(Automiq_main.numbers_of_unsorted_elements, 16)

    def test_sorted_numbers(self):
        print("Проверка количества элементов отсортированного списка. id функции: " + self.id())
        self.assertEqual(Automiq_main.numbers_of_sorted_elements, 16)

    def test_equality(self):
        print("Проверка соответствия количества элементов неотсортированного и отсортированного списка. id функции: " + self.id())
        self.assertEqual(Automiq_main.numbers_of_unsorted_elements, Automiq_main.numbers_of_sorted_elements)


if __name__ == '__main__':
    unittest.main()
