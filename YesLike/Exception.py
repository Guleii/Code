def input_password():
    # 1.提示用户输入密码
    pwd = input('请输入密码：')

    # 2.判断密码位数
    if len(pwd) >= 8:
        return pwd

    # 3.密码长度不够，需要抛出异常
    ex = Exception('密码不足8位')
    raise ex


try:
    user_pwd = input_password()
    print(user_pwd)
except Exception as result:
    print('发现错误:%s' % result)
