def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    
    while(start<=end):
        print("Step", steps, ":" ,str(list[start:end+1]))
        steps = steps+1
        middle = (start + end) // 2
        
        if element == list[middle] :
            return middle
        if element < list[middle]:
            end = middle -1
        else:
            start = middle + 1

    return -1


my_list = list(map(int,input().split()))
target = int(input())
Ix=binary_search(my_list, target)
if Ix!=-1:
    print(f"Element encountered at the index {Ix}")
else:
    print(f"There is no such Element called {target} in the List") 
