def waitting_time(customers):
    finish_time = 0
    waitting_time = 0

    for customer in customers:
        if customer[0] > finish_time:
            finish_time = customer[0] + customer[1]
        else:
            finish_time += customer[1]

        waitting_time += finish_time - customer[0]


    avarage_time = waitting_time / len(customers)


    return avarage_time


customers = [[5,2],[5,4],[10,3],[20,1]]
result = waitting_time(customers)
print(result)