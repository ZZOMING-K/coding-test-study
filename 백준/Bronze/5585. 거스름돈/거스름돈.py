x = int(input()) 
money = 1000 - x 

result =0

coin = [500 ,100 ,50 ,10 ,5 ,1] #가장 큰 화폐부터 거슬러주기 

for i in coin : 
    result += money //i #화폐로 나눈 몫을 잔돈 개수에 추가 
    money = money % i #나머지를 money 변수에 저장 

print(result) 