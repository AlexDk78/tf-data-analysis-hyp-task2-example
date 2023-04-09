import pandas as pd
import numpy as np


chat_id = 897113152 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import ks_2samp
    _, p_value = ks_2samp(x, y)
    return p_value < 0.08
