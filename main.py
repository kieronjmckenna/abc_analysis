b_data = [
    [1, 398, 18],
    [2, 533, 866],
    [3, 9, 613],
    [4, 239, 8501],
    [5, 219, 494],
    [6, 930, 84],
    [7, 543, 1988],
    [8, 385, 187],
    [9, 29, 2],
    [10, 0.2, 1],
    [11, 0.5, 10],
    [12, 12, 12699],
    [13, 1458, 1471],
    [14, 9599, 815],
    [15, 273, 10],
    [16, 7, 2],
    [17, 0.9, 5],
    [18, 1.5, 39],
    [19, 2, 155],
    [20, 5, 4],
    [21, 7, 3],
    [22, 10, 3],
]

c_data = [
    [1, 205, 18],
    [2, 1375, 866],
    [3, 1175, 613],
    [4, 4945, 8501],
    [5, 185, 495],
    [6, 431, 84],
    [7, 396, 1988],
    [8, 125, 187],
    [9, 43, 2],
    [10, 5, 1],
    [11, 20, 10],
    [12, 5890, 122699],
    [13, 338, 1471],
    [14, 2484, 815],
    [15, 98, 10],
    [16, 25, 2],
    [17, 55, 5],
    [18, 1, 39],
    [19, 11, 155],
    [20, 42, 4],
    [21, 0.5, 3],
    [22, 1.2, 3],
]


def takeSecond(elem):
    return elem[1]


def do_bullshit_ABC_analysis(dataList, break1, break2, dataColumn):

    dataList.sort(key=takeSecond, reverse=True)

    xList = []

    yList = []

    zList = []

    for company in dataList:
        print(company[1])
        print(break1)
        if company[dataColumn] >= break1:
            xList.append(company[0])
        elif break2 < company[dataColumn] < break1:
            yList.append(company[0])
        else:
            zList.append(company[0])

    print(f"In order \n\n X List {xList} \n \nY List {yList} \n \n Z List {zList}")


if __name__ == "__main__":
    b_or_c = input("Enter b or c (program will quit on anything else): ")

    if b_or_c == "b":
        do_bullshit_ABC_analysis(b_data, 1000, 200, 1)
    elif b_or_c == "c":
        do_bullshit_ABC_analysis(c_data, 500, 200, 2)
    else:
        print("exited")
