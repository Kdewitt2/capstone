def recPI(i):
    if(i==100):
        return 3
    else:
        if(i%2 == 0): #even
            return 4/((i+1) * (i+2) * (i+3)) + recPI(i+1)

def recPI():
    print(recPI(0)) 