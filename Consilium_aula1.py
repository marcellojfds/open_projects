#!/usr/bin/env python
# coding: utf-8

# In[3]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# # Imports

# In[4]:


import pandas as pd     # Estrutura de dados
import numpy as np      # Calculos e testes lógicos
import scipy as sc      # Numpy mais poderosos (estatística)


# ### Variables

# In[5]:


X = 2           #integer
Y = 2.456        #float
Z = 'Consilium' #string
W = True        #boolean


# In[7]:


print(X)
print(Y)
print(Z)
print(W) # Python é case sensitive


# In[8]:


print(type(X))
print(type(Y))
print(type(Z))
print(type(W))


# ###### Podemos operar com alguns tipos de variáveis, por exemplo: 
# ### Numéricos

# In[9]:


var = X + Y
print(var)


# In[10]:


var = X + 4
print(var) ### Python sobrescreve variáveis


# In[11]:


print(5 + 10)
5+10


# In[12]:


print(10 - 5)
10 - 5


# In[13]:


print(3**2)
a = 3**3
print(a)
3**2


# In[14]:


print(100 / 5)
100 / 20


# In[15]:


from math import sqrt
sqrt(144)


# ### Strings

# In[17]:


print(Z)
print(Z + " 123")


# In[18]:


var = (Z + " 2019")
print(var)


# In[21]:


var = 40
print("Eu tenho " + str(var)+ " anos")


# In[22]:


long_str = '''sentenças mais longas
podem ser escritas usando 3 quote marks'''
print(long_str)


split_line_str = "também posso usar double quotes ese minha frase estiver ficando longa, uso uma barra"
print(split_line_str)


# ### Booleans

# In[23]:


print(2 > 3)
print(3 > 2)
#print(2 > Z) #ops


# In[24]:


a = 'Alemanha'
b = 'Belgica'


# In[25]:


print(a < b)
print(a > b)

# Op. lógicos com strings apelam para a ordem alfabética


# #### Estrutura de Dados

# ###### Listas: Uma lista é um vetor que pode conter variáveis de qualquer formato

# In[40]:


lista = [2, 3.45, "Henrique Dau", True] # uma lista aceita diversos formatos

print(lista)

print(type(lista))

len(lista)


# In[29]:


# Agregar dados a uma lista
lista.append(10) 
lista


# In[30]:


# Remover dados de uma lista
lista.remove(3.45)
lista


# In[36]:


range(0,100)


# In[33]:


lista4 = list(range(0,100, 2)) # list e range formam um intervalo extensivo
print(lista4)

range(1,100) #apenas range apresenta o resultado resumido (python 3.x)


# In[ ]:


# Conditional Removing
lista4.remove(if lista4 > 36).print()  ####### melhorar


# In[44]:


ll = ("100.456")
ll2 = list(ll)
print(ll)
print(ll2)


# In[41]:


print(lista[2]) #acessar posições dentro da lista
print(lista[0]) ### Contagem no Python começa em 0, sendo que o final de um intervalo de lista é não inclusivo


# In[45]:


# acessar intervalos
lista2 = lista[0:3] 
lista2


# In[46]:


#podemos acessar também o final de uma lista
lista2 = lista[-2:] #intervalo aberto
print(lista2)


lista2 = lista[-2:-1] #intervalo fechado
print(lista2)


# In[47]:


### podemos agregar duas listas também
list1 = [1,2,3]
list2 = [4,5,6]

list1 + list2


# In[49]:


[list1, list2] # ou criar listas de listas


# e tambem, podemos checar o tamanho de uma lista
len(list2)


# #### Print como organizador

# In[50]:


# usando print para resutlados
comprimento = 1.10
largura  = 2.20
area   = comprimento * largura
print ("Essa area é: " , area)


# ## Loops

# Loop é uma estrutura lógica que permite realizarmos tarefas repetitivas, sem precisar inputar manualmente o código

# In[51]:


intervalo = range(1, 100)


# In[52]:


x = []
for i in intervalo:
    a = 2**i
    x.append(a)

x


# ## Body Mass Index

# In[56]:


a = []                               #Fernão
pesos = [75, 50, 56, 82, 40, 65, 50, 60]

for i in pesos:
    b = i
    a.append(b)

avg = sum(a)/len(a)

print('A média de peso do Consilium é: ', avg)

# ---------------------------------------------------------
a = []
altura = [175, 170, 155, 190, 182, 153, 164, 180]

for i in altura:
    b = i
    a.append(b)

avg = sum(a)/len(a)

print('A média de altura do Consilium é: ', avg)

#---------------------------------------------------------
a = []
b = []
for i in altura:
    for j in pesos:
        x = j
        a.append(x)
    y = i
    b.append(i)

bmi = sum(a)/(sum(b)/100)**2
print('A média de body mass index do Consilium é: ', bmi)

#---------------------------------------------------------
if bmi < 10:
    print('Estamos magros')
elif bmi <= 25:
    print('Estamos no peso')
else:
    print('Estamos gordos')    


# # Pandas

# In[57]:


import pandas as pd # pd é o apelido padrão


# In[58]:


# Pandas tem uma serie de formatos
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s


# In[59]:


# tambem tem funções que ajudam na manipulação de dados
dates = pd.date_range('20190101', periods=6)
dates


# In[60]:


# podemos montar um DF de forma simples
df = pd.DataFrame(np.random.randn(6, 4),
                  index=dates, columns=list('ABCD'))
df


# In[64]:


# ou mais elaborada
dates = pd.date_range('20190101', periods = 4)
df2 = pd.DataFrame({'A': 1.,
                     'B': dates,
                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D': np.array([3] * 4, dtype='int32'),
                     'E': pd.Categorical(["test", "train", "test", "train"]),
                     'F': 'foo'})
df2


# In[67]:


# Também é util
df2.head(2)
df2.tail(2)


# In[71]:


# Agora com um df bem grande
rows = 1000000 
columns = 4

df = pd.DataFrame(np.random.randn(rows, columns), columns=list('ABCD'))
df.head()


# In[75]:


# Hard way (customizable)

print(df['A'].mean())
print(df['A'].median())
print(df['A'].var())
print(df['A'].std())


summary = {'idx': ['mean', 'median','var', 'std'],
           'A': [df['A'].mean(), df['A'].median(), df['A'].var(), df['A'].std()],
           'B': [df['B'].mean(), df['B'].median(), df['B'].var(), df['B'].std()],
           'C': [df['C'].mean(), df['C'].median(), df['C'].var(), df['C'].std()],
           'D': [df['D'].mean(), df['D'].median(), df['D'].var(), df['D'].std()],
           }    
summary = pd.DataFrame(data=summary)

print(summary)


# In[74]:


# Easy way
df.describe()


# In[78]:


# acessando valores
df['A'] # <--- jeito "correto"
df.A  #<---- jeito "plebe"


# In[80]:


df[100:150]


# In[81]:


# recortando

df[df.A > 0]


# In[83]:


# multicriterio unilateral

df[(df.A < 0) | (df.B > 0)]


# In[84]:


# varios criterios
# regra de bolso (se voce esta usando .loc ou .iloc, alguma coisa de errado esta fazendo)
## linhas 3 e 4 e colunas 1 e 2

df.iloc[3:5, 0:2]


# In[87]:


import datetime as dt


# In[93]:


hour = dt.datetime.utcnow()

x = range(1,10000)
print(list(x))
timeA = dt.datetime.utcnow() - hour
print('exec ', str(timeA))


hour = dt.datetime.utcnow()

x = range(1,10000)
for i in x:
    print(i)
timeB = dt.datetime.utcnow() - hour
print('exec ', str(timeB))


pc = timeB/timeA
print('Method A was', str(pc), '% faster')


# In[ ]:





# ### Regression

# In[ ]:


import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:

