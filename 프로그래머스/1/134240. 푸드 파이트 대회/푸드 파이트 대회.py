def solution(food):
    result = ""
    for idx, f in enumerate(food, start=1):
        result += str(idx - 1) * (f // 2)
    result += "0"
    result += result[-2::-1]
    return result

