
# selection sort

list1 = []
x = int(input('enter the length of the list : '))
for i in range(x):
    val = int(input('enter the values : '))
    list1.append(val)
print(f'list before sorting : {list1}')
for i in range(len(list1) - 1):
    minval = i
    for j in range(i, len(list1)):
        if list1[j] < list1[minval]:
            minval = j
    temp = list1[i]
    list1[i] = list1[minval]
    list1[minval] = temp

print(f"the sorted list is : {list1}")



# bubble sort
list1=[]
x=int(input('enter the length of list1; '))
for i in range(x):
    val=int(input('enter the values in list1: '))
    list1.append(val)
for i in range(len(list1)-1):
    if list1[i]>list1[i+1]:
        list1[i],list1[i+1]=list1[i+1],list1[i]

    else:
        pass
    for j in range(i):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]

        else:
            pass
print(f'the sorted list is : {list1}')



# insertion sort
list1=[]
x=int(input('enter the lenght of list: '))
for i in range(x):
    val=int(input('enter the values in the list : '))
    list1.append(val)
print(f'list before sorting : {list1}')
for i in range(1,len(list1)):
    temp=list1[i]
    n=i
    while temp<list1[n-1]and n>0:
        list1[n]=list1[n-1]
        n=n-1

    list1[n]=temp

print(f'list after sorting : {list1}')


# shell sort
def shellSort(list1):
    gap=len(list1)//2
    while gap>0:
        for j in range(gap ,len(list1)):
            current_element=list1[j]
            position=j
            while position>=gap and current_element<list1[position-gap]:
                list1[position]=list1[position-gap]
                position=position-gap
            list1[position]=current_element
        gap=gap//2
    return list1
x=int (input('enter the lenth of the list : '))
list1=[int(input("enter the numbers in the list : ")) for i in range(x)]
print(shellSort(list1))








 quick sort

def _pivote(list1,first,last):
    pivote=list1[first]
    left=first+1
    right=last
    while True:
        while left<=right and list1[left]<=pivote:
            left+=1
        while left<=right and list1[right]>=pivote:
            right-=1
        if left>right:
            break
        else:
            list1[right],list1[left]=list1[left],list1[right]
    list1[first], list1[right] = list1[right], list1[first]
    return right

def qwicksort(list1,first,last):
    if first<last:
        p=_pivote(list1,first,last)
        qwicksort(list1,first,p-1)
        qwicksort(list1,p+1,last)

x=int(input("enter the length of the list : "))
list1=[int(input("enter the element in the list :"))]
n=len(list1)
qwicksort(list1,0,n-1)
print(list1)




# merge sort

def mergesort(myList):
    if 1<len(myList):
        mid=len(myList)//2
        left=myList[:mid]
        right=myList[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                myList[k]=left[i]
                i+=1
            else:
                myList[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            myList[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            myList[k]=right[j]
            j+=1
            k+=1
x=int(input("enter the length of the list : "))
myList = [int (input("enter the element in the list : ")) for i in range(x)]
mergesort(myList)
print(myList)
