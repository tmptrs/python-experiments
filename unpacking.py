
lst = [1,2,3,4,5,6,7,8,9,10,4]

def relative_result_last(lst):
    *previous, last = lst
    avg_previous = sum(previous) / len(previous)
    return last - avg_previous

def unpack(x,y):
    print(x)
    print(y)