def is_possible_last_index(jumps):
    last_index = len(jumps) - 1
    next_step = 0

    for i in range(len(jumps)-2, -1, -1):
        next_step = jumps[i] + i

        if next_step >= last_index:
            last_index = i

    return last_index == 0

jumps = [ 3,2,1,0,4 ];
print(is_possible_last_index(jumps))