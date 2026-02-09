if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
a= [a for a in range(x+1)]
b= [b for b in range(y+1)]
c= [c for c in range(z+1)]

lst=[[i,j,k] for i in a for j in b for k in c]

flst=[m for m in lst if sum(m)!=n]

print(flst)
