def solution(array, commands):
    result = []
    for command in commands:
        result.append(sorted(array[command[0] - 1 : command[1]])[command[2] - 1])
    return result