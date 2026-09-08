
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorPopMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        # execute the next middleware (and the endpoint).
        response = await call_next(request)

        #if not ('errors' in request.session):
        #    request.session['errors'] = []

        # remove error from session (after generating page with), only if it's not a redirection or error.
        if response.status_code >= 200 and response.status_code < 300:
            request.session['errors'] = []

        return response


