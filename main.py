from model import Task as tf # tf de tarefa

# Variáveis globais
id_cont = 0
tasks_list = []
id_table = []

def show_task(t_list: list, idx: int):
    """Show an individual task inside the list

    Args:
        t_list (list): task list
        idx (int): task index inside the list
    """
    if 0 <= idx < len(t_list):
        tf.get_task_info(t_list[idx])
    else: 
        print("Index out of Bounds")
            
def show_all_tasks(t_list: list):
    """Display all the tasks inside the tasks list

    Args:
        tl (list): A list of tasks
    """
    for x in range(len(t_list)):
        tf.get_task_info(t_list[x])

def create_new_task() -> tf:
    """Create and return a new Task instance    
    """
    
    global id_cont
    status = False
    title = input("Insira um título para a tarefa: ")
    description = input("Insira uma descrição: ")        
    task_id = id_cont
    id_cont += 1
    return tf(task_id, title, description, status)

def remove_task(t_list: list, task_idx: int):
    """Remove uma tarefa da lista de tarefas

    Args:
        t_list (list): Lista de tarefas
        task_id (int): indice da lista que contem a tarefa
    """  
    t_list.remove(id_table[task_idx])
    if id_table[task_idx + 1]:
        id_table[task_idx] = id_table[task_idx + 1]
    


def add_new_task(t_list: list, title:str, description:str):
    """Adiciona uma nova tarefa à lista
    
    Args:
        t_list (list): task's list
        title (str): task's title
        description (str): task's description        
    """
    global id_cont
    new_task = tf(id_cont, title, description, status=False)
    id_cont += 1
    id_table.append(id_cont)
    t_list.append(new_task)
    
def test_add_new_task(t_list: list, ts_obj: tf):
    """Adiciona uma nova tarefa à lista
    
    Args:
        t_list (list): task's list
        title (str): task's title
        description (str): task's description        
    """
    t_list.append(ts_obj)

def main():
    """Main function
    """
    
    task1 = tf(0, "Estudar", "1 hora por dia pelo menos", False)       # id_table[0] = 0
    task2 = tf(1, "Praticar culinária", "Aprender e praticar culinária. Importante para morar sozinho", False)    # id_table[1] = 1
    task3 = tf(2, "Tirar Cochilo", "Cochilar por 10 min", False)        # id_table[2] = 2
    
    #print("### Testando função de adicionar tarefas")
    #test_add_new_task(tasks_list, create_new_task())
    #show_all_tasks(tasks_list)
    
    #test_add_new_task(tasks_list, create_new_task())
    #show_all_tasks(tasks_list)
    
if __name__ == "__main__":
    main()