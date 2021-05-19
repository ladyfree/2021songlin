# 동전 교환 프로그램
# f-string 형태로 출력하기
coin, coin500, coin100, coin50, coin10 = 0,0,0,0,0
money = int(input("교환할 돈은 얼마인가요? "))
coin = 500; coin500 = money // coin; money %= coin # 500원짜리 동전의 갯수 계산하기
coin = 100; coin100 = money // coin; money %= coin # 100원짜리 동전의 갯수 계산하기
coin = 50;   coin50   = money // coin; money %= coin # 50원짜리 동전의 갯수 계산하기
coin = 10;   coin10   = money // coin; money %= coin # 10원짜리 동전의 갯수 계산하기

print(f"동전 : 500원 {coin500}개,  100원 {coin100}개,  50원 {coin50}개,  10원 {coin10}개")

