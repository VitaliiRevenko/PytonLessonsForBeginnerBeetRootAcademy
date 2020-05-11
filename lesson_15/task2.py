# Task 2
#
# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss. You're not allowed to add
# instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.
#
# id_ - is just a random unique integer
#
# class Boss:
#     def __init__(self, id_: int, name: str, company: str):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.workers = []
#
# class Worker:
#     def __init__(self, id_: int, name: str, company: str, boss: Boss):
#         self.id = id_
#         self.name = name
#         self.company = company
#         self.boss = boss

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id
        self.name = name
        self.company = company
        self._workers = ["Petya", "Vanya", "Alex"]

    @property
    def worker(self):
        print("getter")
        return self._workers
    @worker.setter
    def worker(self, value):
        print("setter")
        self._workers.append(value)
    @worker.deleter
    def worker(self):
        print("deleter")
        del self._workers

    def __getitem__(self, idx):
        print("getitem")
        return self._workers[idx]

    def __setitem__(self, idx, value):
        print("setitem")
        self._workers[idx] = value

    def add_worker(self,val):
        if isinstance(val, Worker):
            if val not in self._workers:
                self._workers.append(val)
                return True
            return False
        raise TypeError("Type Error")

class Worker:

    def __init__(self, id_: int, name: str, company: str, b: Boss):
        if isinstance(b, Boss):
            self.__boss = b
        self.id = id_
        self.name = name
        self.company = company

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, val):
        if isinstance(val, Boss):
            val.add_worker(self)
            self._boss = val

if __name__ == '__main__':
    b = Boss(1, 'Vitalii', "NASA" )
    w = Worker
    b.worker = "Evgeniy"
    print(b.worker)
    del b.worker[2]
    print(b.worker)
    print(b[2])
    b[2] = "Zhora"
    print(b.worker)
    #w.add_worker("fsdf")