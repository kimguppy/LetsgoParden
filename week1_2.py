def solution(rows, columns, queries):
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    
    #List 내 for 문:  List 내에 for문을 사용하는 방법
    #[실행문 + for i in (rang or list) + 조건문] 

    t = 1
    
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t+= 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]

        for k in range(x1-1, x2-1):
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            min_num = min(min_num, test)
            
        for k in range(y1-1,y2-1):
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            min_num = min(min_num, test)
            
            
        for k in range(x2-1,x1-1,-1):
                test = array[k-1][y2-1]
                array[k][y2-1] = test
                min_num = min(min_num, test)

        for k in range(y2-1,y1-1,-1):
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            min_num = min(min_num, test)
            
        array[x1-1][y1] = tmp
        answer.append(min_num)
        
    return answer