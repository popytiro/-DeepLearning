import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7 # 10のマイナス7乗
    return -np.sun(t * np.log(y + delta)) 
    """
    np.log(0)はマイナスの無限大を表す-infとなり計算が止まる。
    その防止策として微小な値を追加して、マイナス無限大を発生させないようにしている。
    """

t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

cross_entropy_error(np.array(y), np.array(t))