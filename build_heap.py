# python3  
# Darja Ševcova 221RDC039  
import os

def build_heap(data):
    swaps = []
    for i in range(len(data)//2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down (i, data, swaps):
    size = len(data)
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < size and data[left_child] < data[min_index]:
        min_index = left_child 
    if right_child < size and data[right_child] < data[min_index]:
        min_index = right_child 
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index, data, swaps)
        return swaps
    
def main():
    text = input()
    if "I" in text:
    #input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    #check if length of data is the same as the said length
        assert len(data) == n
        
    elif "F" in text:
        filename = input()        
        path = './tests/'
        file_path = os.path.join(path, filename)
        with open(file_path, mode = "r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return    
    swaps = build_heap(data)
    
    assert len(swaps) <= 4*len(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)        
        
if __name__ == "__main__":
    main()
