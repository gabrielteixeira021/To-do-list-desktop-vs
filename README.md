# Modelagem básica POO - Programação Orientada a Objetos

## Usuario

- contem lista de tarefas

## Tarefa

Atributos

- id (imutável): int
- Titulo: string
- Descrição: string (opcional)
- Status: Boolean (completo | Não completo)

Objeto/Variavel
lista_de_tarefas: serve para armazenar as tarefas(instâncias do obj tarefa) do usuario. Toda operação vai chamar e consultar essa lista.

Comportamentos do sistema

- Adicionar tarefa
- Listar tarefa
- Editar tarefa
- Remover tarefa

### Método: add_task

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
    
### Método: remove_task

    Descrição: 
        Remove uma tarefa da lista 

    Algoritmo: 
        1. User entra com o id
        2. utiliza um metodo para remover da lista
        3. Atualizar o dicionário de índices

### Método: update_task

    Descrição: 
        Método para realizar a operação de alteração de dados de determinada tarefa.
        Para se alterar a tarefa é necessário o ID da Tarefa e a Lista onde está a tarefa.
    
    Algoritmo:
    1. Sistema Pergunta o ID da tarefa a ser Atualizada
    2. Usuario Insere o ID
    3. Sistema Realiza a Busca do ID e Verifica se é valido (ID Inexistente, Fora de escopo e etc...)
    4. Sistema Retorna Resultado:
        ### Sistema Encontra Tarefa.

        4.1.1 Sistema Informa que encontrou a tarefa e pede as novas informações
        4.1.2 Usuario Insere as Novas Informações
        4.1.3 Sistema Salva as novas informações na Lista.
        
        ### Sistema Não Encontra Tarefa.
        
        4.2.1 Sistema Informa que não encontrou tarefa e retorna o erro informando o usuario.

### Método: update_status
    
    Descrição:
        Método para realizar a operação de conclusão de uma tarefa escolhida pelo usuario.
        Para se alterar a tarefa é necessário o ID da Tarefa e a Lista onde está a tarefa.

    Algoritmo:
    1. Sistema Pergunta o ID da tarefa a ser marcada como concluida.
    2. Usuario Insere o ID da tarefa
    3. Sistema Realiza a Busca do ID e Verifica se é valido (ID Inexistente, Fora de escopo e etc...)
        4. Sistema Retorna Resultado:
        
        ### Sistema Encontra Tarefa.
        4.2.1 Sistema Informa que marcou a tarefa como concluida.

        ### Sistema Não Encontra Tarefa.
        
        4.2.1 Sistema Informa que não encontrou tarefa e retorna o erro informando o usuario.    

funções base serão inicialmente desenvolvidas na *main*.
