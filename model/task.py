class Task:
    """"""
    # Atributos
    def __init__(self, __id, title, description, status) -> None:
        self.__id = __id
        self.title = title
        self.description = description
        self.status = status
        
    def get_task_info(self):
        
        print(f"Task id: {self.__id}")
        print(f"Task title: {self.title}")
        print(f"Task description: {self.description}")
        print(f"Task status: {self.status}")
        