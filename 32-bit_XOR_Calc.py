

def XOR_calc_32bit(num1, num2):

    def to_32bit_binary(n):
        # need to find the largest index, call it start, such that 2^(start)<n
        # since the list is sorted, we could implement an Interval Search algorithm (such as binary search)
        # however since len(arr) will always be 32, a linear search (time complexity O(n)) is suitable

        # output [0] represents the sign of the parsed integer, so if n is negative, output[0] shall be True (1)
        # else output[0] = False (0)

        output = [0] * 32
        # determine sign bit for input integer
        if n < 0:
            output[0] = 1
            m = abs(n)
        else:
            m=n

        # loop through output list to give n as binary - (this could be done using python's bin() function however:
        # 1) I wanted to keep the binary as a 32-bit number
        # 2) this allows for very quick element by element comparison for the XOR operation

        i = 1

        while i < len(output):
            two_power = (31 - i)
            if 2**two_power == m:
                output[i] = 1
                return output
            elif 2**two_power < m:
                output[i] = 1
                m -= 2**two_power
                i +=1
            else:
                i+=1
        return output

    arr1 = to_32bit_binary(num1)
    arr2 = to_32bit_binary(num2)
    output_base_10 = 0

    for el in range(0,32):

        two_power = (31 - el)

        #check sign bit to determine sign of return integer:
        if el == 0:
            if arr1[el] == 1 or arr2[el] == 1:
                arr1[el] = 1
        else:
            if arr1[el] == arr2[el]:
                arr1[el] = 0
            else:
                arr1[el] = 1
                output_base_10 += 2 ** two_power


    return output_base_10 if arr1[0] == 0 else -output_base_10
