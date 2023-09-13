from uagents import Agent, Context, Model
from aumanaque import Create_agent
from action import Action
# from goals import Goals
# from intentions import objetivo

class Message(Model):
    message: str
    
lamp = Create_agent.lamp()
action = Action()
  
@lamp.on_event('startup')
async def plan_event(ctx: Context):
    lamp.belief(ctx, 'initial_status', '01/04/2023')
    lamp.belief(ctx, 'horario_passado', 19)
    lamp.belief(ctx, 'local', 'quarto')
    lamp.belief(ctx, 'temperatura_diferente', 24)
    lamp.belief(ctx, 'lampada', 'ON')
    lamp.desire(ctx, 'regular_ambiente')
    # lamp.desire(ctx, 'regular_iluminacao')
    lamp.set_plan_library(ctx, 'regular_iluminacao', {'lampada': 'ON'}, ['desligar'])
    lamp.set_plan_library(ctx, 'regular_temperatura', {'temperatura_diferente': 24}, ['ajustar_temperatura'])
    lamp.set_plan_library(ctx, 'regular_ambiente', {'horario_passado': 19, 'local':'quarto'},['desligar','regular_temperatura'])
    
@lamp.on_interval(period=30.5)
async def plan_interval(ctx: Context):
    # action.ajustar_temperatura(ctx) if lamp.contexto(ctx, {"initial_status": "01/04/2023", "initial_": "01/04/2023"}) else False
    # action.ajustar_temperatura(ctx) if lamp.contexto(ctx, {"initial_status": "01/04/2023"}) else False
    lamp.update_intention(ctx)
    # action.ajustar(ctx) if lamp.contexto(ctx, {"initial_status": "01/04/2023"}) else False

@lamp.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    await ctx.send(sender, Message(message="Hello there alice."))
    
if __name__ == "__main__":
    lamp.run()
