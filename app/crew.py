from crewai import Crew
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()
        local_security_expert = agents.local_security_expert()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_safety_info = tasks.gather_city_safety_info(
            local_security_expert,
            self.cities,
            self.interests,
            self.date_range
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent,
                    city_selection_expert,
                    local_tour_guide,
                    local_security_expert
                    ],
            tasks=[plan_itinerary,
                   identify_city,
                   gather_city_info,
                   gather_city_safety_info
                   ],
            verbose=True,
        )

        result = crew.kickoff()
        return result
