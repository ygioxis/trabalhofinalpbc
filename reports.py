import storage
import utils

def resumo_por_projeto():
    projetos = storage.carregar_projetos()
    tarefas = storage.carregar_tarefas()

    for p in projetos:
        tarefas_proj = [t for t in tarefas if t["projeto_id"] == p["id"]]
        total = len(tarefas_proj)
        concluidas = len([t for t in tarefas_proj if t["status"] == "concluida"])
        andamento = len([t for t in tarefas_proj if t["status"] == "andamento"])
        pendentes = len([t for t in tarefas_proj if t["status"] == "pendente"])
        perc_concluido = (concluidas / total * 100) if total > 0 else 0

        print(f"\nProjeto: {p['nome']}")
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

    for u in usuarios:
        concluidas = [
            t for t in tarefas
            if t["responsavel_id"] == u["id"]
            and t["status"] == "concluida"
            and inicio <= t["prazo"] <= fim
        ]
        print(f"{u['nome']} - {len(concluidas)} tarefas concluídas no período.")

def tarefas_atrasadas():
    hoje = utils.hoje()
    tarefas = storage.carregar_tarefas()
    atrasadas = [
        t for t in tarefas
        if t["status"] != "concluida" and utils.validar_data(t["prazo"])
        and t["prazo"] < str(hoje)
    ]

    print("\nTarefas atrasadas:")
    for t in atrasadas:
        print(f"{t['id']} - {t['titulo']} - Prazo: {t['prazo']} - Status: {t['status']}")
