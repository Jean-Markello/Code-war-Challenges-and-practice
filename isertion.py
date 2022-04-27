from copy import *
def insertion_sort(list):
    for i in range(1, len(list)):
        j=i
        while list[j-1]>list[j] and j>0:
            list[j-1], list[j]= list[j], list[j-1]
            j-=1

def merge_sort(list):
    if len(list)>1:
        list_left=list[:len(list)//2]
        list_right=list[len(list)//2:]

        #recursion:
        merge_sort(list_left)
        merge_sort(list_right)
        
        #merge
        i,j,k=0,0,0
        while i<len(list_left) and j<len(list_right):
            if list_left[i] < list_right[j]:
                list[k]=list_left[i]
                i+=1
            else:
                list[k]=list_right[j]
                j+=1
            k+=1
        
        while i<len(list_left):
            list[k]=list_left[i]
            i+=1
            k+=1
        
        while j<len(list_right):
            list[k]=list_right[j]
            j+=1
            k+=1

def selection_sort(list):
    for i in range(0, len(list)-1):
        min_index=i
        for j in range(i+1, len(list)):
            if list[j]<list[min_index]:
                min_index=j
        
        list[i], list[min_index]=list[min_index],list[i] #swap



list=[2,-1,4,6,33,6,57,2,-2,-5,-33,-54,-2, 4,3,6,]
list2=copy(list)
list3=copy(list)
merge_sort(list)
insertion_sort(list2)
selection_sort(list3)
print(list)
print(list2)
print(list3)