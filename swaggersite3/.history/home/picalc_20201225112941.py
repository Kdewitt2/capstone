def recPI(i):
    if(i==100):
        return 0
    else:
        if(i%2 == 0): #even
            return 4/((i+1) * (i+2) * (i+3)) + recPI(i+1)
        if(i%2 == 1): #odd
            return 4/((i+1) * (i+2) * (i+3)) - recPI(i+1)
            
    
def main():
    print(3 + recPI(0))

