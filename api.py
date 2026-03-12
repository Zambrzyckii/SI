import gymnasium as gym
from stable_baselines3 import PPO
import imageio
from fastapi import FastAPI
from fastapi.responses import FileResponse
from gifgen import record
app = FastAPI()


@app.get("/simulation")
def make_simualtion():
    name = "result.gif"
    record("model",name)
    return FileResponse(name,media_type="image/gif")
