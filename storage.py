import json
import os

DATA_DIR = "data"

def _caminho_arquivo(nome):
    return os.path.join(DATA_DIR, nome)

def _carregar_json(nome):
    try:
        with open(_caminho_arquivo(nome), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def _salvar_json(nome, dados):
    with open(_caminho_arquivo(nome), "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Usuários
def carregar_usuarios():
    return _carregar_json("usuarios.json")

def salvar_usuario(usuario):
    usuarios = carregar_usuarios()
    usuarios.append(usuario)
    _salvar_json("usuarios.json", usuarios)

def salvar_usuarios(lista):
    _salvar_json("usuarios.json", lista)

# Projetos
def carregar_projetos():
    return _carregar_json("projetos.json")

def salvar_projeto(projeto):
    projetos = carregar_projetos()
    projetos.append(projeto)
    _salvar_json("projetos.json", projetos)

def salvar_projetos(lista):
    _salvar_json("projetos.json", lista)

# Tarefas
def carregar_tarefas():
    return _carregar_json("tarefas.json")

def salvar_tarefa(tarefa):
    tarefas = carregar_tarefas()
    tarefas.append(tarefa)
    _salvar_json("tarefas.json", tarefas)

def salvar_tarefas(lista):
    _salvar_json("tarefas.json", lista)
