from sklearn.linear_model import *

treino_entrada = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
treino_classe = [0,1,1,1,1,1,1,1]
neuronio = Perceptron(max_iter=60, eta0=0.2,random_state=0)

neuronio.fit(treino_entrada,treino_classe)


print(neuronio.predict([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,1,1]]))

