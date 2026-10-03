from crewai import Agent

database_query_optimizer_ai = Agent(
    role="Database Query Optimizer Ai",
    goal="Deliver high-precision autonomous Database Query Optimizer Ai operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
