import numpy as np
from math import ceil
def get_val(x):
    return (ord(x)-97)%26
def hill_cipher(key,text,garbage="x"):
    text=text.lower()
    l1=len(text)
    l2=len(key)
    a=ceil(l1/l2)
    text+=garbage*(l2*a-l1)
    key=np.array(key)
    A=[]
    for i in range(a):
        A.append(list(text[i*l2:(i+1)*l2]))
    for i in range(len(A)):
        for j in range(l2):
            A[i][j]=get_val(A[i][j])
    #print(A)
    enc=[]
    for i in A:
        ins=np.array(i)
        #ins.resize((l2,1))
        #print(ins)
        enc.append([x%26 for x in list(key@i)])
    #print(enc)
    enc_text=""
    for i in enc:
        for j in i:
            enc_text+=chr(97+j)
    return enc_text



    
    
#key=[[17,17,5],[21,18,21],[2,2,19]]
#text="payment"
#garbage="x"
n=int(input("Enter size of key "))
key=[[int(j) for j in input().split()] for i in range(n)]
text=input("Enter text to be encoded ")
enc=hill_cipher(key,text)
print("Encoded text ",enc[:len(text)].upper())

