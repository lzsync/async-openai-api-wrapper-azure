from functools import cache
import azure.functions as func
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncAzureOpenAI
from config import Config
from api_utils import function_decorator

app = func.FunctionApp()

@app.function_name(name="chat_completion")
@app.route(route="chat-completion", methods=("POST",), auth_level=func.AuthLevel.ANONYMOUS)
@function_decorator
async def chat_completion(req):
    config = get_config()
    client = get_openai_client(config)

    user_input = req.get_json().get("input")

    messages = [{"role": "user", "content": user_input }]

    response = await client.chat.completions.create(model = config.LLM_DEPLOYMENT_NAME, messages = messages, temperature=0 )
    return { "result": response.choices[0].message.content }

@app.function_name(name="embeddings")
@app.route(route="embeddings", methods=("POST",), auth_level=func.AuthLevel.ANONYMOUS)
@function_decorator
async def embeddings(req):
    config = get_config()
    client = get_openai_client(config)

    user_input = req.get_json().get("input")

    response = await client.embeddings.create(model=config.EMBEDDING_DEPLOYMENT_NAME, input=user_input)
    return [data.embedding for data in response.data]

@app.route(route="azure-token", methods=("POST",), auth_level=func.AuthLevel.ANONYMOUS)
def azure_token(req):
    config = get_config()
    return get_token_provider(config)()

@cache
def get_config():
    return Config()

@cache
def get_openai_client(config):
    return AsyncAzureOpenAI(
            api_version=config.API_VERSION,
            azure_endpoint=config.ENDPOINT,
            azure_ad_token_provider=get_token_provider(config),
            max_retries=config.MAX_RETRIES,
            timeout=config.TIMEOUT_SECONDS)

@cache
def get_token_provider(config):
    return get_bearer_token_provider(
        DefaultAzureCredential(), config.DEFAULT_CRED )
