# Домашнее задание по теме "Методы Юнит-тестирования".
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
                    finishers[place] = participant.__str__()
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    def setUp(self):
        global usein, andrey, nik
        usein = Runner('Усейн', 10)
        andrey = Runner('Андрей', 9)
        nik = Runner('Ник', 3)

    def test_tour_1(self):
        tour = Tournament(90, usein, nik)
        res = tour.start()
        all_results.append(res)
        key = list(res.keys())[-1]
        self.assertTrue(res[key].__eq__('Ник'))

    def test_tour_2(self):
        tour = Tournament(90, andrey, nik)
        res = tour.start()
        all_results.append(res)
        key = list(res.keys())[-1]
        self.assertTrue(res[key].__eq__('Ник'))

    def test_tour_3(self):
        tour = Tournament(90, usein, andrey, nik)
        res = tour.start()
        all_results.append(res)
        key = list(res.keys())[-1]
        self.assertTrue(res[key].__eq__('Ник'))

    @classmethod
    def tearDownClass(cls):
        for elem in all_results:
            print(elem)


if __name__ == '__main__':
    unittest.main()
