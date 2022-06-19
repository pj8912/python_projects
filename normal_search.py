#returns the index of the target

theList = [1,2,3,4,5]

def normal_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1



print(normal_search(theList, 4))

