#https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/
from collections import defaultdict, deque

class Solution:

    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        assert len(recipes) == len(ingredients), f"invalid : num recipes ({len(recipes)}) doesn't match ingredient list for recipes ({len(ingredients)})"
        nodes = set(recipes)
        nodes.update(set(supplies))

        needs_new_supplies = set()
        adjacency_dict = defaultdict(list)
        in_degrees = {node:0 for node in nodes}
        for recipe, ingredients_for_recipe in zip(recipes, ingredients):
            for ingredient in ingredients_for_recipe:
                if ingredient not in nodes:
                    needs_new_supplies.add(recipe)
                else:
                    adjacency_dict[ingredient].append(recipe)
                    in_degrees[recipe] +=1
        
        to_explore = deque(supplies)
        final_recipes = []
        while to_explore:
            new_recipe = to_explore.popleft()
            if new_recipe not in needs_new_supplies:
                final_recipes.append(new_recipe)
                for nbhr in adjacency_dict[new_recipe]:
                    in_degrees[nbhr]-=1
                    if in_degrees[nbhr] == 0:
                        to_explore.append(nbhr)
        
        return final_recipes[len(supplies):]
    
    def can_create_recipe(self, recipe: str, ingredients_dict: dict[str, list[str]], memo_dict: dict[str, bool], visited: set[str])->bool:

        if recipe in memo_dict:
            return memo_dict[recipe]
        if recipe in visited:
            can_create = False
        else:
            visited.add(recipe)
            if recipe not in ingredients_dict:
                can_create = False
            else:
                can_create = True
                for ingredient in ingredients_dict[recipe]:
                    can_create &= self.can_create_recipe(ingredient, ingredients_dict, memo_dict, visited)
                    if not can_create:
                        break


        memo_dict[recipe] = can_create
        return can_create



    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        assert len(recipes) == len(ingredients), f"invalid : num recipes ({len(recipes)}) doesn't match ingredient list for recipes ({len(ingredients)})"
        ingredient_dict = {}
        for recipe, ingredients_for_recipe in zip(recipes, ingredients):
            ingredient_dict[recipe] = ingredients_for_recipe
        
        memo_dict = {supply_item: True for supply_item in supplies}
        visited = set()
        final_recipes = []
        for recipe in recipes:
            if self.can_create_recipe(recipe, ingredient_dict, memo_dict, visited):
                final_recipes.append(recipe)
        return final_recipes