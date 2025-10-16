import uuid
from datetime import datetime

def gerar_id(prefixo):
    return f"{prefixo}_{str(uuid.uuid4())[:8]}"

def validar_email(email):
    return "@" in email and "." in email

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_datas(inicio, fim):
    try:
        d1 = datetime.strptime(inicio, "%Y-%m-%d")
        d2 = datetime.strptime(fim, "%Y-%m-%d")
        return d1 <= d2
    except ValueError:
        return False

def hoje():
    return datetime.today().date()
