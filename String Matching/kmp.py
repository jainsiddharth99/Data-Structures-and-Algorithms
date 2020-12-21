def kmp(T, P):
    n, m = len(T), len(P) 
    if m == 0: return 0 
    fail = compute_kmp_fail(P) 
    j = 0 
    k = 0 
    while j < n:
        if T[j] == P[k]: 
            if k == m-1: 
                return j-m + 1
            j += 1 
            k += 1
        elif k > 0:
                k = fail[k-1] 
        else:
            j += 1
    return -1 

def compute_kmp_fail(P):
    m = len(P)
    fail = [0]*m 
    j = 1
    k = 0
    while j < m: 
        if P[j] == P[k]: 
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else: 
            j += 1
    return fail

T=input('Text: ')
P=input('Pattern: ')
print(kmp(T,P))