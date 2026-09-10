
import html


def htmlSanitise(str_raw: str) -> str:
    """
    Sanitise input from user (prevent injection html).
    """
    output = html.escape(str_raw)
    return output