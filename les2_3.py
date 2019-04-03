my_list_1 = [2, 2, 5, 12, 8, 2, 12]
result = []
for i in my_list_1:
    if not (my_list_1.count(i) > 1):
        result.append(i)
print(result)