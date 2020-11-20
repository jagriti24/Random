class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [ [ 1 for i in range(n) ] for j in range(m) ]
        return self.recursive_methode(m-1,n-1,visited)
    
    
    def recursive_methode(self,m,n,visited):
        
        if(m==0 or n==0):
            return 1
    
        # print "-----------"
        # print ("m", m)
        # print ("n", n)
        # print "-----------"
        if visited[m][n] == 1:
            visited[m][n] = self.recursive_methode(m-1,n,visited) + self.recursive_methode(m,n-1,visited)
        
        return visited[m][n]
