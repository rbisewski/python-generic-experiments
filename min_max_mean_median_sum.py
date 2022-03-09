def min(alist):
    smallest = alist[0]
    for l in alist:
        if l < smallest:
            smallest = l

    return smallest

def max(alist):
    largest = alist[0]
    for l in alist:
        if l > largest:
            largest = l

    return largest

def mean(alist):
    size = len(alist)
    total = 0
    for l in alist:
        total += l

    return total/size

def median(alist):
    alist.sort()
    mid = len(alist) // 2
    median_res = (alist[mid] + alist[~mid]) / 2
    return median_res

def sum(alist):
    total = 0
    for l in alist:
        total += l

    return total

def main():
    alist = [1,2,3,4,5,6,8,9]

    x = min(alist)
    print("The min is:")
    print(x)

    y = max(alist)
    print("The max is:")
    print(y)

    z = mean(alist)
    print("The mean is:")
    print(z)

    a = median(alist)
    print("The median is:")
    print(a)

    b = sum(alist)
    print("The sum is:")
    print(b)

#------
main()