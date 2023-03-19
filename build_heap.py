# python3
# Darja Ševcova 221RDC039
import os

def sift_down (data, i, swaps):
    size = len(data)
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < size and data[left_child] < data[min_index]:
        left_child = min_index
    if right_child< size and data[rigth_child] < data[min_index]:
        rigth_child = min_index
    if min_index != i:
        swaps.append(i, min_index))
        data[min_index], data[i] = data[i], data[min_index]
        sift_down(data, min_index, swaps)
        
def build_heap(data):
    swaps = []
    for i in range(len(data)//2, -1, -1):
        sift_down(data, i, swaps)
    return swaps
    
def main():
    text = input("Enter the letter 'I' or 'F'")
    if "I" in text:
    #input from keyboard
        n = int(input("Enter a number n: ")
        data = list(map(int, input("Enter the number of spaces: ").split()))
    #check if length of data is the same as the said length
        assert len(data) == n
        
    elif "F" in text:
        filename = input("Enter the file name: ")
        path = './test/'
        file_path = of.path.join(path, filename)
        with open(file_path
            n = int(file.readline())
            data =list(map(int, file.readline().split()))
            
     else:
        print("Enter the letter 'I' or 'F'")
        return
        
     #give bak all swaps
     swaps = build_heap(data)
     
     #output all swaps
     print(len(swaps))
     for i, j in swaps:
        print(i, j)
        
if __name__ == '__main__';
    main()
