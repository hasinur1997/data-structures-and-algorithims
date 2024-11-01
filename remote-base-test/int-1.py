def getMinMachines(start, end):
    counter = 1
    for i in range(len(start)):
        if end[i] > start[i]:
            counter += 1

    return counter



start = [1, 8, 3, 9, 6]
end = [7, 9, 6, 14, 7]

print(getMinMachines(start, end))