from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from  typing import List

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
            verbose= True
        )
    @agent
    def competitive_intelligence_analyst(self) -> Agent:
        return Agent(
            config=self.agents_agents['competitive_intelligence_analyst'],
            vebrose = True
        )
    
    @agent
    def customer_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agents_agents['customer_insights_researcher'],
            vebrose = True
        )

    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agents_agents['product_strategy_advisor'],
            vebrose = True
        )

    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agents_agents['business_analyst'],
            vebrose = True
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_agents['market_research_task']
        )
    
    @task
    def competitive_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_agents['competitive_analysis_task']
        )

    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_agents['customer_insights_task']
        )

    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_agents['product_strategy_task']
        )

    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_analyst_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agent=self.agents,
            tasks=self.tasks,
            process=Process.Sequential,
            vebose=True,
        )
    



