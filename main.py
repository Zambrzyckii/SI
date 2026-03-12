import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("LunarLander-v3", render_mode="human")
model = PPO.load("firstattempt.zip")
observation, info = env.reset()
print(env.observation_space)
print(env.action_space)
for _ in range(500):
    action, _states = model.predict(observation, deterministic=True)
    observation, reward, terminated, truncated, info = env.step(action)

    env.render()

    if terminated or truncated:
        env.reset()

env.close()