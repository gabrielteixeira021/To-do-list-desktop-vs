class Task:
    """"""
    # Atributos
    def __init__(self, __id, title, description) -> None:
        self.__id = __id
        self.title = title
        self.description = description
        
    def get_task_info(self):
        
        print(f"Task id: {self.__id}")
        print(f"Task title: {self.title}")
        print(f"Task description: {self.description}")
        