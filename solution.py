import pandas as pd
import numpy as np
from scipy.stats import lognorm
from scipy.optimize import minimize_scalar


chat_id = 385459798 # Ваш chat ID, не меняйте название переменной




def log_likelihood(a, x):
    sigma = np.sqrt(np.var(np.log(x)) + np.mean(np.log(x)) ** 2)
    return -np.sum(lognorm.logpdf(x, s=sigma, scale=np.exp(a)))

    
def solution(x: np.array) -> float:
    result = minimize_scalar(log_likelihood, args=(x,))
    return result.x
