# 이동 시간을 계산하기
# format()의 키워드 인수 방식으로 코딩하기
velocity = int(input("속도를 입력해 주세요 :"))
distance = int(input("거리를 입력해 주세요 :"))
print("속도 = {v}".format(v = velocity))
print("거리 = {d}".format(d = distance))
print("시간 = {d}/{v} = {t}".format(t = distance/velocity, d = distance, v = velocity))

