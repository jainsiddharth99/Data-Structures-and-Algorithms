def merge(list1, list2):
    newList = []
    i = 0
    j = 0

    while len(list1) != 0 and len(list2) != 0:
        if list1[i] < list2[j]:
            newList.append(list1[i])
            list1.remove(list1[i])
        elif list1[i] > list2[j]:
            newList.append(list2[j])
            list2.remove(list2[j])

    if len(list1) == 0:
        newList += list2
    else:
        newList += list1

    return newList

def mergeSort(numList):
    if len(numList) == 0 or len(numList) == 1:
        return numList
    else:
        midpoint = int(len(numList)/2)
        left = mergeSort(numList[:midpoint])
        right = mergeSort(numList[midpoint:])
        return merge(left,right)

list=[10,30,70,40,20,50,60,90,100,80]
print(mergeSort(list))
