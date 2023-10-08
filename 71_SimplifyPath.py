#https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 0:
            raise ValueError(f"absolute path {path} cannot be empty")

        if path[-1] != "/":
            path += "/"
        canonical_path_components = []
        processing_stack = []
        for pos, character in enumerate(path):
            if character == "/":
                component = "".join(processing_stack)
                processing_stack = []
                if component == "..":
                    if len(canonical_path_components) > 0:
                        canonical_path_components.pop()
                elif component != "" and component != ".":
                    canonical_path_components.append(component)
            else:
                processing_stack.append(character)

        return "/" + "/".join(canonical_path_components)