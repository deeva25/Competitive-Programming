while True:
    try:
        n = list(map(int, input().split(" ")))
        s = n[0] + n[1]
        print(s)
    except EOFError  :
        break