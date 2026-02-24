def even_only(list_a) -> list :
    even_list = []
    for value in list_a :
        if value % 2 == 0 :
            even_list.append(value)
    return even_list
