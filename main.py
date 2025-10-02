from model import Task as tf # tf de tarefa

# Variáveis globais
id_cont = 0
tasks_list = []

def show_task(t_list: list, idx: int):
    """Show an individual task inside the list

    Args:
        t_list (list): task list
        idx (int): task index inside the list
    """    
    
    if 0 <= idx <= len(t_list):
        tf.get_task_info(t_list[idx])
    else:
        print("Index out of Bounds")
            
def show_all_tasks(t_list: list):
    """Display all the tasks inside the tasks list

    Args:
        tl (list): A list of tasks
    """
    for t in t_list:
        tf.get_task_info(t)

def remove_task(t_list: list, idx: int):
    """Remove uma tarefa da lista de tarefas

    Args:
        t_list (list): Lista de tarefas
        task_id (int): indice da lista que contem a tarefa
    """  
    
    if 0 <= idx <= len(t_list):
        t_list.pop(idx)      
    else: 
        print(f"Indice inválido para remoção: {idx}")          

def update_status(t_list: list, idx: int):
    """Muda o status da tarefa -> Incompleto para completo e vice-versa

    Args:
        t_list (list): Lista de tarefas
    """
    if 0 <= idx <= len(t_list):
        print("Tarefa encontrada")
        tf.change_status(t_list[idx])
    else:
        print("Err0: Índice inválido")

def update_task(t_list: list, idx: int):
    
    # Obtem id
    if 0 <= idx <= len(t_list):
        task = t_list[idx]
        
        print("Tarefa escolhida: ")
        tf.get_task_info(task)        
        tf.set_title(task, input("Insira um novo titulo: "))
        tf.set_description(task, input("Insira uma nova descrição: "))
        
    else:
        print("Err0: Tarefa não encontrada, insira um índice válido")
    

def add_task(t_list: list, title:str, description:str):
    """Adiciona uma nova tarefa à lista
    
    Args:
        t_list (list): task's list
        title (str): task's title
        description (str): task's description        
    """
    global id_cont
    new_task = tf(id_cont, title, description)
    id_cont += 1
    t_list.append(new_task)
    
def main():  # sourcery skip: extract-duplicate-method
    """Main function
    """
    
    #task1 = tf(0, "Estudar", "1 hora por dia pelo menos")       # id_table[0] = 0
    #task2 = tf(1, "Praticar culinária", "Aprender e praticar culinária. Importante para morar sozinho")    # id_table[1] = 1
    #task3 = tf(2, "Tirar Cochilo", "Cochilar por 10 min")        # id_table[2] = 2
    
    add_task(tasks_list, "Estudar", "1 hora por dia")   # id_table[0] = 0
    add_task(tasks_list, "academia", "treinar")         # id_table[1] = 1  #se remover esse: id_table[1] = 2 
    add_task(tasks_list, "jogar", "1 hora por dia")     # id_table[2] = 2
    add_task(tasks_list, "escutar musica", "No max 1 hora")     # id_table[3] = 3
    
    print("...............")    
    show_all_tasks(tasks_list)   
    
    print("...............Buscar tarefa 1 antes de remove-la")
    show_task(tasks_list, 1)
    
    remove_task(tasks_list, 1)
    
    print("...............Buscar tarefa 1 depois de remover-la")
    show_task(tasks_list, 1)
    
    print("............Exibir tudo")
    show_all_tasks(tasks_list)
    
    
if __name__ == "__main__":
    main()