from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def XOR(x1, x2):
    """
    ゲートを組み合わせる
    """
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)

    return y