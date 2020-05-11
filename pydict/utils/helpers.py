def levenshtein_distance_and_ratio(str_a, str_b, calc_ratio=False):
    rows = len(str_a)
    cols = len(str_b)

    matrix = [[0] * cols for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][0] = i
            matrix[0][j] = j

    for col in range(1, cols):
        for row in range(1, rows):
            if str_a[row] == str_b[col]:
                cost = 0
            else:
                if calc_ratio:
                    cost = 2
                else:
                    cost = 1

            matrix[row][col] = min((matrix[row - 1][col] + 1,
                                    matrix[row][col - 1] + 1,
                                    matrix[row - 1][col - 1] + cost))

    if calc_ratio:
        return ((rows + cols) - matrix[rows - 1][cols - 1]) / (rows + cols)
    else:
        return matrix[rows - 1][cols - 1]
