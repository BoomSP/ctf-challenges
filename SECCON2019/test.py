rot = [51, 37, 35, 35, 47, 46]
cnt  = 0

f = open("dump.txt", "r")
for x in f:
    #print(cnt%6, end = ' ')
    cnt = cnt+1
    # print(int(x), end = ' ')
    y = int(x) - 32
    # print(y, end = ' ')

    if(cnt%6 == 1):
        s = y + 76
    elif(cnt%6 == 2):
        s = y - 5
        if(s < 60):
            s = s + 95
    elif(cnt%6 == 3):
        s = y - 3
        if(s < 60):
            s = s + 95
    elif(cnt%6 == 4):
        s = y - 3
        if(s < 60):
            s = s + 95
    elif(cnt%6 == 5):
        s = y - 15
        if(s < 60):
            s = s + 95
    else:
        s = y - 14
        if(s < 60):
            s = s + 95
    print(chr(s), end = '')

# for i in range(1,10):
#     print rot[i%len(a)]