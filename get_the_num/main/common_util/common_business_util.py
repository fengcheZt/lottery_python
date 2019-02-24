def get_sql_id_list_str(sql,alternative_results):
    id_list_str = ''
    for i in alternative_results:
        id_list_str = id_list_str + str(i[0])+","
    if len(alternative_results) != 0:
        sql = sql + " AND t.all_ssq_id in(%s)" % \
              id_list_str[0:-1]
    return sql
if __name__ =='__main__':
    str="sdfsdfsdf,"
    print(str[0:-1])