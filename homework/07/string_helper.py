def csv_to_list(csv):
    result = []
    for line in csv.split("\n"):
        result.append(line.split(","))
    return result
