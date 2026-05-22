from services.classification_service import ClassificationService
from services.llm_service import LLMService

from utils.logger import salvar_log

from evaluation.report_generator import gerar_report
from evaluation.metrics import gerar_grafico


class ChatbotController:

    def __init__(self):

        self.classifier = ClassificationService()
        self.llm = LLMService()

        self.total_perguntas = 0
        self.total_reclamacoes = 0
        self.total_duvidas = 0
        self.total_elogios = 0

    def start(self):

        print("=== GoodWe Smart Assistant ===")

        while True:

            pergunta = input("\nDigite sua pergunta: ")

            if pergunta.lower() == "sair":

                print("Encerrando...")
                break

            salvar_log(f"Pergunta do usuário: {pergunta}")

            classificacao = self.classifier.classify(pergunta)

            # Corrige retorno string ou dict
            if isinstance(classificacao, dict):

                tipo = classificacao.get(
                    "tipo",
                    "desconhecido"
                )

            else:

                tipo = str(classificacao)

            self.total_perguntas += 1

            # Contadores
            if "reclam" in tipo.lower():

                self.total_reclamacoes += 1

            elif "duvida" in tipo.lower():

                self.total_duvidas += 1

            elif "elogio" in tipo.lower():

                self.total_elogios += 1

            resposta = self.llm.generate_response(pergunta)

            salvar_log(f"Classificação: {tipo}")

            salvar_log(
                f"Resposta gerada: {resposta}"
            )

            print("\n==================================\n")

            print(resposta)

            print("\n==================================")

        self.gerar_avaliacao_final()

    def gerar_avaliacao_final(self):

        report = f"""
RELATÓRIO FINAL

Total de perguntas: {self.total_perguntas}

Reclamações: {self.total_reclamacoes}
Dúvidas: {self.total_duvidas}
Elogios: {self.total_elogios}
"""

        gerar_report(report)

        dados = {

            "Reclamações":
                self.total_reclamacoes,

            "Dúvidas":
                self.total_duvidas,

            "Elogios":
                self.total_elogios
        }

        gerar_grafico(dados)

        salvar_log(
            "Relatório e gráfico gerados com sucesso."
        )