from typing import List


def get_cors_domains(env: str) -> List:
    """Return list of allowed domains for CORS."""
    return ["*"]