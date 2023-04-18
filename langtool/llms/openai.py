from langtool.llms.base import LLM
import openai
import enum

class Model(enum.Enum):
    GPT_4 = 'gpt-4'
    GPT_4_0314  = 'gpt-4-0314' 
    GPT_4_32K  = 'gpt-4-32k' 
    GPT_4_32K_0314  = 'gpt-4-32k-0314' 
    GPT_3_5_TURBO = 'gpt-3.5-turbo'
    GPT_3_5_TURBO_0301 = 'gpt-3.5-turbo-0301'

class Openai(LLM):
    def __init__(self, api_key:str, model:Model, system_prompt:str, temperature:float=0.1, frequency_penalty:float=0,):
        self.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.frequency_penalty = frequency_penalty

        openai.api_key = api_key

    def get_reply(self, message:str)->str:
        response = openai.ChatCompletion.create(
        model=self.model.value,
        messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": message},
            ],
        temperature=self.temperature,
        )
    
        return response['choices'][0]['message']['content'].strip().lower()