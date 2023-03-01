# main.py

import currency_exchange

while True:
    choice = input("请选择要进行的操作：1. 人民币转美元 2. 美元转人民币 3. 退出\n")
    if choice == '1':
        rmb = float(input("请输入人民币金额："))
        usd = currency_exchange.rmb_to_usd(rmb)
        print("兑换后的美元金额为：", usd)
    elif choice == '2':
        usd = float(input("请输入美元金额："))
        rmb = currency_exchange.usd_to_rmb(usd)
        print("兑换后的人民币金额为：", rmb)
    elif choice == '3':
        break
    else:
        print("输入错误，请重新输入。")
