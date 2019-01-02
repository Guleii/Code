class Person:
    """对象：人类"""
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return '我的名字叫%s ,我的体重是%.2f公斤' % (self.name, self.weight)

    def run(self):
        """跑步"""
        self.weight -= 0.5

    def eat(self):
        """吃东西"""
        self.weight += 1


xiaoming = Person('xiaoming', 75.0)
xiaoming.run()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)
