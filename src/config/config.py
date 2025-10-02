from src.model import Config
from src.model.llm_config import LLMConfig
from os import path

FILE_PATH = path.abspath(path.join(path.dirname(__file__), '..', '..', 'config', 'config.yaml'))

def load_config() -> Config:
    """Load configuration from a yaml file and parse it"""
    import yaml
    with open(FILE_PATH, 'r') as file:
        config_dict = yaml.safe_load(file)
    return Config(**config_dict)

def get_llm_config_by_name(name: str) -> LLMConfig:
    """Get LLM configuration by name"""
    config = load_config()
    for llm in config.llms:
        if llm.name == name:
            llm.host = f"{llm.url}:{llm.port}"
            return llm
    raise ValueError(f"LLM with name {name} not found")

def get_all_llm_configs() -> list[LLMConfig]:
    """Get all LLM configurations"""
    config = load_config()
    for llm in config.llms:
        llm.host = f"{llm.url}:{llm.port}"
    return config.llms
