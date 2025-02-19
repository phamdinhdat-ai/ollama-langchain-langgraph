# To install, run: pip install tavily-python
from tavily import TavilyClient

client = TavilyClient(api_key="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")

response = client.search(
    query="what is best football player in the world",
)

print(response)
