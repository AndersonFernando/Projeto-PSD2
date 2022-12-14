from datetime import datetime
antes = datetime.now()
print("Antes = ", antes)
#Matriz 1

arq = open('int.txt', 'r')  
texto = []  
matriz1 = [] 
texto = arq.readlines() 

for i in range(len(texto)):          
    matriz1.append(texto[i].split())

matriz1.pop(0) 
 
def getLinha(matriz, n):
    return [i for i in matriz[n]]  

def getColuna(matriz, n):
    return [i[n] for i in matriz]

mat1  = matriz1
mat1lin = len(matriz1)               
mat1col = len(matriz1[0]) 

for x in range (mat1lin):
   for y in range(mat1col):
    matriz1[x][y] = float(matriz1[x][y]) 

#Matriz 2

arq2 = open('10_int.txt', 'r')  
texto2 = []  
matriz2 = [] 
texto2 = arq2.readlines() 

for i in range(len(texto2)):          
    matriz2.append(texto2[i].split()) 

matriz2.pop(0)  

mat2 = matriz2
mat2lin = len(matriz2)               
mat2col = len(matriz2[0]) 

for x in range (mat2lin):
   for y in range(mat2col):
    #print(matriz1[x][z])
    matriz2[x][y] = float(matriz2[x][y]) 
           
matRes = []

for i in range(mat1lin):           
    matRes.append([])

    for j in range(mat2col):
        listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]
        matRes[i].append(sum(listMult))

print(matRes)
depois = datetime.now()
print("Depois = ", depois)
print(depois - antes)

with open('matrizes.txt', 'a') as arquivo:
    arquivo.write(str(matRes))


