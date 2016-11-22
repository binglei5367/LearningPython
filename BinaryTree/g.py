sum_v = 0
sum_t = 0
sum_t2 = 0
sum_tv = 0
i=0
t=0
while i<8:
    v = float(input("v: "))
    t += 0.05
    sum_v += v
    sum_t += t
    sum_t2 += t**2
    sum_tv += v * t
    i+=1

g = (sum_t/8 * sum_v/8 - sum_tv/8) / ((sum_t/8)**2-(sum_t2/8))

print(g)
