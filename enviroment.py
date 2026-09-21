import gymnasium as gym
from gymnasium import spaces
import numpy as np

from robot import Robot
from mymathcalc import ray_segment_intersect, vector_subtract

class RobotEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(...)  # fill in shape once you pick your obs
        self.robot = Robot("Robo1")
        # wall/goal setup here

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.robot.reset()
        obs = self._get_obs()
        return obs, {}

    def step(self, action):
        self._apply_action(action)
        # advance physics with a fixed dt
        terminated = self._check_collision() or self._check_goal()
        reward = 0  # placeholder until Day 8
        obs = self._get_obs()
        return obs, reward, terminated, False, {}