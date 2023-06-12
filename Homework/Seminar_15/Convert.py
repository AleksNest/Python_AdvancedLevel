def convert_format(input: list[str] = None) -> list[float]:
    '''Преобразования входных данных в терминале в матрицу'''
    if len(input) == 1:
        j = 0
    else:
        j = 1
    m_1 = []
    m_2 = []
    input[j].append(' ')
    for i in input[j]:
        if i == ' ':
            m_2.append(list(m_1))
            m_1.clear()
        else:
            m_1.append(float(i))
    return m_2


# f = [['1', '1', '1', ' ', '1', '1', '1',' ', '1', '1', '1', ' ', '1', '1', '1']]
# f1 =[['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1', '1'], ['1', '2', '4', ' ', '2', '5', '2', ' ', '2', '5', '3']]
#
# print(convert_format(f1))