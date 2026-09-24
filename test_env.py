from environment import RobotEnv

env = RobotEnv()
obs, info = env.reset()
print("Initial obs:", obs)

actions_to_try = [1, 1, 1, 3, 3, 0]  # forward, forward, forward, turn_right, turn_right, stop

for action in actions_to_try:
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"action={action}  obs={obs}  terminated={terminated}")
    if terminated:
        print("Episode ended, resetting")
        obs, info = env.reset()