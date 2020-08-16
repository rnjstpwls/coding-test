### DFS / BFS

> 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

* 탐색(Search) : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

* 자료구조(Data Structure) : 데이터를 표현하고 관리하고 처리하기 위한 구조

  * 스택(Stack) : 

    선입후출(First In last Out) 구조

    파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append와 pop 메서드를 이용하면 스택 자료구조와 동일하게 동작한다. append 메서드는 리스트의 가장 뒤쪽에 데이터를 삽입하고, pop 메서드는 리시트의 가장 뒤쪽에서 데이터를 꺼내기 때문이다.

  * 큐(Queue) : 

    선입선출(First In First Out) 구조

    파이썬에서 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용한다.



#### 재귀함수



#### DFS (Depth First Search)

> 깊이 우선 탐색. 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3.  2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```



#### BFS (Breath First Search)

> 너비 우선 탐색. 가까운 노드부터 탐색하는 알고리즘

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3.  2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```





DFS BFS 모두 탐색을 수행함에 있어 ***O(N)***의 시간이 소요된다. 일반적인 경우 실제 수행 시간은 DFS 보다 BFS가 좋은 편이다.