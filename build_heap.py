import math
def build_heap(data):
    swaps = []
    for i in range(len(data)-1,-1,-1):
        child_index = i
        while(True):
            parent_index = math.ceil(child_index/2)-1               
            if data[child_index] < data[parent_index] and child_index!=0:
                kaste = data[child_index]
                data[child_index] = data[parent_index]
                data[parent_index] = kaste
                swaps.append(parent_index)
                swaps.append(child_index)
                child_index = parent_index
                    
            else:
                break

    return swaps

def main():
    input_method = input()
    
    if "I" in input_method:
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
        print (int(len(swaps)/2))
        for i in range(0,len(swaps),2):
            print (swaps[i] , swaps[i+1])

    elif "F" in input_method:
        file = input()
        file = ("tests/" + file)      
        with open(file,'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
            swaps = build_heap(data)
            print (int(len(swaps)/2))
            for i in range(0,len(swaps),2):
                print (swaps[i] , swaps[i+1])            
        f.close()
        
if __name__ == "__main__":
    main()
