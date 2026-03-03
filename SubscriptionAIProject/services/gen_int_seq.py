from random import sample


SEQUENCE = "1234567890"


def generate_integer_sequence(k: int = 9) -> str:
    """
    Создание уникальной последовастельности, используя SEQUENCE
    :param k:
    :return: unique sequence
    """

    return "".join(sample(SEQUENCE, k=k))
