#https://leetcode.com/problems/remove-invalid-parentheses/description/

import pprint
class Solution:
    def remove_parantheses_rec(self, global_data: dict, node_state: dict):

        current_pos = node_state["position"]

        if current_pos == len(global_data["expression"]):
            is_valid = node_state["kept_open"] == node_state["kept_closed"]
            open_removed = node_state["removed_open"] == global_data["remove_open"]
            closed_removed = node_state["removed_closed"] == global_data["remove_closed"]
            if is_valid and open_removed and closed_removed:
                assert len(node_state["removed_positions"]) == node_state["removed_closed"] + node_state["removed_open"], f"something went wrong"
                valid_expression = []
                for i, character in enumerate(global_data["expression"]):
                    if i not in node_state["removed_positions"]:
                        valid_expression.append(character)
                global_data["valid_expressions"].add("".join(valid_expression))
            #else:
            #    print(f"pruning didn't work: {node_state}, {global_data}")
            return

        node_state["position"] += 1
        if global_data["expression"][current_pos] == "(":
            # remove current "("
            if node_state["removed_open"] < global_data["remove_open"]:
                # update to next node_state
                node_state["removed_open"] += 1
                node_state["removed_positions"].append(current_pos)
                #node_state["position"] += 1
                # recurse
                self.remove_parantheses_rec(global_data, node_state)
                # backtrack
                #node_state["position"] -= 1
                node_state["removed_open"] -= 1
                node_state["removed_positions"].pop()
            # keep current "("
            if global_data["total_open"]-global_data["remove_open"] - node_state["kept_open"]  <= global_data["total_closed"]-global_data["remove_closed"] - node_state["kept_closed"]:
                # update to next node_state
                node_state["kept_open"] += 1
                #node_state["position"] += 1
                # recurse
                self.remove_parantheses_rec(global_data, node_state)
                # backtrack
                node_state["kept_open"] -= 1
                #node_state["position"] -= 1


        elif global_data["expression"][current_pos] == ")":
            # remove current ")"
            if node_state["removed_closed"] < global_data["remove_closed"]:
                # update to next node_state
                node_state["removed_closed"] += 1
                node_state["removed_positions"].append(current_pos)
                #node_state["position"] += 1
                # recurse
                self.remove_parantheses_rec(global_data, node_state)
                # backtrack
                #node_state["position"] -= 1
                node_state["removed_closed"] -= 1
                node_state["removed_positions"].pop()
            # keep current ")"
            if node_state["kept_open"] > node_state["kept_closed"]:
                # update to next node_state
                node_state["kept_closed"] += 1
                #node_state["position"] += 1
                # recurse
                self.remove_parantheses_rec(global_data, node_state)
                # backtrack
                node_state["kept_closed"] -= 1
                #node_state["position"] -= 1

        else:
            # update to next node_state
            #node_state["position"] += 1
            # recurse
            self.remove_parantheses_rec(global_data, node_state)
            # backtrack
            #node_state["position"] -= 1

        
        node_state["position"] -= 1
        return


    def removeInvalidParentheses(self, s: str) -> list[str]:

        total_open = 0
        total_closed = 0
        current_open = 0
        remove_closed = 0
        for character in s:
            if character == "(":
                current_open += 1
                total_open += 1
            elif character == ")":
                total_closed += 1
                if current_open > 0:
                    current_open -= 1
                else:
                    remove_closed += 1
        remove_open = current_open
        global_data = {
            "expression": s,
            "total_open": total_open,
            "total_closed": total_closed,
            "remove_open": remove_open,
            "remove_closed": remove_closed,
            "valid_expressions": set()
        }

        initial_state = {
            "position": 0,
            "kept_open":0,
            "kept_closed":0,
            "removed_open":0,
            "removed_closed":0,
            "removed_positions":[],
        }

        self.remove_parantheses_rec(global_data, initial_state)




        
        return list(global_data["valid_expressions"])