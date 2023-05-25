from uagents.environment import Environment_agent_lamp, Environment_agent_sleep

ag_lamp = Environment_agent_lamp()
ag_sleep = Environment_agent_sleep()

class Goals(): #plan_library 
    def intention_lamp(self): # colocar o plano # nome do objetivo 
        # tem que chamar goals e rodar o plano com o mesmo nome da tabela/json 
        ag_lamp.action()
        
    def plan_sleep(self):
        ag_sleep.action()