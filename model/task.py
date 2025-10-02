class Task:
    """"""
    # Atributos
    def __init__(self, __id, title, description) -> None:
        self.__id = __id
        self.title = title
        self.description = description
        self.status = False
        
    def get_task_info(self):
        
        print(f"Task id: {self.__id}")
        print(f"Task title: {self.title}")
        print(f"Task description: {self.description}")
        print(f"Task status: {self.status}")
    
    def change_status(self):
        
        self.status = not self.status
        
    def get_id(self) -> int:
        return self.__id
    
    def get_title(self) -> str:
        return self.title

    def set_title(self, new_title):
        self.title = new_title
        
    def get_description(self) -> str:
        return self.description
    
    def set_description(self, new_desc):
        self.description = new_desc
    
    def get_status(self) -> bool:
        return self.status
    