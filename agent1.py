from uagents import Agent, Context, Model
from aumanaque import Create_agent
from action import Action

class Message(Model):
    message: str
    
agent1 = Create_agent.agent1()
action = Action()
  
@agent1.on_event('startup')
async def plan_event(ctx: Context):
    agent1.belief(ctx, 'initial_status', '01/04/2023')
    agent1.belief(ctx, 'horario_passado', 19)
    agent1.belief(ctx, 'local', 'quarto')
    agent1.belief(ctx, 'temperatura_diferente', 24)
    agent1.set_plan_library(ctx, 'regular_iluminacao', {'local': 'quarto'}, ['desligar'])
    agent1.set_plan_library(ctx, 'regular_temperatura', {'temperatura_diferente': 24}, ['ajustar_temperatura'])
    agent1.set_plan_library(ctx, 'regular_ambiente', {'horario_passado': 19, 'local':'quarto'}, ['regular_iluminacao','regular_temperatura'])
    agent1.desire(ctx, 'regular_ambiente')
    
@agent1.on_interval(period=30.5)
async def plan_interval(ctx: Context):
    agent1.update_intention(ctx)
    action.ajustar(ctx) if agent1.contexto(ctx, {"initial_status": "01/04/2023"}) else False
    await ctx.send(Create_agent.AGENTE1_ADDRESS, Message(message="Hello there Agent2."))

@agent1.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    await ctx.send(sender, Message(message="Hello there agent."))
    
if __name__ == "__main__":
    agent1.run()
