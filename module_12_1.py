# Домашнее задание по теме "Простые Юнит-Тесты".
from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        test_w = Runner('data')
        for _ in range(10):
            test_w.walk()
        self.assertEqual(test_w.distance, 50)

    def test_run(self):
        test_r= Runner('data')
        for _ in range(10):
            test_r.run()
        self.assertEqual(test_r.distance, 100)

    def test_challenge(self):
        test_c1 = Runner('data_1')
        test_c2 = Runner('data_2')
        for _ in range(10):
            test_c1.walk()
        for _ in range(10):
            test_c2.run()
        self.assertNotEqual(test_c1.distance, test_c2.distance)


if __name__ == '__main__':
    temp = RunnerTest()
    temp.test_walk()
    temp.test_run()
    temp.test_challenge()
