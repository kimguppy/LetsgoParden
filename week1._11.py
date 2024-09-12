def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        # n을 3으로 나눈 몫과 나머지를 동시에 반환하는 코드
        answer += str(re)
    
    return int(answer, 3)