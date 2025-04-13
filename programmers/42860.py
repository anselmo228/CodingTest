def solution(name):
    result = 0
    for n in name:
        joy = min(abs(ord(n)-ord('A')), abs(ord(n)-ord('Z')) + 1)
        result += joy
        
    nameA = []
    listA = []
    for i in range(len(name)):
        if name[i] == 'A':
            if i > 0: 
                if name[i-1] == 'A':
                    nameA.append(i)
            else:
                listA.append(nameA)
                nameA = []
                nameA.append(i)
    cnt = 0
    for lista in listA:
        cnt = len(lista)
        
        result += min(cnt, len(name) - lista[-1] + lista[0])       

    return result