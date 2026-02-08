if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    liarr=list(arr)
    liarr.sort(reverse=True)
    a=max(liarr)
    for i in liarr:
        if i<a:
            print(i)
            break
