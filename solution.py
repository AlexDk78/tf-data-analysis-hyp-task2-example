import pandas as pd
import numpy as np


chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    import numpy as np
    from scipy.stats import kstest
    alpha = 0.08
    stat, p_value = kstest(x, y)
    return p_value > alpha
