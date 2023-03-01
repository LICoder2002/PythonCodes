def rmb_to_usd(amount):
    # 人民币转美元
    return amount * 0.1452


def usd_to_rmb(amount):
    # 美元转人民币
    return amount * 6.8833


while True:
    choice = input("请选择要进行的操作：1. 人民币转美元 2. 美元转人民币 3. 退出\n")
    if choice == '1':
        rmb = float(input("请输入人民币金额："))
        usd = rmb_to_usd(rmb)
        print("兑换后的美元金额为：", usd)
    elif choice == '2':
        usd = float(input("请输入美元金额："))
        rmb = usd_to_rmb(usd)
        print("兑换后的人民币金额为：", rmb)
    elif choice == '3':
        break
    else:
        print("输入错误，请重新输入。")
