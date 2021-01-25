import numpy as np
import pandas as pd

#TOPSIS
def Topsis(A1):
    W0=[0.1,0.5,0.2,0.2] #weight matrix 0.1+0.5+0.2+0.2=1
    #tip:the first column is the "name",so weight 0.2 multiply to the second column "x1" and so on 
    W=np.ones([A1.shape[1],A1.shape[1]],float)
    for i in range(len(W)):
        for j in range(len(W)):
            if i==j:
                W[i,j]=W0[j]
            else:
                W[i,j]=0
    Z=np.ones([A1.shape[0],A1.shape[1]],float)
    Z=np.dot(A1,W) #weighting matrix
    
    #Calculate positive and negative ideal solutions
    Zmax=np.ones([1,A1.shape[1]],float)
    Zmin=np.ones([1,A1.shape[1]],float)
    for j in range(A1.shape[1]):
        if j==3:
            Zmax[0,j]=min(Z[:,j])
            Zmin[0,j]=max(Z[:,j])
        else:
            Zmax[0,j]=max(Z[:,j])
            Zmin[0,j]=min(Z[:,j])

    #Calculate the relative closeness degree C of each scheme
    C=[]  
    for i in range(A1.shape[0]):
            Smax=np.sqrt(np.sum(np.square(Z[i,:]-Zmax[0,:])))
            Smin=np.sqrt(np.sum(np.square(Z[i,:]-Zmin[0,:])))
            C.append(Smin/(Smax+Smin))
    C=pd.DataFrame(C,index=['name' + i for i in list('abcde')])   
    return C

#Standardized treatment
def standard(A):
    #Effectiveness indicators
    A1=np.ones([A.shape[0],A.shape[1]],float)
    for i in range(A.shape[1]):#i represents the number of the column，0 indicates "x1"
        if i==0 or i==2:
            if max(A[:,i])==min(A[:,i]):
                A1[:,i]=1
            else:
                for j in range(A.shape[0]):
                    A1[j,i]=(A[j,i]-min(A[:,i]))/(max(A[:,i])-min(A[:,i]))
    
    #Cost type indicators
        elif i==3:
            if max(A[:,i])==min(A[:,i]):
                A1[:,i]=1
            else:
                for j in range(A.shape[0]):
                    A1[j,i]=(max(A[:,i])-A[j,i])/(max(A[:,i])-min(A[:,i])) 

    #Interval type indicators
        else:
            a,b,lb,ub=5,6,2,12#Let the index value in the interval [a,b] be the best
            #The worst lower limit is lb, the worst upper limit is ub.
            for j in range(A.shape[0]):
                if lb <= A[j,i] < a:
                    A1[j,i]=(A[j,i]-lb)/(a-lb)
                elif a <= A[j,i] < b:
                    A1[j,i]=1		
                elif b <= A[j,i] <= ub:
                    A1[j,i]=(ub-A[j,i])/(ub-b)
                else:  #A[i,:]< lb or A[i,:]>ub
                    A1[j,i]=0	
    return A1

#Read and compute the initial matrix
def data(file_path):
    data=pd.read_excel(file_path).values
    A=data[:,1:]#Begin to calculate from the second column "x1"
    A=np.array(A)
    return A

#weight
A=data('topsis.xlsx')#The path and the name of the file
A1=standard(A)
C=Topsis(A1)
print(C)
