if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    mrk=0.0
    for i in student_marks[query_name]:
        mrk+=i
    mrk=mrk/3
    print(format(mrk, ".2f"))
