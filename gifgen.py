import gymnasium as gym
import imageio
from stable_baselines3 import PPO

def record(model_path, name):
    env = gym.make("LunarLander-v3", render_mode="rgb_array")
    obs,info = env.reset()
    mod = PPO.load(model_path)

    frames = []
    for _ in range(500):
        action, _states = mod.predict(obs,deterministic=True)
        frames.append(env.render())
        obs, reward, terminated, truncated,info = env.step(action)
        if terminated or truncated:
            break
    env.close()
    imageio.mimsave(name, frames, fps=30)

record("model", "model.gif")