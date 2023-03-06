while True:
    try:
        print(input())
    except EOFError: #end of file
        break