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