def solution(s):
    answer=len(s)

    for i in range(1, len(s) // 2+1):
        target=s[0:i]
        compressed=''
        count=1

        for j in range(i, len(s), i):
            if target==s[j:j+1]:
                count+=1
            else:
                compressed+=str(count)+target if count>=2 else target
                target=s[j:j+1]
                count=1
            compressed+=str(count)+target if count>=2 else target
            answer=min(answer, len(compressed))
    
    return answer
