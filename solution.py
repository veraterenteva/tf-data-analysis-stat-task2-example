import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 559507665 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    X_max = np.max(x)
    return X_max, (X_max - 0.092) / alpha ** (1 / len(x)) + 0.092
