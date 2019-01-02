# 名片列表
card_list = []


def show_menu():
    """
    显示菜单
    """
    print('*' * 50)
    print('欢迎使用【名片管理系统】V1.0')
    print('1.新建名片')
    print('2.搜索名片')
    print('3.显示全部')
    print('')
    print('0.退出系统')
    print('*' * 50)


def new_card():
    """
    创建新名片
    """
    print('-' * 50)
    print('功能：新建名片')
    # 1.提示用户输入名片信息
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    email = input('请输入邮箱：')

    # 2.将用户信息保存到字典
    card_dict = {
        'name': name,
        'phone': phone,
        'email': email,
    }
    # 3.将字典添加到名片列表
    card_list.append(card_dict)

    print(card_list)

    # 4.提示添加成功
    print('成功添加 %s ！' % card_dict['name'])


def search_card():
    """
    查询名片
    """
    print('-' * 50)
    print('功能：搜索名片')
    # 1.提示要搜索的名字
    find_name = input('请输入您要搜索的名字：')

    # 2.遍历字典
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print('姓名\t\t电话\t\t邮箱')
            print('-' * 40)

            print('%s\t\t\t%s\t\t\t%s' % (
                card_dict['name'],
                card_dict['phone'],
                card_dict['email']))
            print('-' * 40)

            # 针对查找到的名片进行下一步操作，修改、删除
            print(id(card_dict))
            deal_card(card_dict)
        else:
            print('没有找到 %s!!! 的名片' % find_name)


def show_all():
    """
    显示所有名片
    """
    print('-' * 50)
    print('功能：显示全部')
    for name in ['姓名', '电话', '邮箱']:
        print(name, end='\t\t')

    print('')
    # 打印分割线
    print('-' * 50)
    # 1.如果没有记录
    if len(card_list) == 0:
        print('您的名片包为空！')

        return

    for card_dic in card_list:
        print("%s\t\t%s\t\t%s\t\t" % (card_dic['name'],
                                      card_dic['phone'],
                                      card_dic['email'],))


def deal_card(find_dict):
    """
    操作搜索到的名片
    :param find_dict:找到名片字典
    """
    print(find_dict)

    action = input('请选择要执行的操作：'
                   '[1]修改[2]删除[0]返回上一级')
    if action == '1':
        print('修改')
        find_dict['name'] = input('请输入姓名:')
        find_dict['phone'] = input('请输入电话:')
        find_dict['email'] = input('请输入邮箱:')
        print(id(find_dict))
        print('%s 的名片修改成功' % find_dict['name'])
    elif action == '2':
        print('删除')
        card_list.remove(find_dict)

        print('删除成功!!!')
    elif action == '0':
        print('返回上一级')
    return
