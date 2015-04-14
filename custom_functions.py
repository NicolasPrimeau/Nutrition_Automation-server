def sort_by_date(d_a):
    temp_ar = list()
    temp_ar.append(d_a.pop(0))

    for e in d_a:
        for i in range(len(temp_ar)):
            if temp_ar[i]['date'] > e['date']:
                temp_ar.insert(i, e)
                break
        if e not in temp_ar:
            temp_ar.append(e)

    return temp_ar