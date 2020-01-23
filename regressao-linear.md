# Regressão Linear

```python
import pandas as pd
base = pd.read_csv('faturamento_cnae.csv')
x = base.iloc[:, 0].values
y = base.iloc[:, 1].values

import numpy as np
correlacao = np.corrcoef(x, y)
x = x.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x, y)
regressor.coef_
regressor.intercept_

import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.plot(x, regressor.predict(x), color = 'red')
plt.title('Regressão Linear')
plt.xlabel('Faturamento')
plt.ylabel('CNAE')
plt.show()

score = regressor.score(x,y)

from yellowbrick.regressor import ResidualsPlot
visualizador = ResidualsPlot(regressor)
visualizador.fit(x,y)
visualizador.poof()
```
