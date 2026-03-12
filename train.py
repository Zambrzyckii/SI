import gym
import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("LunarLander-v3")

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=500000)
model.save("model")
