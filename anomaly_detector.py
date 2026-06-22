from sklearn.ensemble import IsolationForest
import pandas as pd

data=pd.DataFrame({

'seconds':[0,1,2,3,4,100]

})

model=IsolationForest()

model.fit(data)

prediction=model.predict(data)

print(prediction)