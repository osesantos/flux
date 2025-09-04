from ollama import Client

# TODO: Change to use env or config file
#URL = "http://ollama-phi.ollama.svc.cluster.local:11435"

client = Client(
    host="http://localhost:11435"
)

MODEL = "phi3:mini"

async def classify(prompt: str) -> str:
    """
    A simple classifier service that classifies text into categories.
    Calls the phi3 model in ollama to classify the text.
    """
    if prompt is None or prompt.strip() == "":
        raise ValueError("Prompt must be specified")

    response = client.generate(model=MODEL,prompt=prompt)   

    return _clean_classification(response.response)

def _clean_classification(classification: str) -> str:
    """
    Cleans the classification string by removing unwanted characters.
    """
    return classification.lower().replace("'", "").replace('"', '').strip()

