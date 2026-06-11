from chatbot import resposta_local


def test_resposta_local_custo():
    resposta = resposta_local("Quanto gastei este mes em recarga?")

    assert "847" in resposta
    assert "753,83" in resposta
