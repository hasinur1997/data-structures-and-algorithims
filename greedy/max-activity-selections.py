def get_activities(s, f):
    n = len(f)

    i = 0
    jobs = [[s[0], f[0]]]
    for j in range(1, n):
        if s[j] >= f[i]:
            jobs.append([s[j], f[j]])
            i = j

    return jobs

def get_max_activities(arr):
    arr.sort(key=lambda x: x[1])

    i = 0
    jobs = [arr[i]]

    for j in range(1, len(arr)):
        if arr[j][0] >= arr[i][1]:
            jobs.append(arr[j])
            i = j

    return jobs

if __name__ == "__main__":
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]

    selected_jobs = get_max_activities([[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]])

    print(selected_jobs)
