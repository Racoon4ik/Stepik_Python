def listmax(list):
    max = list[0]
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]

    return max

print(listmax(input().split(",")))