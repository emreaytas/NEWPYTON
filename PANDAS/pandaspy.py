import pandas as pd
import numpy as np

# path önemli çünkü okuma işlemine PYTHONDAN başladı bu yüzden PANDAS klasörüne girmek gerekti...
df = pd.read_csv("PANDAS/sample1.csv") # csv okumak için read_csv kullanırız...         
df1 = pd.read_json("PANDAS/sample.json") # json okumak için ise read_json kullanırız... eğer ezcelden okuma yapacaksak o zaman pd.read_excel kullanırız ama ayrı bir kütüphane lazım pip install xlrd ile bunu indirmemiz lazım eğer excelden veri okumak istersek...
# excelden veri okumak için ise read_excel kullanırız xlsx ise excel uzantısıdır...



print(df)
print(df1)


