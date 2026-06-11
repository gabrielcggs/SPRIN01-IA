# Chatbot GoodWe - Sprint 2

Projeto da Sprint 2 do EV Challenge 2026. O objetivo foi implementar um chatbot em Python para o contexto **ChargeGrid Intelligence**, relacionado a carregadores de veiculos eletricos da GoodWe em um condominio.

O chatbot usa um **system prompt** com informacoes simuladas sobre carregadores, consumo, custo, disponibilidade e risco de sobrecarga. Ele tambem guarda o historico da conversa para responder de forma mais coerente durante o dialogo.

## Integrantes

| Nome | RM |
|------|-----|
| Gabriel Camarosani Gouvea Goncalves da Silva | 569189 |
| Gustavo Lima Andrade Santos | 571709 |
| Lucas Seiji Hummel | 569673 |
| Pedro Souza Castro | 569311 |
| Bruno Yudi Moritaka Kanashiro | 571776 |

## Dependencias

- Python 3.10 ou superior
- Bibliotecas listadas em `requirements.txt`
- Chave de API do Gemini ou da OpenAI

Instalacao das dependencias:

```bash
pip install -r requirements.txt
```

## Variaveis de ambiente

As chaves de API nao devem ser colocadas diretamente no codigo.

Crie um arquivo `.env` na raiz do projeto, usando o arquivo `.env.example` como modelo:

```env
LLM_PROVIDER=gemini
GOOGLE_API_KEY=sua_chave_gemini_aqui
OPENAI_API_KEY=sua_chave_openai_aqui
GEMINI_MODEL=gemini-2.5-flash-lite
OPENAI_MODEL=gpt-4o-mini
```

Para usar Gemini, mantenha:

```env
LLM_PROVIDER=gemini
GOOGLE_API_KEY=sua_chave_gemini_aqui
```

Para usar OpenAI, altere para:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=sua_chave_openai_aqui
```

## Como executar

Na raiz do projeto, execute:

```bash
python src/main.py
```

Depois disso, digite as perguntas no terminal.

Comandos disponiveis:

- `sair`: encerra o chatbot
- `limpar`: apaga o historico da conversa atual

Tambem existe uma versao para Google Colab em:

```text
notebooks/chatbot_colab.ipynb
```

## Exemplos de uso

Exemplo 1:

```text
Usuario: Quanto gastei este mes em recarga?
Chatbot: O consumo total em junho/2026 foi de 847 kWh, com custo estimado de R$ 753,83.
```

Exemplo 2:

```text
Usuario: Qual carregador esta disponivel agora?
Chatbot: Os carregadores CG-01 e CG-04 estao disponiveis. O CG-02 esta em uso e o CG-03 esta em manutencao.
```

Exemplo 3:

```text
Usuario: Existe sobrecarga agora no condominio?
Chatbot: Nao existe sobrecarga no momento. A demanda atual e de 38 kW para um limite contratado de 50 kW.
```

## Testes

Os 5 casos de teste da Sprint 2 estao em:

```text
docs/testes/modelo_testes.md
```

Para executar os testes:

```bash
python src/run_tests.py
```

O resultado e salvo em:

```text
docs/testes/resultados_testes_sprint02.md
```

O relatorio registra:

- pergunta enviada
- resposta obtida
- avaliacao qualitativa: adequada, parcialmente adequada ou inadequada

## Estrutura do projeto

```text
SPRIN01-IA/
|-- src/
|   |-- main.py
|   |-- chatbot.py
|   |-- run_tests.py
|-- notebooks/
|   |-- chatbot_colab.ipynb
|-- docs/
|   |-- testes/
|       |-- modelo_testes.md
|       |-- resultados_testes_sprint02.md
|-- requirements.txt
|-- .env.example
|-- README.md
```

