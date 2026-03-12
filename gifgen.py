import gymnasium as gym
import imageio
from stable_baselines3 import PPO
import io

def record(model_path, name, wind_power = 0.0, turbulence_power = 0.0,gravity = -10.0):
    enable_wind = wind_power != 0 or turbulence_power != 0
    env = gym.make("LunarLander-v3", render_mode="rgb_array", enable_wind=enable_wind, wind_power = wind_power, turbulence_power = turbulence_power,gravity = gravity)
    obs,info = env.reset()
    mod = PPO.load(model_path)

    total_reward = 0
    steps = 0
    frames = []
    while True:
        action, _states = mod.predict(obs,deterministic=True)
        frames.append(env.render())
        obs, reward, terminated, truncated,info = env.step(action)
        total_reward += reward
        steps += 1
        if terminated or truncated:
            lastframe = frames[-1]
            for _ in range(60 ):
                frames.append(lastframe)
            break
    env.close()
    out = io.BytesIO()
    imageio.mimsave(out, frames,format='GIF', fps=30)
    outbytes = out.getvalue()
    stats = {
        "score" : round(total_reward,3),
        "steps" : steps,
        "status" : "success" if total_reward > 200 else "failure" if total_reward < 0 else "landed"
    }
    return outbytes,stats
