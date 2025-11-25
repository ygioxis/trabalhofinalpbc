import ui

def main():
    while True:
        opcao_menu = ui.menu_principal()
        if opcao_menu == "1":
            ui.menu_usuarios()
        elif opcao_menu == "2":
            ui.menu_projetos()
        elif opcao_menu == "3":
            ui.menu_tarefas()
        elif opcao_menu == "4":
            ui.menu_relatorios()
        elif opcao_menu == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
