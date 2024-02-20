def isPrime(n):
    
       if n>3:
           if n%2==0 or n%3==0:
               flag=False
           else:
               flag=True
       if n==2 or n==3:
           flag=True
       else:
           flag=False
       return flag
    
try:
    num=eval(input("请输入一个整数："))
    print("问：整数{}是素数吗？\n答：{}".format(num,isPrime(num)))
except:
    print("请输入数字")
                    
            
                
