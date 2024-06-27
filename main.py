import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks

# openai_api_key = os.getenv("OPENAI_API_KEY")
# serper_api_key = os.getenv("SERPER_API_KEY")


class ResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = ResearchCrewAgents()
        self.tasks = ResearchCrewTasks()

    def run(self):
        # Initialize agents
        phd_university_finder = self.agents.phd_university_finder()
        phd_professor_finder = self.agents.phd_professor_finder()
        # writer = self.agents.writer()

        # Initialize tasks with respective agents
        find_universities_task = self.tasks.find_universities_task(phd_university_finder, self.inputs)
        find_professors_task = self.tasks.find_professors_task(phd_professor_finder, [find_universities_task])
        # writing_task = self.tasks.writing_task(writer, [find_professors_task])

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[phd_university_finder, phd_professor_finder],
            tasks=[find_universities_task, find_professors_task],
            verbose=True,
            process=Process.sequential
        )

        # Execute the crew to carry out the research project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the PhD Finder!")
    print("---------------------------------------")
    country = input("Please enter the country you wish to do your PhD: ")
    gpa = input("Please enter your GPA (out of 4.0): ")
    research_areas = input("What are the areas or focuses that you want to do your PhD in? ")

    inputs = f"PhD Country: {country}\nGPA: {gpa}\nResearch Areas: {research_areas}"
    research_crew = ResearchCrew(inputs)
    result = research_crew.run()

    print("\n\n##############################")
    print("## Here are the possible PhD Opportunities:")
    print("##############################\n")
    print(result)
