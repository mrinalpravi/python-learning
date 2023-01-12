if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        choice = input().split()
        if(choice[0] == 'insert'):
            l.insert(int(choice[1]),int(choice[2]))
        elif(choice[0] == 'print'):
            print(l)
        elif(choice[0] == 'remove'):
            l.remove(int(choice[1]))
        elif(choice[0] == 'append'):
            l.append(int(choice[1]))
        elif(choice[0] == 'sort'):
            l.sort()
        elif(choice[0] == 'pop'):
            l.pop()
        elif(choice[0] == 'reverse'):
            l.reverse()
        
