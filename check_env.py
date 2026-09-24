from environment import RobotEnv

env = RobotEnv()
obs, info = env.reset()
print("Initial obs:", obs)

for i in range(200):
    obs, reward, terminated, truncated, info = env.step(1)  # forward
    print(f"step={i}  obs={obs}  terminated={terminated}")
    if terminated:
        print("Hit something, stopping")
        break