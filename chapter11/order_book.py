# Write your solution here:

class Task:
    id_counter = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.finished = False

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.tasks = []
        self.programmers_list = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.tasks.append(task)
        if programmer not in self.programmers_list:
            self.programmers_list.append(programmer)

    def all_orders(self):
        return self.tasks

    def programmers(self):
        return self.programmers_list

    def mark_finished(self, id: int):
     
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                return
       
        raise ValueError(f"No task with id {id}")

    def finished_orders(self):
        finished_tasks = []
        for task in self.tasks:
            if task.finished:
                finished_tasks.append(task)
        return finished_tasks

    def unfinished_orders(self):
        unfinished_tasks = []
        for task in self.tasks:
            if not task.finished:
                unfinished_tasks.append(task)
        return unfinished_tasks

    def status_of_programmer(self, programmer: str):
        finished_count = 0
        unfinished_count = 0
        finished_hours = 0
        unfinished_hours = 0
        programmer_exists = False

        for task in self.tasks:
            if task.programmer == programmer:
                programmer_exists = True
                if task.finished:
                    finished_count += 1
                    finished_hours += task.workload
                else:
                    unfinished_count += 1
                    unfinished_hours += task.workload

        if not programmer_exists:
            raise ValueError(f"No programmer with name {programmer}")


        return (finished_count, unfinished_count, finished_hours, unfinished_hours)
        