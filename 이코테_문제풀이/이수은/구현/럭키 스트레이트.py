N=input()

N_half=len(N)//2

left=list(map(int, N[:N_half]))

right=list(map(int, N[N_half:]))

if(sum(left)==sum(right)):
    print("LUCKY")
else:
    print("READY")
    