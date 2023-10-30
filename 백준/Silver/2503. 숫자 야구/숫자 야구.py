n = int(input())

numbers = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for a in range(1,10): # 100의 자리수
    for b in range(1,10): # 10의 자리수
        for c in range(1,10): # 1의 자리수
            count = 0
            
            if( a == b or b == c or c == a): #세 자리수가 다 다르기 때문에
                continue
        
            for array in numbers:
                hint = list(str(array[0])) # ['1','2','3']
                strike = int(array[1])
                ball = int(array[2])

                strike_count = 0
                ball_count = 0

                #스트라이크 계산기
                if (a == int(hint[0])):
                    strike_count += 1
                if (b == int(hint[1])):
                    strike_count += 1
                if (c == int(hint[2])):
                    strike_count += 1
                

                #볼 계산기
                if (a == int(hint[1]) or a == int(hint[2])):
                    ball_count += 1
                if (b == int(hint[0]) or b == int(hint[2])):
                    ball_count += 1
                if (c == int(hint[0]) or c == int(hint[1])):
                    ball_count += 1
                
                
                #(4) 매칭 여부 확인하기
                if (strike == strike_count) and (ball == ball_count):
                    count+= 1 
                else :
                    break


            if count == n:
                answer += 1
                
print(answer)