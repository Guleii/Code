class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print('%s蹦蹦跳跳的....' % self.name)


class DogGod(Dog):
    def __init__(self, name):
        self.name = name

    def game(self):
        print('%s飞来飞去的....' % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print('%s和%s快乐地玩耍...' % (self.name, dog.name))
        dog.game()


wang = Dog('旺财')
cai = DogGod('飞天旺')
xiaoming = Person('小明')
xiaoming.game_with_dog(wang)
xiaoming.game_with_dog(cai)
