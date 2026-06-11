from chatbot import ConversationManager


def test_historico_mantem_contexto():
    manager = ConversationManager(max_turns=1)

    manager.add_user_message("Qual carregador esta livre?")
    manager.add_assistant_message("CG-01 e CG-04 estao disponiveis.")

    historico = manager.get_messages()

    assert len(historico) == 2
    assert historico[0]["role"] == "user"
    assert historico[1]["role"] == "assistant"
