import heapq
import time
import random

# essa classe vai representar um no
class Acao:
    def __init__(acao, descricao):
        acao.descricao = descricao
        acao.proxima = None

# Lista para guardar as ações feitas
class HistoricoAcoes:
    def iniciar(historico):
        historico.primeira = None

    def adicionar(historico, descricao):
        nova_acao = Acao(descricao)
        nova_acao.proxima = historico.primeira
        historico.primeira = nova_acao

    def exibir(historico):
        atual = historico.primeira
        while atual is not None:
            print(f" - {atual.descricao}")
            atual = atual.proxima

# Sistema principal para gerenciar as queimadas
class SistemaQueimadas:
    def iniciar(sistema):
        sistema.ocorrencias = []  # vai funcionar como fila de prioridade
        sistema.historico = {}    # guarda quantas vezes cada região foi atendida
        sistema.acoes = HistoricoAcoes()
        sistema.acoes.iniciar()

    def inserir_ocorrencia(sistema, regiao, severidade):
        # Como o heapq é min-heap, invertemos a severidade
        prioridade = -severidade
        timestamp = time.time()
        heapq.heappush(sistema.ocorrencias, (prioridade, timestamp, regiao))
        print(f"Nova ocorrência adicionada -> Região: {regiao} | Severidade: {severidade}")

    def atender_proxima(sistema):
        if not sistema.ocorrencias:
            print("Nenhuma ocorrência para atender no momento.")
            return

        prioridade, _, regiao = heapq.heappop(sistema.ocorrencias)
        severidade = -prioridade  # revertendo para o valor real

        descricao = f"Atendida ocorrência na região {regiao} com severidade {severidade}"
        print(descricao)
        sistema.acoes.adicionar(descricao)

        if regiao in sistema.historico:
            sistema.historico[regiao] += 1
        else:
            sistema.historico[regiao] = 1

    def gerar_relatorio(sistema):
        print("\n RELATÓRIO FINAL DE ATENDIMENTOS")
        if not sistema.historico:
            print("Nenhuma ocorrência foi atendida.")
            return
        for regiao, total in sistema.historico.items():
            print(f"Região: {regiao} | Total de atendimentos: {total}")

    def listar_acoes(sistema):
        print("\nHISTÓRICO DE AÇÕES")
        if sistema.acoes.primeira is None:
            print("Nenhuma ação realizada ainda.")
        else:
            sistema.acoes.exibir()

    def simular_chamadas(sistema, num_chamadas=5):
        regioes = ["Norte", "Sul", "Leste", "Oeste", "Centro"]
        severidade = 1

        for _ in range(num_chamadas):
            regiao = random.choice(regioes)
            sistema.inserir_ocorrencia(regiao, severidade)
            severidade += 1
            time.sleep(0.1)  # só pra parecer mais "de verdade"

# Código de execução
if __name__ == "__main__":
    sistema = SistemaQueimadas()
    sistema.iniciar()

    print("Simulando recebimento de chamadas de emergência...\n")
    sistema.simular_chamadas(7)

    print("\nAtendendo as ocorrências...\n")
    while sistema.ocorrencias:
        sistema.atender_proxima()

    sistema.listar_acoes()
    sistema.gerar_relatorio()
