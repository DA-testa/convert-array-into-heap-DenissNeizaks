# python3


import math
def build_heap(data):
    swaps = []

    for i in range(len(data)-1,-1,-1):
        if i%2 == 0:
            c = i
            while(True):
                parent_index = math.ceil(c/2)-1
                
                if data[c] < data[parent_index and c!=0]:

                    kaste = data[c]
                    data[c] = data[parent_index]
                    data[parent_index] = kaste
                    swaps.append(parent_index)
                    swaps.append(c)
                    c = parent_index
                    
                else:
                    break
        elif i%2 == 1:
            c = i

            while(True):
                parent_index = math.ceil(c/2)-1
                if data[c] < data[parent_index] and c!=0:

                    kaste = data[c]
                    data[c] = data[parent_index]
                    data[parent_index] = kaste
                    swaps.append(parent_index)
                    swaps.append(c)
                    c = parent_index
                else:
                    break
        
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():

    input_method = input()
    
    if "I" in input_method:
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
        print (int(len(swaps)/2))
        for i in range(0,len(swaps),2):
            print (swaps[i] , " ", swaps[i+1])
    elif "F" in input_method:
        file = input()
        file = ("test/" + file)
        
        with open(file,'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
            swaps = build_heap(data)
            print (int(len(swaps)/2))
            for i in range(0,len(swaps),2):
                print (swaps[i] , " ", swaps[i+1])
            
        f.close()

    

if __name__ == "__main__":
    main()


