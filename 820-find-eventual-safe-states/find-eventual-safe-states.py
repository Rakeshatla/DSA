from collections import deque,defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        degree=[0]*len(graph)
        h=defaultdict(list)
        for i in range(len(graph)):
            for j in graph[i]:
                h[j].append(i)
        print(h)
        for i in range(len(graph)):
            degree[i]=len(graph[i])
        # print(degree)
        queue=deque()
        for i in range(len(degree)):
            if degree[i]==0:
                queue.append(i)
        # print(queue)
        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for nei in h[node]:
                degree[nei]-=1
                if degree[nei]==0:
                    queue.append(nei)
            # print(queue)
        res.sort()
        return res
