import gymnasium as gym
from stable_baselines3 import PPO
import imageio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from gifgen import record
app = FastAPI()


@app.get("/simulation")
def make_simualtion(wind: float = 0.0, turbulence: float = 0.0,gravity: float = -10.0):
    name = "result.gif"
    record("model",name,wind_power = wind, turbulence_power = turbulence,gravity = gravity)
    return FileResponse(name,media_type="image/gif")
