def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False
    
print(solution('a234'))
print(solution('1234'))

def alpha_string46(s):
	return s.isdigit() and len(s) in (4,6)

#isdigit을 통해 숫자인지 확인해주고 len(s)의 길이가 (4, 6)에 포함되는지 확인해주는 코드