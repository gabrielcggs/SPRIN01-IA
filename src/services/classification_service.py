class ClassificationService:

    def classify(self, text):

        texto = text.lower()

        reclamacoes = [
            "erro",
            "falha",
            "problema",
            "nao liga",
            "não liga",
            "quebrou",
            "parou",
            "defeito"
        ]

        duvidas = [
            "preco",
            "preço",
            "quanto",
            "valor",
            "pagamento",
            "custo",
            "como funciona"
        ]

        elogios = [
            "gostei",
            "excelente",
            "otimo",
            "ótimo",
            "bom",
            "parabens",
            "parabéns"
        ]

        for palavra in reclamacoes:

            if palavra in texto:

                return "reclamacao"

        for palavra in duvidas:

            if palavra in texto:

                return "duvida"

        for palavra in elogios:

            if palavra in texto:

                return "elogio"

        return "duvida"