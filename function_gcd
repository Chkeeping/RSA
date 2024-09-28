# 这个函数 gcd(a, b) 用于 计算两个整数 a 和 b 的最大公约数（Greatest Common Divisor，GCD）。最大公约数是同时整除两个整数的最大整数。
# 两个整数 a 和 b（a > b），其最大公约数等于 b 和 a 除以 b 的余数 a % b 的最大公约数，
# gcd(a, b) = gcd(b, a % b)
# 由欧几里得算法原理计算得出两个数的最大公约数，该函数的作用用于判断后续e和r是否互素
def gcd(a, b):
    """计算两个数的最大公约数（递归实现）"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
