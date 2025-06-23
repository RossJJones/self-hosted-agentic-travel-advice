# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

expected_output = ""


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!" #Proven to give models better answers lol

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Task**: Develop a 7-Day Travel Itinerary
                **Description**: Expand the city guide into a full 7-day travel itinerary with detailed
                    per-day plans, including weaather forecasts, places to eat, packing suggestions, safety tips,
                    and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                    actual restaurants to go to all based on local security and safety advice. This itinerary should cover all aspects of the trip,
                    from arrival to departure, integrating the city guide information with practical travel logistics.

                **Parameters**:
                - City: {city}
                - Trip Dates: {travel_dates}
                - Travel Interests: {interests}

                **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=expected_output
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                **Task**: Identify the Best City for the Trip
                **Description**: Analyze and select the best city for the trip based on specific
                    criteria such as weather patterns, seasonal events and travel costs.
                    This task involves comparing multiple cities, considering factors like current weather
                    conditions, upcoming cultural or seasonal events, crime rates and overall travel expenses.
                    Your final answer must be a detailed report on the chosen city,
                    including actual flight costs, weather forecast, attractions and places to avoid due to high crime.

                **Parameters**:
                - Origin: {origin}
                - Cities: {cities}
                - Trip Dates: {travel_dates}
                - Travel Interests: {interests}

                **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=expected_output
        )

    def gather_city_info(self, agent, city, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                **Task**: Gather In-Depth City Guide Information
                **Description**: Compile an in-depth guide for the selected city, gathering information about
                    key attractions, local customs, special events and daily activity recommendations. 
                    This guide should provide a thorough overview of what the city has to offer, including
                    hidden gems, cultural hotspots, must-visit landmarks, weather forecasts and high-level costs.

                **Parameters**:
                - City: {city}
                - Trip Dates: {travel_dates}
                - Travel Interests: {interests}

                **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=expected_output
    )

    def gather_city_safety_info(self, agent, city, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                **Task**: Gather In-Depth City Safety Guide Information
                **Description**: Compile an in-depth security and safety guide for the selected city, gathering information about
                    Places to avoid, regular scams to look out for, common crimes and police recommendations. 
                    This guide should provide a thorough overview of how to stay completely safe in the city, including
                    scam attractions, safest taxi service, local police number and ways to ask for police in the local language.

                **Parameters**:
                - City: {city}
                - Trip Dates: {travel_dates}
                - Travel Interests: {interests}

                **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=expected_output
    )