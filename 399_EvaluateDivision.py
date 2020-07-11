#https://leetcode.com/problems/evaluate-division/
from collections import defaultdict, deque
class Solution:
     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
         
        adj_dict = defaultdict(list)
        for edge,val in zip(equations,values):
            adj_dict[edge[0]].append((edge[1],val))
            if val!=0:  
                adj_dict[edge[1]].append((edge[0],1/val))
                
        def answer_query(query:List[str])->float:
            visited = {}
            for variable in adj_dict:
                visited[variable]=False
            
            a=query[0]
            b=query[1]
            if a not in visited or b not in visited:
                return -1.0
            visited[a]=True
            parent = {a:(None,1)}
            if b==a:
                    return 1.0
            to_be_explored=deque([a])
            flag=False
            while to_be_explored:
                if flag:
                   break
                current_vertex=to_be_explored.popleft()
                
                for child,edgeval in adj_dict[current_vertex]:
                    if visited[child] is False:
                        parent[child]=(current_vertex,edgeval)
                        visited[child]=True
                        to_be_explored.append(child)
                    if child==b:
                       flag=True
                       break
            if visited.get(b, False):
                answer=1.0
                current_child=b
                while(parent[current_child][0]):
                     answer *= parent[current_child][1]
                     current_child = parent[current_child][0]
                return answer
            else:
               return -1.0
        
        answerlist = list(map(answer_query,queries))
        return answerlist 


#Complexity analysis
#N number of equations
#2N edges and <= 2N vertices
#Creating the graph O(N)
#answer_query O(2N+2N+N)=O(N)
#Q queries => O(QN)

    


