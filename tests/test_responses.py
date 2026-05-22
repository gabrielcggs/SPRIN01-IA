from chatbot.response_generator import ResponseGenerator


def test_response():

    generator = ResponseGenerator()

    response = generator.generate("Teste")

    assert "Teste" in response
