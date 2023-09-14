from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from uagents.resolver import RulesBasedResolver
from aumanaque import Create_agent

class Message(Model):
    message: str
    
agent2 = Create_agent.agent2()


@agent2.on_interval(period=30.5)
async def plan_interval(ctx: Context):
    print("I joined the network")


@agent2.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    agent2.run()
