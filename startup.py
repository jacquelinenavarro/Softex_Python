# Ana precisa de um sistema para coordenar os membros(nome) da equipe e as tarefas (descricao) atribuídas a
# cada um deles. Neste sistema, cada membro da equipe pode ter várias tarefas atribuídas, mas uma tarefa
# específica está ligada apenas a um membro da equipe. Sugestão utilizar array e função.

class Equipe:
    def __init__(self):
        self.membros = {}  # Dicionário para armazenar membros e suas tarefas

    def adicionar_membro(self, membro_id, nome, cargo):
        self.membros[membro_id] = {"nome": nome, "cargo": cargo}

    def adicionar_tarefa(self, membro_id, descricao):
        if membro_id in self.membros:
            if "tarefas" not in self.membros[membro_id]:
                self.membros[membro_id]["tarefas"] = []
            self.membros[membro_id]["tarefas"].append(descricao)
        else:
            print(f"Membro com ID {membro_id} não encontrado.")

    def exibir_equipe(self):
        for membro_id, info in self.membros.items():
            nome = info["nome"]
            tarefas = ", ".join(info.get("tarefas", []))
            print(f"{nome} ({membro_id}): {tarefas}")

def main():
    equipe = Equipe()

    # Exemplo de adição de membros e tarefas
    equipe.adicionar_membro(1, "Ana", "Desenvolvedora")
    equipe.adicionar_membro(2, "Carlos", "Tester")
    equipe.adicionar_tarefa(1, "Desenvolver relatório")
    equipe.adicionar_tarefa(2, "Testar novo recurso")
    equipe.adicionar_tarefa(1, "Reunião com cliente")

    # Exibindo a equipe e suas tarefas
    equipe.exibir_equipe()

if __name__ == "__main__":
    main()
