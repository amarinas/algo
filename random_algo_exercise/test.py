import re
def solution(S):
    count = 0

    # print newS
    for i in S:
        count = max(count, len(i.split()))
    return count


S = ["We test coders", "Give us a try", ""]
S2 =["Forget  CVs..Save time . x x"]
# print(solution("we test coders. give us a try?"))

print solution(S)
print solution(S2)
