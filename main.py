import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("LunarLander-v3", render_mode="human")
model = PPO.load("model.zip")
observation, info = env.reset()
print(env.observation_space)
print(env.action_space)
for _ in range(5000):
    action, _states = model.predict(observation, deterministic=True)
    observation, reward, terminated, truncated, info = env.step(action)

    env.render()

    if terminated or truncated:
        env.reset()

env.close()