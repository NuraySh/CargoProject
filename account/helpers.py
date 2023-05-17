from django.utils.crypto import get_random_string


def id_gen():
    return get_random_string(8, allowed_chars="0123456789")
