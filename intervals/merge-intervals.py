def merge(intervals):
    results = []

    i = 0

    while i < len(intervals) - 1:
        if intervals[i][1] > intervals[i+1][0]:
            results.append([intervals[i][0], intervals[i+1][1]])
            i += 1
        else:
            i += 1
            results.append(intervals[i])

    return results


intervals = [[1,4],[4,5]]

print(merge(intervals))