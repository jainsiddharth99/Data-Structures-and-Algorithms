def boyermoore(T, P):
    n, m = len(T), len(P)                  
    if m == 0: return 0                            
    last = {}                                      
    for k in range(m):
        last[P[k]] = k      
        
    i = m-1                                         
    k = m-1                                         
    while i < n:
        if T[i] == P[k]:                   
            if k == 0:
                return i                            
            else:
                i -= 1                              
                k -= 1                              
        else:
            j = last.get(T[i], -1)               
            i += m - min(k, j+1)                 
            k = m - 1                               
    return -1

T=input('Text: ')
P=input('Pattern: ')
print(boyermoore(T,P))