lst = [0, 5, 2, 7, 0, 9, 8, 0]
non_zero = [x for x in lst if x != 0]
result = non_zero + [0] * (len(lst) - len(non_zero))
print(result)
