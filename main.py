# Concrete SHear Strength
# From Table 19 - IS456:2000
# Design strength of concrete TAUc in N/mm-2
import numpy as np
import pandas as pd
from scipy.interpolate import interp2d


def shear_strength():
    df = pd.read_csv('shear.csv')
    df.index = [0, 0.15, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
    x = df.columns
    y = df.index
    z = df.values
    print(x)
    print(y)
    print(z)
    f = interp2d(x, y, z, kind='linear')
    grade = int(input("Enter grade of concrete:"))
    percent_steel = float(input("Enter percent steel:"))
    return f(grade, percent_steel)


print(shear_strength())
