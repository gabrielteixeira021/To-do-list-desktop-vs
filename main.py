from model import Task as tf # tf de tarefa

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
    
# Variável global
tasks_list = []

def main():
    """Main function
    """
    
    task1 = tf(1, "Estudar", "1 hora por dia pelo menos")
    task2 = tf(2, "Praticar culinária", "Aprender e praticar culinária. Importante para morar sozinho")
    task3 = tf(3, "Tirar Cochilo", "Cochilar por 10 min")
    
    tasks_list.append(task1)
    tasks_list.append(task2)
    tasks_list.append(task3)
    
    print("#### Exibindo todas as tarefas ####")
    
    show_all_tasks(tasks_list)
    
    print("#### Exibindo apenas uma tarefa ####")
    
    show_task(tasks_list, 3)
    
if __name__ == "__main__":
    main()