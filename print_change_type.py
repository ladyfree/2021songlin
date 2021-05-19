#숫자와 문자열 사이의 형변환
i_num = int(input("정수를 입력하세요 : ")) # string값을 integer로 변환
print(i_num, type(i_num))

f_num = float(input("실수를 입력하세요 : ")) # string값을 float로 변환
print(f_num, type(f_num))

s_num = str(i_num) # integer값을 string로 변환
print(s_num, type(s_num))

s_num = str(f_num) # float값을 string로 변환
print(s_num, type(s_num))
