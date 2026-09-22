
import html


# not use (currently).
def htmlSanitise(str_raw: str) -> str:
    """
    Sanitise input from user (prevent injection html).
    """
    output = html.escape(str_raw)
    return output

def isContainsSpecialChars(str_raw: str, chars: list[str]) -> bool:
    for c in chars:
        if c in str_raw:
            return True
    return False