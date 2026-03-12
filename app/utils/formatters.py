def format_bytes(size):

    mb = size / (1024 * 1024)
    gb = mb / 1024

    if gb >= 1:
        return f"{gb:.2f} GB"

    return f"{mb:.2f} MB"