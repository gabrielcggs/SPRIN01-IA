class LLMService:
    """
    Serviço responsável por processar solicitações do usuário
    e gerar respostas inteligentes para o assistente GoodWe.

    Estrutura preparada para futura integração com:
    - OpenAI
    - Ollama
    - Gemini
    - LangChain
    """

    def __init__(self):

        self.formas_pagamento = [
            "pagar",
            "pagamento",
            "formas de pagamento",
            "cartão",
            "cartao",
            "pix",
            "boleto",
            "credito",
            "débito",
            "debito",
            "como pagar",
            "como faço o pagamento",
            "paguei",
            "cobrança",
            "cobranca",
            "fatura"
        ]

        # =========================
        # PROBLEMAS TÉCNICOS
        # =========================

        self.problemas_tecnicos = [
            "quebrou",
            "erro",
            "falha",
            "travou",
            "bug",
            "não funciona",
            "nao funciona",
            "não liga",
            "nao liga",
            "não está ligando",
            "nao esta ligando",
            "parou de funcionar",
            "apagou",
            "desligou sozinho",
            "não responde",
            "nao responde",
            "defeito",
            "problema técnico",
            "problema tecnico"
        ]

        # =========================
        # CARREGAMENTO LENTO
        # =========================

        self.carregamento_lento = [
            "carregando devagar",
            "muito lento",
            "demora para carregar",
            "carregamento lento",
            "lentidão",
            "lentidao",
            "carrega pouco",
            "baixa velocidade"
        ]

        # =========================
        # SUPERAQUECIMENTO
        # =========================

        self.superaquecimento = [
            "esquentando",
            "muito quente",
            "superaquecimento",
            "super aquecimento",
            "temperatura alta",
            "aqueceu",
            "cheiro de queimado"
        ]

        # =========================
        # CONEXÃO / INTERNET
        # =========================

        self.conexao = [
            "wifi",
            "wi-fi",
            "internet",
            "sem conexão",
            "sem conexao",
            "offline",
            "não conecta",
            "nao conecta",
            "desconectado",
            "falha de conexão",
            "falha de conexao"
        ]

        # =========================
        # APLICATIVO
        # =========================

        self.aplicativo = [
            "app",
            "aplicativo",
            "não abre",
            "nao abre",
            "travando",
            "erro no app",
            "bug no app",
            "não sincroniza",
            "nao sincroniza"
        ]

        # =========================
        # ENERGIA SOLAR
        # =========================

        self.energia_solar = [
            "energia solar",
            "painel solar",
            "fotovoltaico",
            "placa solar",
            "solar",
            "geração solar",
            "geracao solar"
        ]

        # =========================
        # HORÁRIO DE PICO
        # =========================

        self.horario_pico = [
            "horário de pico",
            "horario de pico",
            "pico de energia",
            "tarifa alta",
            "economizar energia",
            "melhor horário",
            "melhor horario"
        ]

        # =========================
        # CUSTO / PAGAMENTO
        # =========================

        self.pagamento = [
            "custo",
            "custa",
            "valor",
            "preço",
            "preco",
            "pagamento",
            "cobrança",
            "cobranca",
            "fatura",
            "tarifa",
            "quanto vou pagar",
            "quanto custa carregar"
        ]

        # =========================
        # STATUS DO CARREGAMENTO
        # =========================

        self.status = [
            "status",
            "carregando",
            "terminou",
            "concluído",
            "concluido",
            "em andamento",
            "carregamento completo",
            "quanto falta"
        ]

        # =========================
        # TEMPO DE CARREGAMENTO
        # =========================

        self.tempo = [
            "tempo",
            "demora",
            "quanto tempo",
            "carregar completamente",
            "tempo estimado"
        ]

        # =========================
        # CONSUMO ENERGÉTICO
        # =========================

        self.consumo = [
            "consumo",
            "energia",
            "gasto energético",
            "gasto energetico",
            "quilowatt",
            "kwh",
            "uso de energia"
        ]

        # =========================
        # POTÊNCIA
        # =========================

        self.potencia = [
            "potência",
            "potencia",
            "kw",
            "amperagem",
            "voltagem",
            "220v",
            "110v",
            "capacidade"
        ]

        # =========================
        # COMPATIBILIDADE
        # =========================

        self.compatibilidade = [
            "compatível",
            "compativel",
            "compatibilidade",
            "funciona no meu carro",
            "serve no veículo",
            "serve no veiculo",
            "tipo de conector"
        ]

        # =========================
        # RESET
        # =========================

        self.reset = [
            "reset",
            "reiniciar",
            "reinicia",
            "resetar",
            "restaurar",
            "configuração de fábrica",
            "configuracao de fabrica"
        ]

        # =========================
        # MANUTENÇÃO
        # =========================

        self.manutencao = [
            "manutenção",
            "manutencao",
            "limpeza",
            "troca",
            "revisão",
            "revisao",
            "preventiva",
            "inspeção"
        ]

        # =========================
        # SEGURANÇA
        # =========================

        self.seguranca = [
            "segurança",
            "seguranca",
            "choque",
            "curto circuito",
            "curto-circuito",
            "risco elétrico",
            "risco eletrico",
            "proteção",
            "protecao"
        ]

        # =========================
        # FIRMWARE / ATUALIZAÇÃO
        # =========================

        self.firmware = [
            "firmware",
            "atualização",
            "atualizacao",
            "versão",
            "versao",
            "update",
            "software"
        ]

    # =====================================================
    # FUNÇÃO AUXILIAR
    # =====================================================

    def contains(self, text, keywords):

        return any(keyword in text for keyword in keywords)

    # =====================================================
    # PROCESSAMENTO PRINCIPAL
    # =====================================================

    def generate_response(self, prompt):

        text = prompt.lower().strip()

        # =====================================================
        # PROBLEMAS TÉCNICOS
        # =====================================================

        if self.contains(text, self.problemas_tecnicos):

            return """
Foi identificado um possível problema técnico no carregador.

Recomendações:
- Verifique a alimentação elétrica
- Confirme se o disjuntor está ativo
- Reinicie o equipamento
- Verifique cabos e conectores

Caso o problema continue, entre em contato
com o suporte técnico especializado.
"""

        # =====================================================
        # CARREGAMENTO LENTO
        # =====================================================

        elif self.contains(text, self.carregamento_lento):

            return """
O carregamento lento pode ocorrer devido a:

- Limitação de potência do carregador
- Instabilidade elétrica
- Configuração do veículo
- Horário de pico energético
- Temperatura elevada da bateria

Recomenda-se verificar a potência configurada
e utilizar horários de menor demanda elétrica.
"""

        # =====================================================
        # SUPERAQUECIMENTO
        # =====================================================

        elif self.contains(text, self.superaquecimento):

            return """
Foi identificado possível superaquecimento.

Por segurança:
- Interrompa o carregamento temporariamente
- Verifique ventilação do equipamento
- Evite exposição direta ao sol
- Confira cabos e conectores

Se houver cheiro de queimado ou aquecimento excessivo,
desconecte imediatamente o carregador.
"""

        # =====================================================
        # WI-FI / CONEXÃO
        # =====================================================

        elif self.contains(text, self.conexao):

            return """
O carregador aparenta estar com problemas de conexão.

Verifique:
- Sinal Wi-Fi disponível
- Senha da rede
- Distância do roteador
- Estabilidade da internet

Reiniciar o roteador e o carregador
pode resolver falhas temporárias.
"""

        # =====================================================
        # APLICATIVO
        # =====================================================

        elif self.contains(text, self.aplicativo):

            return """
Foi detectado um possível problema no aplicativo.

Recomendações:
- Atualize o aplicativo
- Faça login novamente
- Limpe o cache
- Reinicie o celular

Verifique também se o carregador
está corretamente sincronizado.
"""

        # =====================================================
        # ENERGIA SOLAR
        # =====================================================

        elif self.contains(text, self.energia_solar):

            return """
O carregador pode ser integrado
a sistemas de energia solar fotovoltaica.

Benefícios:
- Redução de custos
- Maior eficiência energética
- Sustentabilidade
- Uso inteligente da geração solar

O sistema pode priorizar energia solar
durante o carregamento do veículo.
"""

        # =====================================================
        # HORÁRIO DE PICO
        # =====================================================

        elif self.contains(text, self.horario_pico):

            return """
Evitar horários de pico pode reduzir significativamente
o custo do carregamento.

Recomendação:
- Priorize carregamentos noturnos
- Utilize agendamento inteligente
- Evite períodos de maior demanda elétrica

Isso melhora a eficiência energética
e reduz custos operacionais.
"""

        elif self.contains(text, self.formas_pagamento):

            return """
        As formas de pagamento disponíveis podem incluir:

        - PIX
        - Cartão de crédito
        - Cartão de débito
        - Carteira digital
        - Cobrança via aplicativo

        Verifique o aplicativo para visualizar
        os métodos habilitados.
        """

        # =====================================================
        # PAGAMENTO / CUSTO
        # =====================================================

        elif self.contains(text, self.pagamento):

            return """
O custo médio de carregamento varia conforme:

- Potência do carregador
- Tempo de utilização
- Tarifa energética local
- Tipo de carregamento

Em média:
- Carregadores residenciais:
  R$ 5 a R$ 20 por hora

- Carregadores rápidos:
  valores mais elevados devido à potência.
"""

        # =====================================================
        # STATUS
        # =====================================================

        elif self.contains(text, self.status):

            return """
O carregamento pode estar em um destes estados:

- Em carregamento
- Pausado
- Concluído
- Aguardando conexão
- Falha operacional

O aplicativo permite acompanhar
o status em tempo real.
"""

        # =====================================================
        # TEMPO
        # =====================================================

        elif self.contains(text, self.tempo):

            return """
O tempo médio de carregamento completo
pode variar entre 4 e 10 horas.

Isso depende de:
- Capacidade da bateria
- Potência do carregador
- Nível atual de carga
- Tipo de veículo
"""

        # =====================================================
        # CONSUMO
        # =====================================================

        elif self.contains(text, self.consumo):

            return """
O consumo energético depende principalmente de:

- Potência do carregador
- Tempo de carregamento
- Capacidade da bateria
- Eficiência energética do veículo

O monitoramento pode ser realizado
em tempo real pelo sistema.
"""

        # =====================================================
        # POTÊNCIA
        # =====================================================

        elif self.contains(text, self.potencia):

            return """
A potência do carregador influencia diretamente
na velocidade de carregamento.

Exemplos:
- 7 kW → carregamento residencial
- 22 kW → carregamento comercial
- 50 kW+ → carregamento rápido

Sempre verifique a compatibilidade elétrica.
"""

        # =====================================================
        # COMPATIBILIDADE
        # =====================================================

        elif self.contains(text, self.compatibilidade):

            return """
A compatibilidade depende de:

- Tipo de conector
- Potência suportada
- Modelo do veículo
- Padrão de carregamento

Consulte as especificações do veículo
e do carregador antes da instalação.
"""

        # =====================================================
        # RESET
        # =====================================================

        elif self.contains(text, self.reset):

            return """
Para reiniciar o carregador:

1. Desconecte da energia
2. Aguarde alguns segundos
3. Reconecte o equipamento
4. Verifique o status no aplicativo

O reset pode resolver falhas temporárias.
"""

        # =====================================================
        # MANUTENÇÃO
        # =====================================================

        elif self.contains(text, self.manutencao):

            return """
A manutenção preventiva é essencial
para garantir segurança e desempenho.

Recomendações:
- Verificar conectores
- Inspecionar cabos
- Limpar entradas de ventilação
- Atualizar firmware regularmente
"""

        # =====================================================
        # SEGURANÇA
        # =====================================================

        elif self.contains(text, self.seguranca):

            return """
Para garantir segurança elétrica:

- Utilize aterramento adequado
- Evite extensões improvisadas
- Não utilize cabos danificados
- Verifique proteção contra sobrecarga

Em caso de risco elétrico,
interrompa imediatamente o carregamento.
"""

        # =====================================================
        # FIRMWARE
        # =====================================================

        elif self.contains(text, self.firmware):

            return """
Manter o firmware atualizado melhora:

- Segurança
- Estabilidade
- Compatibilidade
- Eficiência energética

Verifique atualizações disponíveis
no aplicativo do carregador.
"""

        # =====================================================
        # FALLBACK INTELIGENTE
        # =====================================================

        return """
Não consegui identificar exatamente sua solicitação.

Você pode perguntar sobre:
- falhas técnicas
- custo do carregamento
- consumo energético
- potência
- energia solar
- aplicativo
- conexão Wi-Fi
- manutenção
- segurança elétrica
- compatibilidade do veículo

Tente descrever o problema com mais detalhes.
"""