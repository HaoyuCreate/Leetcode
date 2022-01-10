def BinarySearch(input_list, target: int)-> int:
    input_list.sort()

    low = 0
    high = len(input_list)-1

    while low<=high:
        mid = low + int(0.5 * (high-low) )
        if input_list[mid]<target:
            low = mid+1
        elif input_list[mid]>target:
            high = mid-1
        else:
            return mid
    else:
        return None

def InsertSearch(input_list,target):
    input_list.sort()

    low = 0
    high = len(input_list) - 1
    while low<=high:
        mid = low + int((target-input_list[low])/(input_list[high]-input_list[low])*(high-low))
        if input_list[mid] < target:
            low = mid + 1
        elif input_list[mid] > target:
            high = mid -1
        else:
            return mid
    else:
        return None


input_list=[2,5,7,9,10,13,24,25]
target = 1
print(BinarySearch(input_list,target))
print(InsertSearch(input_list,target))