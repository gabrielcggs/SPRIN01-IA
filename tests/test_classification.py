from services.classification_service import ClassificationService


def test_classification():

    service = ClassificationService()

    result = service.classify(
        "Qual o custo da recarga?"
    )

    assert result == "billing"
