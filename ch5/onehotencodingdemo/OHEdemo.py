import pandas as pd
from sklearn.feature_extraction import DictVectorizer


df = pd.DataFrame([['rick','young'],['phil','old']],columns=['name','age-group'])
print(df)
print("\n----By using Panda ----\n")
print(pd.get_dummies(df))

X = pd.DataFrame({'income': [100000,110000,90000,30000,14000,50000],
                  'country':['US', 'CAN', 'US', 'CAN', 'MEX', 'US'],
                  'race':['White', 'Black', 'Latino', 'White', 'White', 'Black']})



print("\n----By using Sikit-learn ----\n")
v = DictVectorizer()
qualitative_features = ['country']
X_qual = v.fit_transform(X[qualitative_features].to_dict('records'))
print(v.vocabulary_)
print(X_qual.toarray())