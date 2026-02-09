
# Complete the solve function below.
def solve(s):
    name=s[0].upper()
    for i in range(1,len(s)):
        if s[i-1]==" ":
            name+=s[i].upper()
            continue
        name+=s[i]
    return name
