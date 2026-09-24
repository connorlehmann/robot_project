from stable_baselines3.common.env_checker import check_env
from environment import RobotEnv

env = RobotEnv()
check_env(env, warn=True)
print("check_env passed")