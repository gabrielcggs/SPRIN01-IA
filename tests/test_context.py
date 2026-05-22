from chatbot.context_manager import ContextManager


def test_context():

    manager = ContextManager()

    context = manager.build_context(
        "teste",
        "general",
        []
    )

    assert "teste" in context
