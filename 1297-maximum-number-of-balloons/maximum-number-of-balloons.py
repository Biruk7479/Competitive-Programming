class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
       d={}
       for i in text:
            if i in d:
                d[i]+=1
            else: d[i] = 1
       output=0
       while d.get('b', 0) >= 1 and d.get('a', 0) >= 1 and d.get('l', 0) >= 2 and d.get('o', 0) >= 2 and d.get('n', 0) >= 1:
            d['b']-=1
            d['a']-=1
            d['l']-=2
            d['o']-=2
            d['n']-=1
            output +=1
       return output    
          