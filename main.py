import ui

def main():
    while True:
        opcao = ui.menu_principal()
        if opcao == "1":
            ui.menu_usuarios()
        elif opcao == "2":
            ui.menu_projetos()
        elif opcao == "3":
            ui.menu_tarefas()
        elif opcao == "4":
            ui.menu_relatorios()
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
