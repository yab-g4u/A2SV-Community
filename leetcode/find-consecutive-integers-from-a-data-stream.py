class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = []
        self.count = {}
        self.unique_elements = set()

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.unique_elements.add(num)
            self.count[num] = self.count.get(num, 0) + 1

        if len(self.queue) > self.k:
            removed_num = self.queue.pop(0)
            if removed_num == self.value:
                self.count[removed_num] -= 1
                if self.count[removed_num] == 0:
                    self.unique_elements.remove(removed_num)

        return len(self.unique_elements) == 1 and self.count[self.value] == self.k
