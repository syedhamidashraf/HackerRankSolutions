if __name__ == '__main__':
    N = int(input())

lst=[]
for i in range(N):
    strlst=input().split()
    if strlst[0]=="insert":
        lst.insert(int(strlst[1]),int(strlst[2]))
    elif strlst[0]=="print":
        print(lst)
    elif strlst[0]=="remove":
        lst.remove(int(strlst[1]))
    elif strlst[0]=="append":
        lst.append(int(strlst[1]))
    elif strlst[0]=="sort":
        lst.sort()
    elif strlst[0]=="pop":
        lst.pop()
    elif strlst[0]=="reverse":
        lst.reverse()
