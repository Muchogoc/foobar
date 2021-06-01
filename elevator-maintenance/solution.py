def solution(l):
    parsed = []
    for e in l:
        parsed.append(e.split("."))

    parsed_ints = []
    for e in parsed:
        parsed_ints.append(list(map(int, e)))

    parsed_ints.sort()

    sorted_joined = []
    for sorted_int in parsed_ints:
        string_ints = [str(x) for x in sorted_int]
        sorted_joined.append(".".join(string_ints))

    return sorted_joined

