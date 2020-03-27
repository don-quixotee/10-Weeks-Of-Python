def find_max(n,max_index):
    sorted_nums = sorted(set(n))
    return sorted_nums[-max_index]

num = [15,452,74,78,96,54,5,45]
print(find_max(num,2))