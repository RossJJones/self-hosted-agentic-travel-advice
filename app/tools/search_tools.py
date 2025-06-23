import os
from crewai.tools import BaseTool
from exa_py import Exa
import os

exa_api_key = os.getenv("EXA_API_KEY")

class SearchTools(BaseTool):
  name: str = "search_and_get_contents_tool"
  description: str = "Exa internet search and get contents"
  
  def _run(self, question: str) -> str:
      """Tool using Exa's Python SDK to run semantic search and internet search and return result highlights."""

      exa = Exa(exa_api_key)

      response = exa.search_and_contents(
          question,
          type="neural",
          num_results=3,
          highlights=True
      )

      parsedResult = ''.join([f'<Title id={idx}>{eachResult.title}</Title> <URL id={idx}>{eachResult.url}</URL> <Highlight id={idx}>{"".join(eachResult.highlights)}</Highlight>' for (idx, eachResult) in enumerate(response.results)])

      return parsedResult