import cards_tools

while True:

    cards_tools.show_menu()

    action = input('请选择功能：')
    print('您选择的操作是 %s' % action)

    # 根据用户选择进行后续操作
    if action in ['1', '2', '3']:

        if action == '1':

            cards_tools.new_card()

        elif action == '2':

            cards_tools.search_card()

        elif action == '3':

            cards_tools.show_all()

    elif action == '0':

        print('欢迎再次使用【名片管理系统】')
        break
    else:
        print('输入有误，请重新输入')

