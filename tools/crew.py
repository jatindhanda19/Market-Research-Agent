from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from  typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, SeleniumScrapingTool
from dotenv import load_dotenv

load_dotenv()

web_search_tool = SerperDevTool()
web_scraping_tool = ScrapeWebsiteTool()
Selenium_scraping_tool = SeleniumScrapingTool()

toolkit = [web_search_tool, web_scraping_tool, Selenium_scraping_tool]

@CrewBase
class MarketResearchCrew():
    agents: List[BaseAgent]
    tasks: List[Task]

    agents_agents = "agents/agents.yaml"
    tasks_agents = "agents/tasks.yaml"


    @agent 
    def market_research_specialist(self) -> Agent:
        return Agent(
            config= self.agents_agents['market_research_specialist'],
            verbose= True,
            tools = toolkit
        )
    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_agents['competitive_intelligence_analyst'],
            vebrose = True,
            tools = toolkit
            )
    
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_agents['customer_insights_researcher'],
            vebrose = True,
            tools = toolkit
        )

    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_agents['product_strategy_advisor'],
            vebrose = True,
            tools = toolkit
        )

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_agents['business_analyst'],
            vebrose = True,
            tools = toolkit
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_agents['market_research_task']
        )
    
    @task
    def competitive_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_agents['competitive_analysis_task'],
            context=[self.market_research_task()]
        )

    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_agents['customer_insights_task'],
            context=[self.market_research_task(),
                     self.competitive_analysis_task()]
        )

    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_agents['product_strategy_task'],
            context=[self.market_research_task(),
                    self.competitive_analysis_task(),
                    self.customer_insights_task()]
        )

    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_analyst_task'],
            context=[self.market_research_task(),
                    self.competitive_analysis_task(),
                    self.customer_insights_task(),
                    self.product_strategy_task()]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agent=self.agents,
            tasks=self.tasks,
            process=Process.Sequential,
            vebose=True,
        )
    



