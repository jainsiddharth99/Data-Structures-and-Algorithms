def brute_force(T, P):
    l1 = len(T)
    l2 = len(P)
    i = 0
    j = 0
    flag = False
    while i<l1:
        j = 0
        count = 0
        while j<l2:
            if i+j < l1 and T[i+j] == P[j]:
                count += 1
            j += 1
            if count == l2:
                print("\nPattern occurs at index : {}".format(i))
                flag = True
        i += 1
    if not flag:
        print("\nPattern is not at all present in the array")

print('Text: ' )
T=input()
print('Pattern: ' )
P=input()
brute_force(T,P)