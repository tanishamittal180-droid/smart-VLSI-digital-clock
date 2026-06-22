import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {

'day':[1,2,3,4,5,6,7],
'wakeup_hour':[6,6,7,6,7,8,8],
'wakeup_min':[30,30,0,15,0,30,45]

}

df=pd.DataFrame(data)

X=df[['day']]
y=df['wakeup_hour']

model=DecisionTreeClassifier()

model.fit(X,y)

def predict_alarm(day):

    hour=model.predict([[day]])[0]

    return hour