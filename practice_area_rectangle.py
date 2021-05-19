#사각형의 높이와 넓이를 입력 받아 면적을 계산하여 출력
# format()의 인수번호 사용하여 출력하기
height = int(input("높이를 읿력하세요 :"))
width =  int(input("너비 를 읿력하세요 :"))

print('둘레 :{2} = {0}+{0}+{1}+{1}'.format(height, width, height*2+width*2))
print('면적 :{2} = {0} * {1} '.format(height, width, height*width))

