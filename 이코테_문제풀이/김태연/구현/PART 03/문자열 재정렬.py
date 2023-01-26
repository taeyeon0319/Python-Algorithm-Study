s = list(input())
n = 0

for i in range (len(s)):
    if s[i].isnumeric:
        print("{}는 숫자".format(s[i]))
    else:
        print("삑")
  
