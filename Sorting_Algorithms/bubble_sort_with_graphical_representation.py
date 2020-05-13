def bubble_sort(arr):

    import matplotlib.pyplot as plt


    fig = plt.figure()
    #creating a subplot
    ax1 = fig.add_axes([1,1,1,1])

    def update_plot(arr):

        xaxis = [x for x in range(0,len(arr))]
        plt.bar(xaxis, height=arr)

        plt.xlabel("Position")
        plt.ylabel("Value")
        plt.title("Animation of Bubble Sort")
        plt.show()



    in_order = False
    while in_order == False:
        num_swaps = 0
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                num_swaps+=1
                update_plot(arr)


        if num_swaps == 0:
            in_order = True

    return arr



x = [1,1,2,3,4,5,1,12,3,5,67,8,5,4,1,23,4,43,21,4,5]
print(bubble_sort(x))
