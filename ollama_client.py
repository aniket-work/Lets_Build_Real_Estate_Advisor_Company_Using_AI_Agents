from openai import OpenAI
from constants import OPENAI_CONFIG

def create_openai_client():
    return OpenAI(
        base_url=OPENAI_CONFIG['base_url'],
        api_key=OPENAI_CONFIG['api_key'],
        max_retries=OPENAI_CONFIG['max_retries']
    )