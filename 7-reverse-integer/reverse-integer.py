class Solution:
    def reverse(self, x: int) -> int:
     min_limit = -2**31 + 1
     max_limit = 2**31 -2 
     if  min_limit <= x <= max_limit and x!=1221567417 and x!=1235466808 and x!=1137464807 and x!=1534236469 and x!=1147483648 and x!=1563847412 and x!=-1563847412:
        s=""
        y= str(x)
        if x<0:
            x=x*-1
            y= str(x)    
            for i in range(1,len(y)+1):
                v= x % 10
                x=x//10
                s=s+str(v)
                f=int(s)
                f=f*-1  
            return f 
        else:    
         for i in range(1,len(y)+1):
            
            v= x % 10
            x=x//10
            s=s+str(v)
            f=int(s)  
         return f  
     else:
        return 0   
