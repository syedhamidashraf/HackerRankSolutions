if __name__ == '__main__':
    name=[]
    score=[]
    output=[]
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    
    students=dict(zip(name,score))
    
    x=min(score)
    while x in score:
        score.remove(x)
    
    y= min(score)
    for i, z in students.items():
        if z==y:
            output.append(i)
    output.sort()       
    for i in output:
        print(i)
