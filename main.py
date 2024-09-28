import random


def gcd(a, b):
    """计算两个数的最大公约数（递归实现）"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def extended_gcd(a, b):
    """扩展欧几里得算法，计算 ax + by = gcd(a, b) 的整数解"""
    if b == 0:
        return a, 1, 0
    else:
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y

def mod_inverse(e, phi_n):
    """计算 e 在模 phi_n 下的乘法逆元，即找到 d，使得 e * d ≡ 1 (mod phi_n)"""
    gcd_val, x, y = extended_gcd(e, phi_n)
    if gcd_val != 1:
        # 如果 e 和 phi_n 不互质，则逆元不存在
        return None
    else:
        # 确保 d 是正数
        return x % phi_n

def is_prime(num):
    """检查是否为质数"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


if __name__ == '__main__':
    p = int(input("请输入第一个质数 p: "))
    q = int(input("请输入第二个质数 q: "))

    # 检查输入的数字是否为质数
    if not is_prime(p) or not is_prime(q):
        print("输入的数必须是质数！")
        exit()
    # 计算 n 和 φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e_list = []
    e = 2
    while e < phi_n:
        if gcd(e, phi_n) == 1:
            e_list.append(e)
        e += 1
    print(e_list)
    choice_e = random.choice(e_list)
    print("随机选择的choice_e为： {}".format(choice_e))
    # 计算私钥指数 d
    d = mod_inverse(choice_e, phi_n)
    if d is None:
        print("无法找到 e 的模逆，选择不同的 e。")
        exit()

    # 输出计算结果
    print(f"计算得到的模数 n = {n}")
    print(f"选择的公钥指数 e = {choice_e}")
    print(f"计算得到的私钥指数 d = {d}")
