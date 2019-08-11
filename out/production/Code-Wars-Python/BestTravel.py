import itertools

# t = max sum of distances
# k = number of towns to visit
# ls = list of distances between towns
def choose_best_sum(t, k, ls):
    # Create list with all permutations of k towns
    # sort ls from highest to lowest
    # start creating combinations until it is lower
    # than t

    # need to calculate how many combinations are possible
    # before the for loop
    combinations = list(itertools.combinations(ls, k))
    #print(combinations)
    sum = 0;
    sumList = []
    # TODO Try to do this in Comprehension lists
    for i in range(len(combinations)):
        sum = 0
        # calculate sums for all combinations
        for j in range(len(combinations[i])):
            sum =+ sum + combinations[i][j]
        # only append if needed to save memory
        if sum <= t:
            sumList.append(sum)
    # reverse order of sumlist first index should be our answer
    sumList.sort(reverse=True)

    # unless of course is empty then it means all sums were greater
    if not sumList:
        return None
    else:
        return sumList[0]

