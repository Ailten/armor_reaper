

# for inject error in session (and create as array if first).
# use for set error.
def injectError(session: dict[str, any], error):
    if not 'errors' in session:
        session['errors'] = [error]
        return
    session['errors'].append(error)

# clean last error.
# use at start of every end point.
def resetError(session: dict[str, any]):
    if session.get('is_page_reach', True):
        session['errors'] = []

# use before redirect to another end-point.
def redirectError(session: dict[str, any]):
    session['is_page_reach'] = False

# use before generate a page jinja.
def reachThePage(session: dict[str, any]):
    session['is_page_reach'] = True