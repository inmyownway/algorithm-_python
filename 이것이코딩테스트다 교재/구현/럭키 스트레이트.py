
n= input()

front=n[0:len(n)//2]
back=n[len(n)//2:]
front_sum=0
back_sum=0

print(front,back)
for i in range(len(n)//2):
    front_sum+=int(front[i])
    back_sum+=int(back[i])
if front_sum==back_sum:
    print("LUCKY")
else:
    print("READY")
