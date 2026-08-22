class Solution:
    def checkDivisibility(self, n: int) -> bool:    
        s=str(n)
        d_sum=0
        d_product=1
        for char in s:
            d=int(char)
            d_sum+=d
            d_product*=d
            total=d_sum+d_product
        if n%total==0:
            return True 
        else:
            return False   
                
        

                

        
            
            
