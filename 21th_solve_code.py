An = [2,0,0,0,0,0,0,0,0,0]
An_sum = An[0]
#Define List An

for i in range(1,10):
    An[i] = An[i-1]*2
    An_sum += An[i]
#An = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

print(An)
print(An_sum) #2046

try:
    for a in reversed(range(10)):
        An[a] = -An[a]
        An_sum = 0
        for q in range(0, 10):
            An_sum += An[q]
        if An_sum < 0:
            for b in range(0, 10):
                An[b] = -An[b]
                An_sum = 0
                for q in range(0, 10):
                    An_sum += An[q]
                if An_sum == -14:
                    result = 0
                    for j in range(0, 10, 2):
                        result += An[j]
                    print(result)
                    raise NotImplementedError

except:
    print("end")
