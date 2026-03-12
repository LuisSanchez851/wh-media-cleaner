import re

PATTERN = re.compile(r"(IMG|null)-(\d{8})-WA(\d+)\.jpg", re.IGNORECASE)

def filter_by_range(files, desde, hasta):

    m1 = PATTERN.match(desde)
    m2 = PATTERN.match(hasta)

    if not m1 or not m2:
        raise ValueError("Formato incorrecto")

    _, fecha, n1 = m1.groups()
    _, _, n2 = m2.groups()

    n1 = int(n1)
    n2 = int(n2)

    result = []

    for f in files:
        m = PATTERN.match(f.name)
        if m:
            _, f_fecha, numero = m.groups()
            numero = int(numero)

            if f_fecha == fecha and n1 <= numero <= n2:
                result.append(f)

    return result