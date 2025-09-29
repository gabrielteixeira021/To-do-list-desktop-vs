# Modelagem básica POO - Programação Orientada a Objetos

## Usuario

- contem lista de tarefas

## Tarefa

Atributos

- id (imutavel): int 
- Titulo: string
- Descrição: string 

Objeto/Variavel
lista_de_tarefas: serve para armazenar as tarefas(instâncias do obj tarefa) do usuario. Toda operação vai chamar e consultar essa lista.

Comportamentos

- Adicionar tarefa
- Listar tarefa
- Editar tarefa
- Remover tarefa

### Método: add_tasks:
    
    Descrição:
        Adiciona uma nova instância do objeto tarefa à lista.

    Algoritmo:
        1. Recebe a nova tarefa via parametro
        2. Chama a lista de tarefas
        3. realiza append pra adicionar a nova tarefa à lista

### Método: show_all_tasks

    Descrição:
        Exibe todas as tarefas presentes na lista

    Algoritmo:
        1. Recebe a lista de tarefas via parametros
        2. Mostra as tarefas utilizando um loop

Desenvolver funções base inicialmente na *main*.
