import numpy as np
import pandas as pd

data = {
    'X':[10,20,30,40,50],
    'Y':[15,25,35,45,55]
}

df=pd.DataFrame(data)
print('Data Set')
print('-----------')
print(df)


cov_xy=np.cov(df['X'],df['Y'])[0,1]
print('\n Convirnce between X and Y =',cov_xy)

corr_xy=np.corrcoef(df['X'],df['Y'])[0,1]
print('correlation between x and y=',corr_xy)

cov_matrix=df.cov()
print('\n corariance matrix:')
print(cov_matrix);

Data Set
-----------
    X   Y
0  10  15
1  20  25
2  30  35
3  40  45
4  50  55

 Convirnce between X and Y = 250.0

 correlation between x and y= 1.0

 corariance matrix:
       X      Y
X  250.0  250.0
Y  250.0  250.0