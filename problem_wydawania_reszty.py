def reszta(rest, ):
    rest_dict = {}
    my_cash = float(rest)
    denomination_list = [
        0.5, 1, 2, 5, 10, 20, 50,
        100, 200, 500, 0.1, 0.2,
        0.001, 0.002, 0.005
    ]

    try:
        denomination_list.sort()
    except TypeError:
        raise Exception("denomination_list isn't a list")

    for i, cash in enumerate(denomination_list, 1):
        my_list = denomination_list[-i]

        while my_list <= my_cash:
            my_cash -= my_list

            if my_list in rest_dict.keys():
                rest_dict[my_list] += 1
            else:
                rest_dict[my_list] = 1

    return rest_dict
