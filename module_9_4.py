first = 'Мама мыла раму'
second = 'Рамена мало было'


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf8') as file:
            for data in data_set:
                file.write(str(data) + '\n')

    return write_everything


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        from random import choice
        return choice(self.words)


# part #1
print(list(map(lambda x, y: x == y, first, second)))
# part #2 - > example.txt
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# part #3
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
