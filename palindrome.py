def largest(min_factor, max_factor):
    lists = sorted(list())
    for i in range(min_factor, max_factor + 1):
        for num in range(min_factor, max_factor + 1):
            string = str(i*num)
            if string == string[::-1]:
                lists.append(i*num)
    factors = []
    for i in range(1, int(lists[-1]**0.5)+1):
        if lists[-1] % i == 0:
            factors.append((i, int(lists[-1] / i)))
    return (lists[0], factors[-1])
    
print(largest(10, 99))

def smallest(min_factor, max_factor):
    lists = sorted(list())
    for i in range(min_factor, max_factor + 1):
       for num in range(min_factor, max_factor + 1):
            string = str(i*num)
            if string[0] == string[-1]:
                lists.append(i*num)     
    factors = []
    for i in range(1, int(lists[0]**0.5)+1):
        if lists[0] % i == 0:
            factors.append((i, int(lists[0] / i)))
    return (lists[0], factors[-1])

print(smallest(1000, 9999))