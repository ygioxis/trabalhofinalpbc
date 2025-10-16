import utils
import storage

def criar_usuario(nome, email, perfil):
    return {
        "id": utils.gerar_id("u"),
        "nome": nome,
        "email": email,
        "perfil": perfil
    }

def validar_email_unico(email):
    usuarios = storage.carregar_usuarios()
    for u in usuarios:
        if u["email"] == email:
            return False
    return True

def criar_projeto(nome, descricao, inicio, fim):
    return {
        "id": utils.gerar_id("p"),
        "nome": nome,
        "descricao": descricao,
        "inicio": inicio,
        "fim": fim
    }

def validar_nome_projeto_unico(nome):
    projetos = storage.carregar_projetos()
    for p in projetos:
        if p["nome"].lower() == nome.lower():
            return False
    return True

def criar_tarefa(titulo, projeto_id, responsavel_id, status, prazo):
    return {
        "id": utils.gerar_id("t"),
        "titulo": titulo,
        "projeto_id": projeto_id,
        "responsavel_id": responsavel_id,
        "status": status,
        "prazo": prazo
    }
