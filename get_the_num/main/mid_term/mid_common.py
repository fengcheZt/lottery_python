def getIntersectionResults(trend_num_list,alternative_results):
    al_results = []
    for i in alternative_results:
        ll = set(i).intersection(set(trend_num_list))
        if len(ll) > 0:
            al_results.append(i)
    if len(al_results) == 0:
        return alternative_results
    else:
        return al_results