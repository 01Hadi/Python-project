def EX3_2(X):
  """
  (list) -> int
  Alist of integers that return the largest product of adjacent numbers
  """
    maxx = []
    for i in range(0,len(X)-1):
        maxx.append(X[i]*X[i+1])
    
    print(max(maxx)) 
