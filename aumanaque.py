from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from uagents.resolver import RulesBasedResolver

class Create_agent():  

    AGENTE1_ADDRESS = "agent1q0f3l47jc7nwp6u6tem9g9nwpd2qnl7a379aznwntpeqxxr5hks3zxazuse"
    AGENTE2_ADDRESS = "agent1qws0tpmufe40gw6j02unxflftzl8uy56045kku5z9huafhyef3fy7v0h7mt"
    
    resolve=RulesBasedResolver(
        {
            AGENTE1_ADDRESS: "http://127.0.0.1:8020/submit",
            AGENTE2_ADDRESS: "http://127.0.0.1:8021/submit",
        }
    )
    
    def agent1():   
        agent1 = Agent(
            name="agent1",
            port=8020,
            seed="agent1 secret phrase",
            resolve= Create_agent.resolve,
        )
        
        fund_agent_if_low(agent1.wallet.address())
        
        return agent1
        
    def agent2():
        agent2 = Agent(
            name="agent2",
            port=8021,
            seed="agent2 secret phrase",
            resolve= Create_agent.resolve,
        )
        
        fund_agent_if_low(agent2.wallet.address())
        
        return agent2
    