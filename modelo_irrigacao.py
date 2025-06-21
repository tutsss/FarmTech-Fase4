
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

dados = {'umidade': [20, 30, 45, 60, 25, 10, 80, 50, 33, 28, 70, 90], 'nutrientes': [25, 40, 60, 70, 20, 15, 80, 55, 30, 20, 75, 95], 'irrigar': [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]}

df = pd.DataFrame(dados)

X = df[['umidade', 'nutrientes']]
y = df['irrigar']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%")

joblib.dump(modelo, 'modelo_irrigacao.joblib')
