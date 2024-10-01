# Домашнее задание по теме "Оператор "with".

class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):
        words_dict = {}
        for name in self.file_names:
            temp = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower().split()
                    for elem in line:
                        temp.append(elem)
                words_dict[name] = temp
        return words_dict

    def find(self, word):
        word_place = {}
        words_dict = self.get_all_words()
        for key, values in words_dict.items():
            word = word.lower()
            if word in values:
                word_place[key] = values.index(word) + 1
        return word_place

    def count(self, word):
        words_count = {}
        words_dict = self.get_all_words()
        for key, values in words_dict.items():
            count = 0
            for value in values:
                if value == word.lower():
                    count += 1
            words_count[key] = count
        return words_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
