def solution(list_of_nums):
    dic = dict()
    count_even,count_odd = 0, 0
    for i in list_of_nums:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    dic['ODD'] = count_odd
    dic['EVEN'] = count_even
    return dic

l = [1, 2, 3, 5, 8, 9]
print solution(l)
