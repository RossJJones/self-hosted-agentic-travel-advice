from crewai import Agent, LLM
from textwrap import dedent
from tools.math_tools import CalculationTools
from tools.search_tools import SearchTools


### Notes ###
# Agents should be results driven and have a clear goal in mind
# Role is their job title
# Goals should be actionable
# Backstory should be their CV/resume

class TravelAgents:
    def __init__(self):
        self.llm = LLM(
            model="hosted_vllm//models/meta-llama/Llama-3.1-8B-Instruct",
            api_base="http://vllm-models:8000/v1",
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("""
                             Expert in travel planning and logistics.
                             I have decades of experience making travel iteneraries.
                             """),
            goal=dedent("""
                        Create a 7-day travel itinerary with detailed per-day plans,
                        include budget, packing suggestions, things to do based on traveler interest and safety tips.
                        """),
            tools=[
                SearchTools(),
                CalculationTools(),
            ],
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("""
                             Expert at analyzing travel data to pick ideal destinations.
                             """),
            goal=dedent("""
                        Select best cities based on weather, season, prices and traveler interests.
                        """),
            tools=[
                SearchTools(),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("""
                             Knowledgeable local guide with extensive information about the city, it's attractions and customs.
                             """),
            goal=dedent("""
                        Provide the BEST insights about the selected city.
                        """),
            tools=[
                SearchTools(),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )
    
    def local_security_expert(self):
        return Agent(
            role="Local Security Expert",
            backstory=dedent("""
                             Expert in local security and has 10 year experience in how to stay safe in the city.
                             """),
            goal=dedent("""
                        Provide the BEST security advice about staying safe, places to avoid, local scams and safest places about the selected city.
                        """),
            tools=[
                SearchTools(),
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.llm,
        )