alg1=['e','n','e','e','n']
alg2=['w','n','w','n','w','w','n']
def ex3(X):
    flag = True
    while flag:
        if ('w' in X) and ('e' in X):
            X.remove('w')  
            X.remove('e')
            flag = True
        
        if ('n' in X) and ('s' in X):
            X.remove('s')  
            X.remove('n')
            flag = True
        
        else : flag = False
    
    sX= set(X)  
    salg1 =set(alg1) 
    salg2 = set(alg2)
    if len((sX.union(salg1)  - sX.intersection(salg1))) == 0 or len((sX.union(salg2)  - sX.intersection(salg2))) == 0 : print("True")  
    else : print("False")  
