from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from uagents.resolver import RulesBasedResolver
from aumanaque import Create_agent
from goals import Goals

class Message(Model):
    message: str
    
sleep = Create_agent.sleep()


@sleep.on_interval(period=30.5)
async def plan(ctx: Context):
    sleep.belief(ctx, 'desire_initial_status', "initial_status", '28/04/2023')
    
    await ctx.send(Create_agent.LAMP_ADDRESS, Message(message="Hello there bob."))


@sleep.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

if __name__ == "__main__":
    sleep.run()
