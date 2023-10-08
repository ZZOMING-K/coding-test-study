def solution(s):
    
    num = ['0','1','2','3','4','5','6','7','8','9']
    eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
    eng_num = dict(zip(eng,num))
    
    for key in eng_num :
        s = s.replace(key , eng_num[key])
    
    
    return int(s)