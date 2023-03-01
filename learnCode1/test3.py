def rmb_to_usd(amount):
    # 人民币转美元
    return amount * 0.1452


def usd_to_rmb(amount):
    # 美元转人民币
    return amount * 6.8833


# 测试
print(rmb_to_usd(100))  # 人民币100元转换成美元的金额
print(usd_to_rmb(10))  # 美元10元转换成人民币的金额
