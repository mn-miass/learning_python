def reverse_str(str_a) -> str:
    reverse = ""
    size = len(str_a) - 1
    while size >= 0:
        reverse += str_a[size]
        size -= 1
    return reverse
