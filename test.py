Flag = True
times = 0
P1_a = 1.0 # the percent of liquid A in box 1
P1_b = 0.0 # the percent of liquid A in box 1
P2_b = 1.0 # the percent of liquid A in box 1
P2_a = 0.0 # the percent of liquid A in box 1
v = 100 # the Volume of the box
s = 10 # the Volume of the scope

error_threshold = 1e-6 # the gap between A/B percent and 50%

while Flag:
    times += 1
    P2_a = (v * P2_a + P1_a * s) / (v+s)
    P2_b = (v * P2_b + P1_b * s) / (v + s)

    times += 1
    P1_b = (P1_b * (v-s) + s * P2_b) / (v)
    P1_a = (P1_a * (v-s) + s * P2_a) / (v)

    # test if the Volume never change
    # print(times,P1_a,P2_b, P1_a*v+P2_a*v, P1_b*v+P2_b*v)

    if P1_a - 0.5 < error_threshold:
        print ("it needs "+str(times)+" times")
        print("when B liquid in box 1 reaches " + str(P1_b) + " % and A liquid in box 2 reaches " + str(P2_a) + "%")
        break