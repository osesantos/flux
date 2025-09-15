from src.model import Config
from src.model.llm_config import LLMConfig
from os import path

FILE_PATH = path.join(path.dirname(__file__), '..', '..', 'config', 'config.yaml')
FILE_PATH = path.abspath(FILE_PATH)

def LoadConfig() -> Config:
    """Load configuration from a yaml file and parse it"""
    import yaml
    with open(FILE_PATH, 'r') as file:
        config_dict = yaml.safe_load(file)
    return Config(**config_dict)

def GetLLMConfigByName(name: str) -> LLMConfig:
    """Get LLM configuration by name"""
    config = LoadConfig()
    for llm in config.llms:
        if llm.name == name:
            llm.host = f"{llm.host}:{llm.port}"
            return llm
    raise ValueError(f"LLM with name {name} not found")
