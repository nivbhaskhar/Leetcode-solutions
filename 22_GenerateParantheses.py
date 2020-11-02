#https://leetcode.com/problems/generate-parentheses/solution/

class Solution:
    def generateParenthesis_rec(self, n: int) -> List[str]:
        ans_list = []

        def f(node_string, open, close):
           if open==n and close==n:
            ans_list.append(node_string)
            return 
           if open+1 <= n:
            f(node_string+"(", open+1, close)
           if close+1 <= open and close+1 <= n:
            f(node_string+")", open, close+1)


        f("",0,0)
        return ans_list

      def generateParenthesis(self, n: int) -> List[str]:
        ans_list = []
        if n==0:
            return [""]
        for x in range(n):
            A = self.generateParenthesis(x)
            B = self.generateParenthesis(n-1-x)
            for a in A:
                for b in B:
                    #print("("+a+")"+b)
                    ans_list.append("("+a+")"+b)

        return ans_list


    def generateParenthesis_backtrack(self, n: int) -> List[str]:
        ans_list = []
        state = {"node_string":[], "open": 0, "close":0}
        def f():
           if state["open"]==n and state["close"]==n:
            ans_list.append(''.join(state["node_string"]))
            return
           if state["open"]+1 <= n:
                state["node_string"].append("(")
                state["open"] += 1
                f()
                state["node_string"].pop()
                state["open"] -=1
           if state["close"]+1 <= state["open"] and state["close"]+1 <= n:
                state["node_string"].append(")")
                state["close"] += 1
                f()
                state["node_string"].pop()
                state["close"] -=1
              


        f()
        return ans_list
        


#Complexity
#Exponential
