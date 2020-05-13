def bubble_sort(arr):

    x = len(arr) - 1
    in_order = False
    while in_order == False:
        num_swaps = 0
        for i in range(0,x):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                num_swaps+=1
        if num_swaps == 0:
            in_order = True
    return arr

x = [5,6,7,4,1,2,5,76,1,2,45,4]
print(bubble_sort(x))
