from sklearn.linear_model import *

treino_entrada = [[1,1],[1,0],[0,1],[0,0]]
treino_classe = [1,1,1,0]
neuronio = Perceptron(max_iter=60, eta0=0.2,random_state=0)

neuronio.fit(treino_entrada,treino_classe)

res = neuronio.predict([[1,0]])
print(res)

