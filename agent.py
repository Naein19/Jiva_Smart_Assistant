from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RoomInputOptions
from livekit.plugins import google, noise_cancellation
from tools import *
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION

load_dotenv()

class Assistant(Agent):
    def __init__(self):
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            llm=google.beta.realtime.RealtimeModel(voice="Aoede", temperature=0.8),
            tools=[
                get_weather, search_web, send_email, ask_ai,
                control_app, read_screen, write_to_file, create_folder,
                open_whatsapp, send_whatsapp_message,get_day_info
            ],
        )

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession()
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )
    await ctx.connect()
    await session.generate_reply(instructions=SESSION_INSTRUCTION)

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

