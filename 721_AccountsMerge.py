#https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict
class Solution:

    def mergeComponent(self, accounts: list[list[str]], component: list[int])->list[str]:
        if len(component) == 0:
            raise ValueError(f"cannot have empty components")
        account_name = accounts[component[0]][0]
        emails = set()
        for vertex in component:
            if accounts[vertex][0] != account_name:
                raise ValueError(f"invalid component {component} as have different account names")
            num_emails = len(accounts[vertex])-1
            for i in range(1, num_emails+1):
                emails.add(accounts[vertex][i])
            
        emails = list(emails)
        emails.sort()
        ans = [account_name]
        ans.extend(emails)
        return ans

    def dfs(self, start: int, visited: dict[int, int], label: int, adjacency_dict: dict[int, list[int]], components: dict[int, list[int]]):
        visited[start] = label
        components[label].append(start)
        for nbhr in adjacency_dict[start]:
            if visited[nbhr] != label:
                self.dfs(nbhr, visited, label, adjacency_dict, components)


    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        email_to_pos = defaultdict(list)
        for pos, account in enumerate(accounts):
            num_emails = len(account) - 1
            if num_emails >= 1:
                for i in range(1, num_emails+1):
                    email = account[i]
                    email_to_pos[email].append(pos)

        adjacency_dict = defaultdict(set)
        for email in email_to_pos:
            # Create a complete subgraph
            #for vertex in email_to_pos[email]:
            #    adjacency_dict[vertex].update(email_to_pos[email])

            # Create a star graph, rep_vertex - edge to any other vertex
            num_vertices = len(email_to_pos[email])
            rep_vertex = email_to_pos[email][0]
            for i in range(1, num_vertices):
                adjacency_dict[rep_vertex].add(email_to_pos[email][i])
                adjacency_dict[email_to_pos[email][i]].add(rep_vertex)
        
        label = 0
        visited = {i: label for i in range(n)}
        components = defaultdict(list)
        for vertex in range(n):
            if visited[vertex] == 0:
                label += 1
                self.dfs(vertex, visited, label, adjacency_dict, components)


        merged_accounts = []
        for label in components:
            merged_accounts.append(self.mergeComponent(accounts, components[label]))
        
        return merged_accounts

        
        








                
        