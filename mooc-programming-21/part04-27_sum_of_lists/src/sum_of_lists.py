# Write your solution here
def list_sum(list1, list2):
    list_add = []
    for i in range(len(list1)):
        add = list1[i] + list2[i]
        list_add.append(add)
    return list_add