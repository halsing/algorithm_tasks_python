def pascal_triangle(n):
    pascal_list = []

    for i in range(n):
        if i == 0:
            pass
        else:
            new_list = []

            for x in range(i):
                if x == 0 or x == i-1:
                    new_list.append(1)
                else:
                    last_pascal = pascal_list[-1]
                    new_int = last_pascal[x-1] + last_pascal[x]
                    new_list.append(new_int)

            pascal_list.append(new_list)

    return pascal_list


def pascal_print(n):
    pascal_list = pascal_triangle(n)
    for lists in pascal_list:
        for i in lists:
            print(i, end=" ")
        print("")
