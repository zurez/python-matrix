
def add(X,Y):
    result= gen_zero(len(X),len(Y[0]))
    for i in range(len(X)):
        for j in range(len(X[0])):
            
            if type(X[i][j])is list and type(Y[i][j]) is list:
                
                result[i][j]=add_frac(X[i][j],Y[i][j])
            if type(X[i][j])is list and type(Y[i][j]) is int:result[i][j]=add_frac(X[i][j],Y[i][j])
            if type(X[i][j])is int and type(Y[i][j]) is list:result[i][j]=add_frac(X[i][j],Y[i][j])
            if type(X[i][j])is int and type(Y[i][j]) is int:result[i][j]=X[i][j]+Y[i][j]
    return result            
def sub(X,Y):
    result= gen_zero(len(X),len(Y[0]))
    for i in range(len(X)):
        for j in range(len(X[0])):
            
            if type(X[i][j])is list and type(Y[i][j]) is list:result[i][j]=add_frac(X[i][j],Y[i][j],"sub")
            if type(X[i][j])is list and type(Y[i][j]) is int:result[i][j]=add_frac(X[i][j],Y[i][j],"sub")
            if type(X[i][j])is int and type(Y[i][j]) is list:result[i][j]=add_frac(X[i][j],Y[i][j],"sub")
            if type(X[i][j])is int and type(Y[i][j]) is int:
                result[i][j]=X[i][j]-Y[i][j]
    return result    
def gen_zero(m,n):
    rm = [[0 for row in range(n)] for col in range(m)]
    return rm
def add_frac(a,b,mode="add"):
    #mode :: add,sub
    if a==b and a[1]/2!=1 and a[1]%2==0:
        print "A"
        return [a[0],(a[1]/2)]
    elif a==b and a[1]/2!=1 and a[1]%2!=0:
        return [(a[0]*2),a[1]]
    elif a==b and a[1]/2==1:
         return a[0]
    if type(a) is list  and type(b) is list:
        pass
    elif type(a) is list and type(b) is int:
        
        b= [b,1]
        
    elif type(a) is int and type (b) is list:
        
        a = [a,1]
    
    
    g= gcd(a[1],b[1])
    den= (a[1]/g) * (b[1]/g)
    #den should be an int
    if mode=="add":
        num = ((den/a[1]) * a[0])+((den/b[1]) * b[0])
    elif mode=="sub":
        num = ((den/a[1]) * a[0])-((den/b[1]) * b[0])
    if den==1:
        return num
    else:return [num,den]

def mult(X,Y):
    result= gen_zero(len(X),len(Y[0]))
    for i in range(len(X)):
       # iterate through columns of Y
        for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               #Check for irrational
               if type(X[i][k])is list and type(Y[k][j]) is list:
                   print "a"
                   result[i][j] = add_frac(result[i,j], mult_frac(X[i][k] * Y[k][j]))
               if type(X[i][k])is list and type(Y[k][j]) is int:
                   print "b"
                   a= X[i][k]
                   b=Y[k][j]
                
                   p = mult_frac(a ,b )
                   
                   result[i,j]=add_frac(result[i,j], p)
               if type(X[i][k])is int and type(Y[k][j]) is list:
                   print "c"
                   add_frac(result[i,j], mult_frac(X[i][k] * Y[k][j]))
               if type(X[i][k])is int and type(Y[k][j]) is int:
                   print "d"
                   result[i][j] += X[i][k] * Y[k][j]
    return result
   
            
   
def gcd(x,y):
    
    while y:
        x, y =y, x%y
    return x
def clean(v):
    num= v[0]
    den=v[1]
   
    g = gcd(num,den)
    if den/g==1:
        return num/g
    return [num/g,den/g]
def get_inner(nested):
    
    if all(type(x) == list for x in nested):
        return sum(map(get_inner, nested), [])
    return [nested]
def mult_frac(a,b):
    if type(a) is not list: a= [a,1]
    if type(b) is not list: b= [b,1]

    return clean([(a[0]*b[0]),(a[1]*b[1])])
#Main Function
def mateval(A):
    op= ["+","-","*"]
   
#Testing
x= [[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[5,7,3],[4,5,9]]
a= [[[1,2],[2,3]],[[1,4],[1,5]]]
b=[]
test1= [[2,[-1,2]],[[7,3],5]]
test2=[[4,[2,7]],[8,2]]

print mult(test1,test2)

