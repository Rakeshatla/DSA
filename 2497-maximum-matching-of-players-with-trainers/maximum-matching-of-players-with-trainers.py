class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        n=len(players)
        m=len(trainers)
        res=0
        i,j=0,0
        while(i<n and j<m):
            if(players[i]<=trainers[j]):
                res+=1
                i+=1
                j+=1
            else:
                i+=1
            # print(players[i],trainers[j])
        return res