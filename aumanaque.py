from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from uagents.resolver import RulesBasedResolver

class Create_agent():  

    LAMP_ADDRESS = "agent1q0f3l47jc7nwp6u6tem9g9nwpd2qnl7a379aznwntpeqxxr5hks3zxazuse"
    SLEEP_ADDRESS = "agent1qws0tpmufe40gw6j02unxflftzl8uy56045kku5z9huafhyef3fy7v0h7mt"
    
    resolve=RulesBasedResolver(
        {
            LAMP_ADDRESS: "http://127.0.0.1:8020/submit",
            SLEEP_ADDRESS: "http://127.0.0.1:8021/submit",
        }
    )
    
    def lamp():   
        lamp = Agent(
            name="lamp",
            port=8020,
            seed="lamp secret phrase",
            resolve= Create_agent.resolve,
        )
        
        fund_agent_if_low(lamp.wallet.address())
        
        return lamp
        
    def sleep():
        sleep = Agent(
            name="sleep",
            port=8021,
            seed="sleep secret phrase",
            resolve= Create_agent.resolve,
        )
        
        fund_agent_if_low(sleep.wallet.address())
        
        return sleep
    