import math
import pandas as pd
import numpy as np
from scipy.stats import lognorm
from scipy.optimize import minimize_scalar
from scipy.optimize import minimize


chat_id = 385459798  # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    return np.log(x-855).mean()