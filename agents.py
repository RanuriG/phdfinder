from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool, TXTSearchTool


class ResearchCrewAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool(website="https://www.findaphd.com")
        self.scrape_tool = ScrapeWebsiteTool()
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4", temperature=0.3)

    def phd_university_finder(self):
        # Detailed agent setup for the phd_university_finder
        return Agent(
            role='PhD Universities Finder',
            goal='A research assistant helping users find all universities that align with their research area and PhD goals.',
            backstory=(
        "With a deep understanding of research areas and universities across the country, I excel at "
        "finding all universities that match your research interests and potential PhD fit. "
        "I can search the web, filter results, and prioritize universities based on "
        "research reputation, rankings, and faculty expertise to help you find the "
        "perfect academic environment for your PhD journey."
    ),
            verbose=True,
            allow_delegation=False,
            tools=[self.serper, self.scrape_tool, self.web],
            llm=self.gpt3,
        )

    def phd_professor_finder(self):
        # Detailed agent setup for the phd_professor_finder
        return Agent(
            role='Professor and Topic Finder',
            goal='A research assistant who helps you identify professors with PhD topics whose research aligns with your PhD aspirations.',
            backstory=(
        "I'm your dedicated professor scouting companion. I'll leverage my web search skills and delve into all university websites, "
        "faculty databases, and research-oriented sources to discover professors whose expertise aligns with your research area. "
        "You find the professors and their topics and interests based on the universities provided by the PhD University Finder. "
        "I can analyze their publications and research projects to understand their focus and potential fit for your PhD goals. "
        "I can find the professors in universities that aligns with your research areas"
        "I guarantee to find the bestprofessors who share your research passion, who offer PhDs related to your interest area, and pave the way for a successful PhD experience."
        "I find the correct and accurate details, I recheck everything by myself so I won't make a mistake"
    ),
            tools=[self.serper, self.scrape_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    # def writer(self):
    #     # Detailed agent setup for the Writer
    #     return Agent(
    #         role='Master Storyteller and Technical Writer',
    #         goal='Integrate and articulate insights into a compelling narrative with precise citations.',
    #         backstory="As a celebrated author and journalist with over twenty years of experience crafting stories that captivate and inform, you possess a unique flair for making intricate information accessible and engaging. Your writing has graced the pages of major publications and influential blogs, where your ability to elucidate complex concepts in an engaging manner has won you numerous accolades. In this role, you are the final architect, molding the raw analytical content into a final piece that is not only informative but also profoundly impactful.",
    #         tools=[self.txt_tool],
    #         verbose=True,
    #         allow_delegation=False,
    #         llm=self.gpt3,
    #     )