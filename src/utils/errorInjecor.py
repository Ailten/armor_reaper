from src.utils.errorView import ErrorView

# for inject error in session (and create as array if first).
# use for set error.
def injectError(session: dict[str, any], error: ErrorView):

    # inject error.
    if error.input_name == None:
        session['errors']['generic'].append(error.msg)
        return
    session['errors'][error.input_name] = error.msg

# clean last error.
# use at start of every end point.
def resetError(session: dict[str, any]):
    if session.get('is_page_reach', True):
        session['errors'] = {'generic': []}
        if 'dto_form' in session:  # remove dto form.
            del session['dto_form']

# use before redirect to another end-point.
def redirectError(session: dict[str, any]):
    session['is_page_reach'] = False

# use before generate a page jinja.
def reachThePage(session: dict[str, any]):
    session['is_page_reach'] = True


# ------>

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pydantic import BaseModel

# stock the DTO form.
def injectDtoForm(session: dict[str, any], dto: "BaseModel"):
    session['dto_form'] = vars(dto)