input = [s for s in open("input.txt").read().split('\n') if s]


def isRangeWithin(arr1,arr2):
    x1, x2 = int(arr1[0]), int(arr1[1])
    y1, y2 = int(arr2[0]), int(arr2[1])

    return ((x1 >= y1 and x2 <= y2) or (y1 >= x1 and y2 <= x2))

count = 0
fullyContainedCount = 0
nonOverlapCount = 0

for i in range(len(input)):
    pair = input[i]
    print(pair)
    arr1, arr2 = pair.split(",")[0].split("-"), pair.split(",")[1].split("-")
    print(arr1, arr2)

    set_1 = set(range(int(arr1[0]), int(arr1[1])+1))
    set_2 = set(range(int(arr2[0]), int(arr2[1])+1))

    if set_1.issubset(set_2) or set_2.issubset(set_1):
        fullyContainedCount += 1

    # no elements in common
    if set_1.isdisjoint(set_2):
        nonOverlapCount += 1

    if(isRangeWithin(arr1, arr2)):
        count+=1


print(len(input))
print(count)
print(fullyContainedCount)
print(len(input) - nonOverlapCount)

