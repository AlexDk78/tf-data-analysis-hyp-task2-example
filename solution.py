import pandas as pd
import numpy as np
from scipy import stats

chat_id = 897113152

def solution(x: np.array, y: np.array) -> bool:
    res = stats.cramervonmises_2samp(x, y)
    return res.pvalue < 0.08



