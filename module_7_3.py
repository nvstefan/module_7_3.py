# Домашнее задание по теме "Оператор "with".

# Задача "Найдёт везде":

import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, '')
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return word, result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result

finder1 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
print(finder1.get_all_words())
print(finder1.find('THE'))
print(finder1.count('thE'))