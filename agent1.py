from uagents import Agent, Context, Model
from aumanaque import Create_agent
from goals import Goals
from intentions import objetivo

class Message(Model):
    message: str
    
lamp = Create_agent.lamp()
goal = Goals()
    
@lamp.on_interval(period=30.5)
async def plan_interval(ctx: Context):
    lamp.belief(ctx, 'initial_status', '01/04/2023')
    goal.intention_lamp() if objetivo.contexto(ctx, {"initial_status": "01/04/2023", "initial_": "01/04/2023"}) else False
    goal.intention_lamp() if objetivo.contexto(ctx, {"initial_status": "01/04/2023"}) else False

@lamp.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    # send the response
    await ctx.send(sender, Message(message="Hello there alice."))
    
if __name__ == "__main__":
    lamp.run()
