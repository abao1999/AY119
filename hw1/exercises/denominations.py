def countDenomsSplits(denoms, target):
    splits = [0] * (target + 1)
    splits[0] = 1
    for d in denoms:
        for i in range(d, target+1):
            splits[i] += splits[i - d]
    return splits[target]

if __name__ == "__main__":
    denoms = [1,5,10,25]
    target = 100
    print("denominations: ", denoms)
    print("target: ", target)
    print("ways to split: ", countDenomsSplits(denoms, target))

    sum_1_100_odd = 0
    for i in range(1, 101):
        num_splits = countDenomsSplits(denoms, i)
        if num_splits % 2 == 1:
            sum_1_100_odd += num_splits
    print("The sum of the number of odd number splits for 1 through 100: ", sum_1_100_odd)
    if sum_1_100_odd%2 == 0:
        print("... which is even")
    else:
        print("... which is odd")
