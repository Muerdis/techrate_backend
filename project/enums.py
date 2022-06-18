"""
Project enums
"""


class BlockchainType:  # pylint: disable=too-few-public-methods
    """
    Blockchain type
    """

    BSC = "BSC"
    ETHERIUM = "Etherium"

    CHOICES = (
        (BSC, "BSC"),
        (ETHERIUM, "Etherium"),
    )
