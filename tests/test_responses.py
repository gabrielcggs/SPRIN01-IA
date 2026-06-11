from chatbot import resposta_local


def test_resposta_local_sobrecarga():
    resposta = resposta_local("Existe sobrecarga energetica agora no condominio?")

    assert "38 kW" in resposta
    assert "50 kW" in resposta
    assert "Nao existe sobrecarga" in resposta
