from stable_baselines3 import PPO

from stable_baselines3 import PPO
from environment import RobotEnv

env = RobotEnv()

model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_robot_tensorboard/")
model.learn(total_timesteps=200000)

model.save("robot_policy")