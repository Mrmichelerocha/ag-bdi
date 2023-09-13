# AÇÔES DISPONÍVEIS #
# Cada função/método corresponde a uma ação (por momento apenas simulada)

class Action:
    def ajustar_temperatura(self, ctx):
        ctx.storage.set_belief("aiai", "ai")
        print("###> temperatura ajustada <### ")
        
    def ajustar(self, ctx):
        ctx.storage.set_belief("temperatura_diferente", 24)
        print("###> temperatura ajustada <### ")

    def desligar(self, ctx):
        # ctx.storage.set_belief("temperatura_diferente", 18)
        print("###> desligado <### ")