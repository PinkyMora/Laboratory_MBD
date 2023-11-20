def merge_max_mappings(d1,d2):
    merged = d1.copy()

    for key in d2:
        if key not in merged or merged[key] < d2[key]:
            merged[key] = d2[key]

    return merged 


dict1 = {'bananas': 7, 'apples': 3, 'pears': 14}
dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}
print(merge_max_mappings(dict1,dict2))
