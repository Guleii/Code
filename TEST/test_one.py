def a():
    pass


def b():
    pass


def c():
    pass


def decorator(func):
    print('Start %s' % func)
    func()


def main():
    decorator(a)
    decorator(b)
    decorator(c)
