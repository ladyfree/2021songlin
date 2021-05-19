# 체질량지수를 계산하기
print( '체질량지수 (BMI)를 계산식')
print( '(참고 사항) 정상 : 0.18~0.22')

weight = int(input('체중 (kg)를 입력하세요 : '))
height = float(input('키 (cm)를 입력하세요 : '))/10
bmi = weight / (height * height)
comment = 'BMI는 %d/(%.2f * %.2f)이므로 %6.2f입니다.'
#퀴즈
print( comment % ___________________) # %로 여러 값을 출력하기

# 정답
print( comment % ( weight, height, height, bmi )) # %로 여러 값을 출력하기




