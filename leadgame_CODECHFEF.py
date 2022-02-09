N=int(input())
players={"1":0 ,"2":0}
cumu_sum1=0
cumu_sum2=0
for rounds in range(1,N+1):
    scores_list=list(map(int,input().split()))
    score1=scores_list[0]
    score2=scores_list[1]
    cumu_sum1+=score1
    cumu_sum2+=score2
    
    if cumu_sum1-cumu_sum2 > players.get("1"):
        players["1"]=cumu_sum1-cumu_sum2
    #dict.get("key") is to extract values from key
    if cumu_sum2-cumu_sum1> players.get("2"):
        players["2"]=cumu_sum2-cumu_sum1
        
if players.get("1")>players.get("2"):
    print("1",players.get("1"), sep=" ")
else:
    print("2",players.get("2"), sep=" ")
    
