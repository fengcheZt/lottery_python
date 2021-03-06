"""
    复式7，12个号码中6保5型旋转矩阵
"""
from get_the_num.main.getData import get_last_one_data
import itertools
def get_matrix_f7_12_6_5(selected_num_list=[]):
    matrix_list=[]
    selected_num_list.insert(0,-1)
    s_list =selected_num_list
    if len(s_list)==13:
        list01 = [s_list[1], s_list[2], s_list[3], s_list[4], s_list[5], s_list[6], s_list[12]]
        list02 = [s_list[1], s_list[2], s_list[3], s_list[5], s_list[6], s_list[7],s_list[11]]
        list03 = [s_list[1], s_list[2], s_list[4], s_list[5], s_list[7], s_list[11],s_list[12]]
        list04 = [s_list[1], s_list[2], s_list[4], s_list[8], s_list[10], s_list[11],s_list[12]]
        list05 = [s_list[1], s_list[2], s_list[5], s_list[6], s_list[8], s_list[9],s_list[10]]

        list06 = [s_list[1], s_list[3], s_list[4], s_list[7], s_list[8], s_list[9], s_list[11]]
        list07 = [s_list[1], s_list[3], s_list[5], s_list[9], s_list[10], s_list[11], s_list[12]]
        list08 = [s_list[1], s_list[3], s_list[6], s_list[7], s_list[8], s_list[10], s_list[12]]
        list09 = [s_list[1], s_list[4], s_list[5], s_list[6], s_list[7], s_list[9], s_list[10]]
        list10 = [s_list[2], s_list[3], s_list[4], s_list[6], s_list[7], s_list[8], s_list[11]]

        list11 = [s_list[2], s_list[3], s_list[4], s_list[6], s_list[9], s_list[10], s_list[11]]
        list12 = [s_list[2], s_list[3], s_list[4], s_list[7], s_list[9], s_list[10], s_list[12]]
        list13 = [s_list[2], s_list[3], s_list[4], s_list[7], s_list[8], s_list[9], s_list[12]]
        list14 = [s_list[2], s_list[6], s_list[7], s_list[9], s_list[10], s_list[11], s_list[12]]
        list15 = [s_list[3], s_list[4], s_list[5], s_list[7], s_list[8], s_list[10], s_list[11]]

        list16 = [s_list[4], s_list[5], s_list[6], s_list[7], s_list[9], s_list[11], s_list[12]]

        matrix_list.extend(list(itertools.combinations(list01, 6)))
        matrix_list.extend(list(itertools.combinations(list02, 6)))
        matrix_list.extend(list(itertools.combinations(list03, 6)))
        matrix_list.extend(list(itertools.combinations(list04, 6)))
        matrix_list.extend(list(itertools.combinations(list05, 6)))

        matrix_list.extend(list(itertools.combinations(list06, 6)))
        matrix_list.extend(list(itertools.combinations(list07, 6)))
        matrix_list.extend(list(itertools.combinations(list08, 6)))
        matrix_list.extend(list(itertools.combinations(list09, 6)))
        matrix_list.extend(list(itertools.combinations(list10, 6)))

        matrix_list.extend(list(itertools.combinations(list11, 6)))
        matrix_list.extend(list(itertools.combinations(list12, 6)))
        matrix_list.extend(list(itertools.combinations(list13, 6)))
        matrix_list.extend(list(itertools.combinations(list14, 6)))
        matrix_list.extend(list(itertools.combinations(list15, 6)))

        matrix_list.extend(list(itertools.combinations(list16, 6)))

    else:
        print("备选号码必须为12个数")
    return matrix_list
if __name__ =='__main__':
    last_one=get_last_one_data()
    selected_num_list=[1,2,3,14,16,17,19,21,24,25,28,33]
    results=get_matrix_f7_12_6_5(selected_num_list)
    print(len(results))
    # for i in results:
    #     x=set(last_one)
    #     y=set(i)
    #     a=x.intersection(y)
    #     if len(a)>=4:
    #         print(i)