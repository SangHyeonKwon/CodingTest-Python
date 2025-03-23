def solution(s):
    num_list = ["zero", "one","two","three","four","five","six","seven","eight","nine"]
    
    for x in range(len(num_list)):
        s = s.replace(num_list[x], str(x))
    return int(s)