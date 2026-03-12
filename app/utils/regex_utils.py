import re

WHATSAPP_IMAGE_PATTERN = re.compile(
    r"(IMG|null)-(\d{8})-WA(\d+)\.jpg",
    re.IGNORECASE
)


def parse_whatsapp_filename(filename):
    """
    Extrae prefijo, fecha y número de un archivo WhatsApp.

    Ejemplo:
    IMG-20250219-WA0101.jpg
    -> ("IMG", "20250219", 101)
    """

    match = WHATSAPP_IMAGE_PATTERN.match(filename)

    if not match:
        return None

    prefix, date, number = match.groups()

    return prefix, date, int(number)