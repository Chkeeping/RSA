def mod_inverse(e, phi_n):
    """计算 e 在模 phi_n 下的乘法逆元，即找到 d，使得 e * d ≡ 1 (mod phi_n)"""
    gcd_val, x, y = extended_gcd(e, phi_n)
    if gcd_val != 1:
        # 如果 e 和 phi_n 不互质，则逆元不存在
        return None
    else:
        # 确保 d 是正数
        return x % phi_n
