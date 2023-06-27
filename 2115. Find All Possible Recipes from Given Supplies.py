class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        #bfs approach
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)
        
        created = []
        queue = deque(supplies)
        while queue:
            ing = queue.popleft()
            for recipe in graph[ing]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    created.append(recipe)
                    queue.append(recipe)

        return created

        
        
        # dfs approach
        created = set(recipes)
        graph = defaultdict(list)
        colors = defaultdict(int)
        supplies = set(supplies)

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ing in ingredients[i]:
                graph[recipe].append(ing)
        
        def dfs(recipe, colors):
            if recipe not in graph and recipe not in supplies:
                return False

            colors[recipe] = -1
            for ing in graph[recipe]:
                if colors[ing] == 1:
                     continue
                elif colors[ing] == -1:
                    if recipe in created:
                        created.remove(recipe) 
                    return False
                else:
                    if not dfs(ing, colors):
                        if recipe in created:
                            created.remove(recipe)
                        return False
            colors[recipe] = 1
            return True

        
        for recipe in recipes:
            if colors[recipe] == 0:
                dfs(recipe, colors)

        return list(created)
