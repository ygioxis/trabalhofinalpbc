import storage
import utils
from datetime import datetime

def resumo_por_projeto():
    projetos = storage.carregar_projetos()
    tarefas = storage.carregar_tarefas()

    for p in projetos:
        tarefas_proj = [t for t in tarefas if t.get("projeto_id") == p.get("id")]
        total = len(tarefas_proj)
        concluidas = len([t for t in tarefas_proj if t.get("status","").lower() == "concluida"])
        andamento = len([t for t in tarefas_proj if t.get("status","").lower() == "andamento"])
        pendentes = len([t for t in tarefas_proj if t.get("status","").lower() == "pendente"])
        perc_concluido = (concluidas / total * 100) if total > 0 else 0

        print(f"\nProjeto: {p.get('nome')}")
        print(f"  Total: {total}")
        print(f"  Pendentes: {pendentes}")
        print(f"  Em andamento: {andamento}")
        print(f"  Concluídas: {concluidas}")
        print(f"  % Concluído: {perc_concluido:.2f}%")

def produtividade_por_usuario():
    usuarios = storage.carregar_usuarios()
    tarefas = storage.carregar_tarefas()
    inicio = input("Data início (YYYY-MM-DD): ")
    fim = input("Data fim (YYYY-MM-DD): ")

    if not (utils.validar_data(inicio) and utils.validar_data(fim)):
        print("Datas inválidas. Use o formato YYYY-MM-DD.")
        return

    d_inicio = datetime.strptime(inicio, "%Y-%m-%d").date()
    d_fim = datetime.strptime(fim, "%Y-%m-%d").date()

    for u in usuarios:
        concluidas = [
            t for t in tarefas
            if t.get("responsavel_id") == u.get("id")
            and t.get("status","").lower() == "concluida"
            and utils.validar_data(t.get("prazo",""))
            and d_inicio <= datetime.strptime(t.get("prazo"), "%Y-%m-%d").date() <= d_fim
        ]
        print(f"{u.get('nome')} - {len(concluidas)} tarefas concluídas no período.")

def tarefas_atrasadas():
    hoje = utils.hoje()
    tarefas = storage.carregar_tarefas()
    atrasadas = [
        t for t in tarefas
        if t.get("status","").lower() != "concluida"
        and utils.validar_data(t.get("prazo",""))
        and datetime.strptime(t.get("prazo"), "%Y-%m-%d").date() < hoje
    ]

    print("\nTarefas atrasadas:")
    for t in atrasadas:
        print(f"{t.get('id')} - {t.get('titulo')} - Prazo: {t.get('prazo')} - Status: {t.get('status')}")
