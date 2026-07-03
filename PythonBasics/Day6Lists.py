if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(1, N+1):
        inp_List = input().split()
        command = inp_List[0]
        if command == "insert":
          lst.insert(int(inp_List[1]), int(inp_List[2]))
        if command == "print":
            print(lst)
        if command == "remove":
            lst.remove(int(inp_List[1]))
        if command == "append":
            lst.append(int(inp_List[1]))
        if command == "sort":
            lst.sort()
        if command == "pop":
            lst.pop()
        if command == "reverse":
            lst.reverse()
