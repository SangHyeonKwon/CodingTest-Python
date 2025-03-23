def solution(strings, n):
    return [item for _, item in sorted(enumerate(strings), key=lambda x: (x[1][n], x[1]))]