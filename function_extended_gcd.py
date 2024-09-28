# 
def extended_gcd(a, b):
    """扩展欧几里得算法，计算 ax + by = gcd(a, b) 的整数解"""
    if b == 0:
        return a, 1, 0
    else:
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y
