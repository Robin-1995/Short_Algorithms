def closest_points(arr,k=1):

    #store each co-ordinate in a dict in format point:dist
    distance_store = {}

    if k == len(arr):
        return arr
    elif k == 0:
        return 0

    elif k <= len(arr)/2:
        temp_arr = [float("inf")] * k
        output_arr = []
        for point in arr:
            distance = (point[0]**2 + point[1]**2)**0.5
            distance_store[point] = distance

            #compare distance with max distance in the temp_array, if it's less then the max, replace max dist with
            #new dist
            if distance < max(temp_arr):
                temp_arr[temp_arr.index(max(temp_arr))] = distance

        for dist in temp_arr:
            for key, val in distance_store.items():
                if val == dist:
                    output_arr.append(key)
        return output_arr

    else:
        temp_arr = [float("-inf")] * (len(arr)-k)
        output_arr = [point for point in arr]
        for point in arr:
            distance = (point[0]**2 + point[1]**2)**0.5
            distance_store[point] = distance
            if distance > min(temp_arr):
                temp_arr[temp_arr.index(min(temp_arr))] = distance

        for dist in temp_arr:
            for key, val in distance_store.items():
                if val == dist:
                    output_arr.remove(key)

        return output_arr