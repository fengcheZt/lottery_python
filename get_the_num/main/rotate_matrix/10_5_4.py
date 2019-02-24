"""
    10个号码中5保4型旋转矩阵
"""
from get_the_num.main.getData import get_last_one_data
def get_matrix_10_5_4(selected_num_list=[]):
    matrix_list=[]
    selected_num_list.insert(0,-1)
    list =selected_num_list
    if len(list)==11:
        tupple01 = (list[3], list[4], list[6], list[7], list[8], list[9])
        tupple02 = (list[1], list[2], list[3], list[5], list[6], list[8])
        tupple03 = (list[1], list[2], list[3], list[6], list[7], list[10])
        tupple04 = (list[2], list[4], list[5], list[6], list[7], list[10])
        tupple05 = (list[1], list[3], list[5], list[8], list[9], list[10])
        tupple06 = (list[1], list[2], list[4], list[5], list[7], list[9])
        tupple07 = (list[1], list[2], list[4], list[8], list[9], list[10])

        matrix_list=[tupple01,tupple02,tupple03,tupple04,tupple05,tupple06,tupple07]
    else:
        print("备选号码必须为10个数")
    return matrix_list
if __name__ =='__main__':
    last_one=get_last_one_data()
    list=[1,2,3,16,19,21,24,25,28,33]
    results=get_matrix_10_5_4(list)
    for i in results:
        x=set(last_one)
        y=set(i)
        a=x.intersection(y)
        if len(a)>=4:
            print(i)