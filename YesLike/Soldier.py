class Gun:
    def __init__(self, model):
        # 枪的类型
        self.model = model
        # 子弹装填数
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count
        print('装填完成...')

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print('没有子弹了...')
            return

        # 发射一颗子弹
        self.bullet_count -= 1
        print('%s发射子弹[%d]...' % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # 1.判断是否有枪
        if self.gun is None:
            print('[%s] 还没有枪!' % self.name)
            return
        # 2.高喊口号
        print('冲啊...[%s]' % self.name)

        # 3.让枪装好子弹
        self.gun.add_bullet(50)

        # 4.让子弹发射
        self.gun.shoot()


ak47 = Gun('ak47')
soldier_76 = Soldier('士兵76')
soldier_76.gun = ak47
soldier_76.fire()
