import models
import storage
import utils

# === USUÁRIOS ===

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    perfil = input("Perfil (admin/user): ")

    if not nome.strip():
        print("Nome não pode ser vazio.")
        return

    if not utils.validar_email(email):
        print("Email inválido.")
        return

    if not models.validar_email_unico(email):
        print("Email já cadastrado.")
        return

    usuario = models.criar_usuario(nome, email, perfil)
    storage.salvar_usuario(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    usuarios = storage.carregar_usuarios()
    for u in usuarios:
        print(f"{u['id']} - {u['nome']} - {u['email']} ({u['perfil']})")

def buscar_usuario():
    termo = input("Digite nome ou email: ").lower()
    encontrados = [u for u in storage.carregar_usuarios()
                   if termo in u['nome'].lower() or termo in u['email'].lower()]
    for u in encontrados:
        print(f"{u['id']} - {u['nome']} - {u['email']} ({u['perfil']})")

def atualizar_usuario():
    listar_usuarios()
    uid = input("ID do usuário a atualizar: ")
    usuarios = storage.carregar_usuarios()
    for u in usuarios:
        if u["id"] == uid:
            nome = input(f"Novo nome ({u['nome']}): ") or u['nome']
            email = input(f"Novo email ({u['email']}): ") or u['email']
            perfil = input(f"Novo perfil ({u['perfil']}): ") or u['perfil']

            if email != u["email"] and not models.validar_email_unico(email):
                print("Email já existe.")
                return

            u.update({"nome": nome, "email": email, "perfil": perfil})
            storage.salvar_usuarios(usuarios)
            print("Usuário atualizado.")
            return
    print("Usuário não encontrado.")

def remover_usuario():
    listar_usuarios()
    uid = input("ID do usuário a remover: ")
    usuarios = storage.carregar_usuarios()
    usuarios = [u for u in usuarios if u["id"] != uid]
    storage.salvar_usuarios(usuarios)
    print("Usuário removido.")


# === PROJETOS ===

def cadastrar_projeto():
    nome = input("Nome do projeto: ")
    descricao = input("Descrição: ")
    inicio = input("Data de início (YYYY-MM-DD): ")
    fim = input("Data de fim (YYYY-MM-DD): ")

    if not utils.validar_datas(inicio, fim):
        print("Datas inválidas.")
        return

    if not models.validar_nome_projeto_unico(nome):
        print("Nome de projeto já existe.")
        return

    projeto = models.criar_projeto(nome, descricao, inicio, fim)
    storage.salvar_projeto(projeto)
    print("Projeto cadastrado.")

def listar_projetos():
    for p in storage.carregar_projetos():
        print(f"{p['id']} - {p['nome']} ({p['inicio']} a {p['fim']})")

def buscar_projeto():
    termo = input("Digite nome do projeto: ").lower()
    for p in storage.carregar_projetos():
        if termo in p["nome"].lower():
            print(f"{p['id']} - {p['nome']} ({p['inicio']} a {p['fim']})")

def atualizar_projeto():
    listar_projetos()
    pid = input("ID do projeto: ")
    projetos = storage.carregar_projetos()
    for p in projetos:
        if p["id"] == pid:
            nome = input(f"Novo nome ({p['nome']}): ") or p['nome']
            descricao = input(f"Nova descrição ({p['descricao']}): ") or p['descricao']
            inicio = input(f"Nova data de início ({p['inicio']}): ") or p['inicio']
            fim = input(f"Nova data de fim ({p['fim']}): ") or p['fim']

            if not utils.validar_datas(inicio, fim):
                print("Datas inválidas.")
                return

            p.update({"nome": nome, "descricao": descricao, "inicio": inicio, "fim": fim})
            storage.salvar_projetos(projetos)
            print("Projeto atualizado.")
            return
    print("Projeto não encontrado.")

def remover_projeto():
    listar_projetos()
    pid = input("ID do projeto a remover: ")
    projetos = storage.carregar_projetos()
    projetos = [p for p in projetos if p["id"] != pid]
    storage.salvar_projetos(projetos)
    print("Projeto removido.")


# === TAREFAS ===

def cadastrar_tarefa():
    titulo = input("Título da tarefa: ")
    listar_projetos()
    projeto_id = input("ID do projeto: ")
    listar_usuarios()
    responsavel_id = input("ID do responsável: ")
    status = "pendente"
    prazo = input("Prazo (YYYY-MM-DD): ")

    if not utils.validar_data(prazo):
        print("Data inválida.")
        return

    tarefa = models.criar_tarefa(titulo, projeto_id, responsavel_id, status, prazo)
    storage.salvar_tarefa(tarefa)
    print("Tarefa cadastrada.")

def listar_tarefas():
    for t in storage.carregar_tarefas():
        print(f"{t['id']} - {t['titulo']} - {t['status']} - Prazo: {t['prazo']}")

def listar_tarefas_por_projeto():
    listar_projetos()
    pid = input("ID do projeto: ")
    tarefas = storage.carregar_tarefas()
    for t in tarefas:
        if t["projeto_id"] == pid:
            print(f"{t['id']} - {t['titulo']} - {t['status']} - Prazo: {t['prazo']}")

def listar_tarefas_por_responsavel():
    listar_usuarios()
    uid = input("ID do responsável: ")
    tarefas = storage.carregar_tarefas()
    for t in tarefas:
        if t["responsavel_id"] == uid:
            print(f"{t['id']} - {t['titulo']} - {t['status']} - Prazo: {t['prazo']}")

def listar_tarefas_por_status():
    status = input("Status (pendente/andamento/concluida): ")
    tarefas = storage.carregar_tarefas()
    for t in tarefas:
        if t["status"] == status:
            print(f"{t['id']} - {t['titulo']} - {t['status']} - Prazo: {t['prazo']}")

def atualizar_tarefa():
    listar_tarefas()
    tid = input("ID da tarefa: ")
    tarefas = storage.carregar_tarefas()
    for t in tarefas:
        if t["id"] == tid:
            titulo = input(f"Novo título ({t['titulo']}): ") or t['titulo']
            listar_projetos()
            projeto_id = input(f"Novo projeto ({t['projeto_id']}): ") or t['projeto_id']
            listar_usuarios()
            responsavel_id = input(f"Novo responsável ({t['responsavel_id']}): ") or t['responsavel_id']
            status = input(f"Novo status ({t['status']}): ") or t['status']
            prazo = input(f"Novo prazo ({t['prazo']}): ") or t['prazo']

            if not utils.validar_data(prazo):
                print("Data inválida.")
                return

            t.update({
                "titulo": titulo,
                "projeto_id": projeto_id,
                "responsavel_id": responsavel_id,
                "status": status,
                "prazo": prazo
            })
            storage.salvar_tarefas(tarefas)
            print("Tarefa atualizada.")
            return
    print("Tarefa não encontrada.")

def concluir_tarefa():
    listar_tarefas()
    tid = input("ID da tarefa a concluir: ")
    tarefas = storage.carregar_tarefas()
    for t in tarefas:
        if t["id"] == tid:
            t["status"] = "concluida"
            storage.salvar_tarefas(tarefas)
            print("Tarefa concluída.")
            return
    print("Tarefa não encontrada.")

def reabrir_tarefa():
    listar_tarefas()
    tid = input("ID da tarefa a reabrir: ")
    tarefas = storage.carregar_tarefas()
    for t in tarefas:
        if t["id"] == tid:
            t["status"] = "pendente"
            storage.salvar_tarefas(tarefas)
            print("Tarefa reaberta.")
            return
    print("Tarefa não encontrada.")

def remover_tarefa():
    listar_tarefas()
    tid = input("ID da tarefa a remover: ")
    tarefas = storage.carregar_tarefas()
    tarefas = [t for t in tarefas if t["id"] != tid]
    storage.salvar_tarefas(tarefas)
    print("Tarefa removida.")
