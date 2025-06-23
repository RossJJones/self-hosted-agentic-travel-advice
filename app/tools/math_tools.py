from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class CalculationInputs(BaseModel):
    operation: str = Field(..., description="The mathematical operation to preform")

class CalculationTools(BaseTool):
    name: str = "calculator"
    description: str = "Performs a specified mathematical operation.S"
    args_schema: Type[BaseModel] = CalculationInputs

    def _run(self, operation):
        """
        Performs a specified mathematical operation.

        Parameters:
        - operation (str): a string representing a mathematical operation (e.g. "10 + 5").

        Returns:
        - A string representation of the calculation result.
        """
        try:
            return f"The result of {operation} is {eval(operation)}"
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"