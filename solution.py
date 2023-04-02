import pandas as pd
import numpy as np
from scipy.stats import lognorm
from scipy.optimize import minimize_scalar


chat_id = 385459798 # Ваш chat ID, не меняйте название переменной


    
def solution(x: np.array) -> float:
    x = np.array([v - 855 for v in x])
    print(x)
    s, loc, scale = lognorm.fit(x)
    return loc;
