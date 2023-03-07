# 문자열 압축


def solution(s):
    answer = len(s)
    cnt = 1
    for step in range(1, len(s) // 2 + 1):
        compression = ""
        prev = s[0:step]
        for i in range(step, len(s), step):
            if prev == s[i : i + step]:
                cnt += 1
            else:
                compression += str(cnt) + prev if cnt >= 2 else prev
                prev = s[i : i + step]
                cnt = 1
        compression += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(compression))
    return answer
