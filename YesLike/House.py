class HouseItem:
    """家具"""
    def __init__(self, name, area):
        """
        :param name:家具名
        :param area:家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 的占地面积是 %.2f " % (self.name, self.area)


class House:
    """房间"""
    def __init__(self, house_type, area):
        """
        :param house_type:房间类型
        :param area: 初始面积
        """
        self.house_type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []

    def __str__(self):
        return '户型:%s\n初始面积:%.2f[剩余面积:%.2f]\n家具:%s' % (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self, item):
        print('要添加 %s' % item)

        # 1.判断要添加的家具占地面积是否小于剩余面积
        if item.area > self.free_area:
            print('%s 的面积太大， 不能添加到房子中!' % item.name)
            return
        else:
            self.item_list.append(item.name)
            self.free_area -= item.area
            print('剩余面积是 %.2f' % self.free_area)
            print('现有家具: %s' % self.item_list)


item1 = HouseItem('bed', 2.5)
h1 = House('一套一', 60)
h1.add_item(item1)

