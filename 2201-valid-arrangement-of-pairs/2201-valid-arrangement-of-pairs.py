class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        
        stack = [start_node]
        path = []
        
        while stack:
            node = stack[-1]
            if graph[node]:
                next_node = graph[node].popleft()
                stack.append(next_node)
            else:
                path.append(stack.pop())
        
        path.reverse()
        result = [[path[i], path[i+1]] for i in range(len(path) - 1)]
        return result
        