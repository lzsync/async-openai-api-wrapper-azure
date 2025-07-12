import logging
import json
import azure.functions as func
from openai import APIStatusError

def function_decorator(http_function):
    async def wrapper(req):
        try:
            return http_response(await http_function(req))
        except APIStatusError as e:
            logging.error(e)
            return http_response(e.body, e.status_code)
        except Exception as e:
            logging.error(e)
            return http_response({ "message": "API error" }, 500)
    return wrapper

def http_response(body, status_code = 200):
    return func.HttpResponse(
        json.dumps(body),
        mimetype="application/json",
        status_code=status_code
        )