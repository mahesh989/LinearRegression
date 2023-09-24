import numpy as np
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./README.md')



df.head()
df.duplicated().sum()
