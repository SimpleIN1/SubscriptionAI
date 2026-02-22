from random import sample


SEQUENCE = "1234567890"


def generate_integer_sequence(k: int = 9):
    """

    :param k:
    :return:
    """

    return "".join(sample(SEQUENCE, k=k))
