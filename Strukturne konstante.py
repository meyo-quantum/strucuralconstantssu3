import numpy as np

G1 = 1/2*np.array([[0,complex(1,0),0],[1,0,0],[0,0,0]])
G2 = 1/2*np.array([[0,complex(0,-1),0],[complex(0,1),0,0],[0,0,0]])
G3 = 1/2*np.array([[1,0,0],[0,-1,0],[0,0,0]])
G4 = 1/2*np.array([[0,0,1],[0,0,0],[1,0,0]])
G5 = 1/2*np.array([[0,0,complex(0,-1)],[0,0,0],[complex(0,1),0,0]])
G6 = 1/2*np.array([[0,0,0],[0,0,1],[0,1,0]])
G7 = 1/2*np.array([[0,0,0],[0,0,complex(0,-1)],[0,complex(0,1),0]])
G8 = np.array([[1,0,0],[0,1,0],[0,0,-2]])/np.sqrt(3)/2

G = [G1,G2,G3,G4,G5,G6,G7,G8]

def komutator(x,y):
    return np.dot(x,y)-np.dot(y,x)

f=np.zeros((8,8,8),dtype='complex_')

for i in range(8):
    for j in range(8):
        A = komutator(G[i], G[j])
        #print(A)
        for k in range(8):
            B = G[k]
            for l in range(3):
                for m in range(3):
                    if B[l,m]!=0 and A[l,m]!=0:
                        c=A[l,m]/B[l,m]
                        f[i,j,k]=c/complex(0,1)
                        break
                    else:
                        continue
            
for i in range(8):
    for j in range(8):
        for k in range(8):
            if i==j or i==k or k==j:
                f[i,j,k]=0
            elif np.abs(f[i,j,k])>1:
                f[i,j,k]=0
            elif f[i,j,k].imag!=0:
                f[i,j,k]=0
            else:
                continue
            

for i in range(8):
    for j in range(8):
        for k in range(8):
            if f[i,j,k]!=0:
                print('Strukturna konstanta f{',i+1,j+1,k+1,'}: ',f[i,j,k].real)

#da bi uštedili prostora, napisat ćemo samo one koje nisu nule :) 
print('Ostale strukurne konstante su jednake nuli!')




                        
                        