import time

numbers=list(range(1,1_000_001))
target=999_999

def linear_search(lst,target):
    for i in range(len(lst)):
        if lst[i]==target:
            return lst[i]
    return -1
start=time.time()
index=linear_search(numbers,target)
end=time.time()

print(f"Grammikh anazhthsh vrethike sth thesh {index} se {end-start:.5f} deuterolepta")

def binary_search(lst,target):
    left=0
    right=len(lst) -1
    while left<=right:
        mid=(left+right)//2
        if lst[mid]==target:
            return mid  
        elif lst[mid] < target:
            left=mid+1
        else:
            right=mid-1
    return -1

start=time.time()
index=binary_search(numbers,target)
end=time.time()

print(f"Diadikh anazhthsh vrethike sth thesh {index} se {end-start:.5f} deuterolepta")