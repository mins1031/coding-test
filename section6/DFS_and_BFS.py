'''
bfs(너비우선탐색)의 기본적인 알고리즘 로직 자체는
visited  - queue
need_visited - queue
그리고 각 노드별로 인접한 노드 value를 가지고 있는 그래프 - dict()  이렇게 3개가 있다
1. need_visit에 초기값을 넣어놓고 반복문을 돌린다
2. need_visit에서 popleft한다
3. 그래프에서 나온 값(= popV)을 key로 가진 value 들을 need_visited에 추가해준다
4. 또 visited에 popV가 없다면 append해준다.
5. 해당 작업을 need_visited에서 popleft하지 못할때 까지 반복한다.

이게 기본 기조이다.

dfs(깊이우선탐색)의 기본적인 알고리즘 로직 자체는 bfs와 거의 동일하게 구현된다
차이점은
2. need_visit에서 popleft가 아닌 그냥 pop이라고 한다. 다만 이건 그래프... 음.. 그래프 순서를 잘 정렬해놓은 상황에서만 사용될수 있는 로직인거 같은데...
일단 문제 많이 풀어봐야 결론 날듯.

재귀함수를 이용하는 케이스도 있는 것 같은데 일단 이쪽이 더 쉽긴한데 재귀함수를 통해 구현하는게 나중에 편해질 수도 있을것 같다.
'''
from collections import deque


def bfs(graph, start_node):
    visited = deque()
    need_visit = deque()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

def dfs(graph, start_node):
    visited = deque()
    need_visit = deque()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

graph = dict()
graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "G", "H", "I"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["G"] = ["C"]
graph["H"] = ["C"]
graph["I"] = ["C", "J"]
graph["J"] = ["I"]

start_node = "A"

print(bfs(graph, start_node))
print(dfs(graph, start_node))
