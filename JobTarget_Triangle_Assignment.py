"""Write a program in a language of your choice to find the maximum total from top to bottom in
triangle.txt, a text file containing a triangle with 100 rows. """

#Opening and reading file in correct format
f = open("triangle.txt", "r")   
l = []
t = []
tri = []
for line in f:
    l.append(line.split(' \n'))
for i in l:
    t.append(i[0])
for i in t:
    tri.append(list(map(int, i.split(' '))))

def maximumTotal(t):
        
        # corner case
        if len(t)==1:
            return t[0][0]
        res = 0
        #Finding adjacent elements and adding with sum i.e res
        for i in range(1,len(t)):
            for j in range(i+1):
                if j==0:
                    t[i][j] += t[i-1][j]     
                elif j==i:
                    t[i][j] += t[i-1][j-1]
                else:
                    t[i][j] += max(t[i-1][j], t[i-1][j-1])
                  
                if i==len(t)-1: res = max(res,t[i][j]) 
        return res
    
    
res = maximumTotal(tri)
print(res)

#Answer for given file is triangle.txt : 732506