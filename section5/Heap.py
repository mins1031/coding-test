'''
힙의 조건
1. 각 노드의 값은 최대 힙의 경우 해당 노드의 자식 노드가 가진 값보다 크거나 같고 최소 힙의 경우 작거나 같다
2. 완전 이진 트리 형태를 가진다.(왼쪽부터 )

힙 데이터 삽입의 경우
1. 먼저 데이터의 위치부터 특정해 넣어준다. (왼쪽부터 채워가는 작업)
2. 이후 부모 노드와 대소비교후 크면 부모노드와 자리를 바꾸는 과정을 반복하는 것으로 자기 자리를 찾아간다.

힙의 데이터 삭제의 경우
1. 먼저 최대 or 최소값인 제일 위의 루트 노드를 삭제한다.(힙은 최대, 최소값을 빠르게 찾기 위해 고안된 자료구조이다)
2. 이후 가장 마지막으로 삽입된 데이터를 루트노드로 올린다
3. 이후 자식 노드들과 비교해 더 큰값과 바꿔가는 과정을 반복해 자리를 찾아간다.(이렇게 해야 최대 값을 루트 노드로 올릴수 있다)

힙을 리스트로 구현시
부모 노드 인덱스 = 자식 노드 인덱스 // 2
왼쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2
오른쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 1
참고로 리스트로 구현한다면 삽입은 1차적으론 리스트.append함수로 충분한게 어짜피 끝에서 부터 추가하면 왼쪽부터 채워가는 거나 다름이 없기 때문
'''

# 힙 구현
class Heap:
    # def __init__(self):
    #     self.heap_array = list()
    #     self.heap_array.append(None)

    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

    def move_down(self, poped_idx):
        child_left_idx = poped_idx * 2
        child_right_idx = poped_idx * 2 + 1
        # case 1: 왼쪽 자식 노드도 없을때
        if child_left_idx >= len(self.heap_array):
            # child_left_idx >= len(self.heap_array)는 없는 노드 인덱스를 가리키고 있는 경우이다
            return False
        # case 2: 오른쪽 자식 노드만 없을때
        elif child_right_idx >= len(self.heap_array):
            if self.heap_array[poped_idx] < self.heap_array[child_left_idx]:
                return True
            else:
                return False
        # case 3:  왼,오 자식 모두 있을때
        else:
            if self.heap_array[child_left_idx] < self.heap_array[child_right_idx]:
                if self.heap_array[poped_idx] < self.heap_array[child_right_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[poped_idx] < self.heap_array[child_left_idx]:
                    return True
                else:
                    return False

        return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return 0

        returned_data = self.heap_array[1]

        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        poped_idx = 1

        while self.move_down(poped_idx):
            child_left_idx = poped_idx * 2
            child_right_idx = poped_idx * 2 + 1
            # case 2: 오른쪽 자식 노드만 없을때
            if child_right_idx >= len(self.heap_array):
                if self.heap_array[poped_idx] < self.heap_array[child_left_idx]:
                    self.heap_array[poped_idx], self.heap_array[child_left_idx] = self.heap_array[child_left_idx], self.heap_array[poped_idx]
                    poped_idx = child_left_idx
            # case 3:  왼,오 자식 모두 있을때
            else:
                if self.heap_array[child_left_idx] < self.heap_array[child_right_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[child_right_idx]:
                        self.heap_array[poped_idx], self.heap_array[child_right_idx] = self.heap_array[child_right_idx], self.heap_array[poped_idx]
                        poped_idx = child_right_idx
                else:
                    if self.heap_array[poped_idx] < self.heap_array[child_left_idx]:
                        self.heap_array[poped_idx], self.heap_array[child_left_idx] = self.heap_array[child_left_idx], self.heap_array[poped_idx]
                        poped_idx = child_left_idx
        return returned_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
# [None, 20, 10, 15, 5, 4, 8] 큰값이 부모 노드로 올려쳐진것을 확인할 수 있다
print(heap.pop())
print(heap.heap_array)



    

