import gymnasium as gym
import imageio
from stable_baselines3 import PPO

def record(model_path, name, wind_power = 0.0, turbulence_power = 0.0,gravity = -10.0):
    enable_wind = wind_power != 0 or turbulence_power != 0
    env = gym.make("LunarLander-v3", render_mode="rgb_array", enable_wind=enable_wind, wind_power = wind_power, turbulence_power = turbulence_power,gravity = gravity)
    obs,info = env.reset()
    mod = PPO.load(model_path)

    frames = []
    while True:
        action, _states = mod.predict(obs,deterministic=True)
        frames.append(env.render())
        obs, reward, terminated, truncated,info = env.step(action)
        if terminated or truncated:
            lastframe = frames[-1]
            for _ in range(60 ):
                frames.append(lastframe)
            break
    env.close()
    imageio.mimsave(name, frames, fps=30)

record("model", "model.gif")