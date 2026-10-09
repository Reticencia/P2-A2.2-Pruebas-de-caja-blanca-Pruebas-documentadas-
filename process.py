def process(values):
    result = []
    for value in values:
        if value > 0:
            result.append("positivo")
        if value % 2 == 0:
            result.append("par")
    return result