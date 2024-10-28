# Домашнее задание по теме "Логирование".
import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}.')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


first = Runner('Вося', 10)
second = Runner('Илья', 5)
# third = Runner('Арсен', 10)

t = Tournament(101, first, second)
print(t.start())


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            fst = Runner(22, 5)
            for _ in range(10):
                fst.walk()
            self.assertEqual(fst.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except ValueError as verr:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            scd = Runner('Вося', -5)
            for _ in range(10):
                scd.run()
            self.assertEqual(scd.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError as terr:
            logging.warning(msg='Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        test_c1 = Runner('data_1')
        test_c2 = Runner('data_2')
        for _ in range(10):
            test_c1.walk()
        for _ in range(10):
            test_c2.run()
        self.assertNotEqual(test_c1.distance, test_c2.distance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w",
                        format="%(asctime)s | %(levelname)s | %(message)s", encoding="utf-8")


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            first = Runner(22, 5)
            for _ in range(10):
                first.walk()
            self.assertEqual(first.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except ValueError as verr:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            second = Runner('Вося', -5)
            for _ in range(10):
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError as terr:
            logging.warning(msg='Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        test_c1 = Runner('data_1')
        test_c2 = Runner('data_2')
        for _ in range(10):
            test_c1.walk()
        for _ in range(10):
            test_c2.run()
        self.assertNotEqual(test_c1.distance, test_c2.distance)
