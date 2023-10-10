def solution(park, routes):
    
    dx = {"N" : -1 , "S" : 1 , "W" : 0 ,"E" : 0}
    dy = {"N" : 0 , "S" : 0 , "W" : -1 ,"E" : 1}
    

    #시작지점 찾기 
    x,y = -1,-1
    n,m = len(park) , len(park[0])
    for i in range(n) :
        for j in range(m) :
            if park[i][j] == 'S' :
                x,y = i,j 
                break
         

    for route in routes :
        op , count = route.split(' ')
       
        for i in range(1,int(count)+1) :
                
            nx = x + dx[op]*i
            ny = y + dy[op]*i
                
            if 0 <= nx < n and 0 <= ny < m and park[nx][ny] != "X" :
                continue 
            else :
                break
        else :
            x,y = nx,ny
         
    
    return [x,y] 
                    