import numpy as pd
import pandas as pd 
from graphviz import Digraph
dot = Digraph()
a=pd.read_csv('box_macaco (4).csv')
lista= []
import numpy as np
with open('box_macaco (4).csv') as data_file:
      for line in data_file:
         lista.append(line.strip().split(','))

def comp_terminal(val):
    if val=="corpo":
        return 1
    if val=="llai":
        return 2
    if val=="llaf":
        return 3
    if val=="llaf":
        return 4
    if val=="pari":
        return 5
    if val=="parf":
        return 6
    if val=="ler":
        return 7
    if val=="mostre":
        return 8
    if val=="corr":
        return 9
    if val=="id":
        return 10
    if val=="may":
        return 11
    if val=="men":
        return 12
    if val=="maye":
        return 13
    if val=="mene":
        return 14
    if val=="dif":
        return 15
    if val=="simi":
        return 16
    if val=="sin":
        return 17
    if val=="senao":
        return 18
    if val=="senaosin":
        return 19    
    if val=="enquanto":
        return 20
    if val=="intei":
        return 21
    if val=="dupla":
        return 22
    if val=="val":
        return 23
    if val=="corrente":
        return 24
    if val=="binar":
        return 25
    if val=="equal":
        return 26
    if val=="num":
        return 27
    if val=="soma":
        return 28
    if val=="sub":
        return 29
    if val=="multi":
        return 30
    if val=="div":
        return 31
    if val=="$":
        return 32
    else:
        return 0

def comp_noterminal(stra):
    if stra=="CORPO":
        return 1
    if stra=="LEC":
        return 2
    if stra=="LEC_S":
        return 3
    if stra=="MOST":
        return 4
    if stra=="CON":
        return 5
    if stra=="CON_S":
        return 6
    if stra=="CONT":
        return 7
    if stra=="TYPE_CON":
        return 8
    if stra=="VAL":
        return 9
    if stra=="VAL_S":
        return 10
    if stra=="TYPE":
        return 11
    if stra=="ASI":
        return 12
    if stra=="ASI_S":
        return 13
    if stra=="E":
        return 14
    if stra=="E'":
        return 15
    if stra=="T":
        return 16
    if stra=="FN":
        return 17
    if stra=="SIM":
        return 18
    else:
        return 0
cadena = "corpo llai dupla id equal num llaf"
cadena = cadena.split(' ')
cadena.append("$")
tam = len(cadena)
action=[]
stack = ["CORPO","$"]
continuar=True
aux1=0
aux2=0
aux=[]
dot.node(str(aux1), stack[0])
padres=[0,-1]
print(stack)
print(cadena)
while continuar:
  if stack[0]=="$" and cadena[0]=="$":
    continuar=False
    print(stack)
    print(cadena)
  elif stack[0] == cadena[0]:
    print(stack)
    print(cadena)
    stack = stack[1:]
    cadena.pop(0)
  elif stack[0][0]==(stack[0][0]).lower() and cadena[0]==(cadena[0]).lower():
    continuar=False
    print(stack)
    print(cadena)
  else:
    if comp_terminal(cadena[0])!=0:
        reemplazo = lista[comp_noterminal(stack[0])][comp_terminal(cadena[0])]
        aux2=int(padres[0])
    else:
      continuar=False
      print(stack)
      print(cadena)
      break
    array_aux=reemplazo.split()
    stack = np.concatenate((array_aux,stack[1:]),axis=0)
    hijos = len(array_aux)
    aux.clear()
    for e in range(hijos):
      aux1=aux1+1
      if array_aux[e][0]==array_aux[e][0].upper():
        aux.append(aux1)
      aux3=aux1
      dot.node(str(aux3), array_aux[e])
      dot.edge(str(aux2),str(aux3))
    padres = np.concatenate((aux,padres[1:]),axis=0)
    print(stack)
    print(cadena)
print(dot.source)
