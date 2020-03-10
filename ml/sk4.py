import pandas as pd
from sklearn import svm, model_selection

csv = pd.read_csv('data\\iris.csv')
data = csv[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']]
label = csv['Species']
model = svm.SVC()
scores = model_selection.cross_val_score(model, data, label, cv=5)
print(scores)