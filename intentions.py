from uagents import Agent, Context, Model
class objetivo():
    @staticmethod
    def contexto(ctx: Context, *args):
        dicionario_context = {}
        dicionario_belief = {}
        dicionario_context = {item: arg[item] for arg in args for item in arg}        
        dicionario_belief = ctx.storage.all_belief()
        return all(chave in dicionario_belief and dicionario_belief[chave] == valor for chave, valor in dicionario_context.items())






























