import services
import reports

def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Gerenciar Usuários")
    print("2 - Gerenciar Projetos")
    print("3 - Gerenciar Tarefas")
    print("4 - Relatórios")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def menu_usuarios():
    while True:
        print("\n--- Usuários ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar por nome/email")
        print("4 - Atualizar")
        print("5 - Remover")
        print("0 - Voltar")
        opc = input("Opção: ")

        if opc == "1":
            services.cadastrar_usuario()
        elif opc == "2":
            services.listar_usuarios()
        elif opc == "3":
            services.buscar_usuario()
        elif opc == "4":
            services.atualizar_usuario()
        elif opc == "5":
            services.remover_usuario()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_projetos():
    while True:
        print("\n--- Projetos ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar por nome")
        print("4 - Atualizar")
        print("5 - Remover")
        print("0 - Voltar")
        opc = input("Opção: ")

        if opc == "1":
            services.cadastrar_projeto()
        elif opc == "2":
            services.listar_projetos()
        elif opc == "3":
            services.buscar_projeto()
        elif opc == "4":
            services.atualizar_projeto()
        elif opc == "5":
            services.remover_projeto()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_tarefas():
    while True:
        print("\n--- Tarefas ---")
        print("1 - Cadastrar")
        print("2 - Listar todas")
        print("3 - Listar por projeto")
        print("4 - Listar por responsável")
        print("5 - Listar por status")
        print("6 - Atualizar")
        print("7 - Concluir")
        print("8 - Reabrir")
        print("9 - Remover")
        print("0 - Voltar")
        opc = input("Opção: ")

        if opc == "1":
            services.cadastrar_tarefa()
        elif opc == "2":
            services.listar_tarefas()
        elif opc == "3":
            services.listar_tarefas_por_projeto()
        elif opc == "4":
            services.listar_tarefas_por_responsavel()
        elif opc == "5":
            services.listar_tarefas_por_status()
        elif opc == "6":
            services.atualizar_tarefa()
        elif opc == "7":
            services.concluir_tarefa()
        elif opc == "8":
            services.reabrir_tarefa()
        elif opc == "9":
            services.remover_tarefa()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def menu_relatorios():
    print("\n--- RELATÓRIOS ---")
    print("1 - Resumo por Projeto")
    print("2 - Produtividade por Usuário")
    print("3 - Tarefas Atrasadas")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        reports.resumo_por_projeto()
    elif opc == "2":
        reports.produtividade_por_usuario()
    elif opc == "3":
        reports.tarefas_atrasadas()
    else:
        print("Opção inválida.")
    
