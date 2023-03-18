# python3


import math
def build_heap(data):
    swaps = []
    swaps = data
    for i in range(len(data)-1,-1,-1):
        if i%2 == 0:
            c = i
            while(True):
                parent_index = math.ceil(c/2)-1
                
                if data[c] < data[parent_index and c!=0]:
                    print (parent_index, " ", data[c], " " ,data[parent_index])
                    kaste = data[c]
                    data[c] = data[parent_index]
                    data[parent_index] = kaste
                    c = parent_index
                else:
                    break
        elif i%2 == 1:
            c = i

            while(True):
                parent_index = math.ceil(c/2)-1
                if data[c] < data[parent_index] and c!=0:
                    print (parent_index, " ", data[c], " " ,data[parent_index])
                    kaste = data[c]
                    data[c] = data[parent_index]
                    data[parent_index] = kaste
                    c = parent_index
                else:
                    break
        
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
 
   ## for i, j in swaps:
    ##    print(i, j)
    for i in range(len(swaps)):
        print (swaps[i])


if __name__ == "__main__":
    main()
