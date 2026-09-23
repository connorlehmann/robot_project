import gymnasium as gym
from gymnasium import spaces
import numpy as np
import math

from robot import Robot
from mymathcalc import ray_segment_intersect, vector_subtract

"""Closest Wall Calculation Function
"""
def closest_hit(robot_position, ray_direction, walls):
    #Cast ray_direction from the robot and return the distance to the
    #nearest wall it actually hits, or None if it hits nothing."""
    hits = [ray_segment_intersect(robot_position, ray_direction, wall_q, wall_s)
            for wall_q, wall_s in walls]
    valid_hits = [h for h in hits if h is not None]
    return min(valid_hits) if valid_hits else None


"""RL MODEL
"""
class RobotEnv(gym.Env):
    def __init__(self):
        super().__init__()

        """Observation and Action Space Setup
        """
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(...)  # fill in shape once you pick your obs



        """Robot Setup
        """
        self.robot1 = Robot("Robo1")



        """Wall and Goal Setup
        """
        self.inner_walls = {"top": 300,
               "bottom": 400,
               "right": 500,
               "left": 400}
        
        self.wall_start1 = (400, 300)
        self.wall_end1 = (500, 300)
        self.wall_start2 = (500, 300)
        self.wall_end2 = (500, 400)
        self.wall_start3 = (500, 400)
        self.wall_end3 = (400, 400)
        self.wall_start4 = (400, 400)
        self.wall_end4 = (400, 300)

        #S  (segment direction MUST go start -> end for u to range over [0, 1])
        self.wall_direction1 = vector_subtract(self.wall_end1, self.wall_start1)
        self.wall_direction2 = vector_subtract(self.wall_end2, self.wall_start2)
        self.wall_direction3 = vector_subtract(self.wall_end3, self.wall_start3)
        self.wall_direction4 = vector_subtract(self.wall_end4, self.wall_start4)

        self.walls = [
            (self.wall_start1, self.wall_direction1),
            (self.wall_start2, self.wall_direction2),
            (self.wall_start3, self.wall_direction3),
            (self.wall_start4, self.wall_direction4),
        ]

        self.goal = (477.5, 377.5)



        """Time/dt Setup
        """
        self.dt = 1/60


    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        """Resetting Robot and Returning Observation
        """
        self.robot1.reset()
        obs = self._get_obs()
        return obs, {}


    def _get_obs(self):

        """Finding Robot Position
        """
        robot_position = (self.robot1.pos_x, self.robot1.pos_y)



        """Ray Direction and Distance Calulations
        """
        ray_direction_front = (math.cos(self.robot1.theta), -math.sin(self.robot1.theta))
        ray_direction_left = (math.cos(self.robot1.theta + math.pi/2), -math.sin(self.robot1.theta + math.pi/2))
        ray_direction_right = (math.cos(self.robot1.theta - math.pi/2), -math.sin(self.robot1.theta - math.pi/2))
        ray_direction_back = (math.cos(self.robot1.theta + math.pi), -math.sin(self.robot1.theta + math.pi))

        front_dist = closest_hit(robot_position, ray_direction_front, self.walls)
        left_dist = closest_hit(robot_position, ray_direction_left, self.walls)
        right_dist = closest_hit(robot_position, ray_direction_right, self.walls)
        back_dist = closest_hit(robot_position, ray_direction_back, self.walls)



        """Treating None Types
        """
        maximum = 150
        if front_dist is None:
            front_dist = maximum
        if left_dist is None:
            left_dist = maximum
        if back_dist is None:
            back_dist = maximum
        if right_dist is None:
            right_dist = maximum

        scaled_front = front_dist/maximum
        scaled_back = back_dist/maximum
        scaled_left = left_dist/maximum
        scaled_right = right_dist/maximum



        """Finding Dx and Dy
        """
        dx = self.goal[0] - robot_position[0]
        dy = self.goal[1] - robot_position[1]



        """Angle to Goal
        """
        world_angle = math.atan2(-dy, dx)
        proper_turn_angle = world_angle - self.robot1.theta
        normalized_turn_angle =(proper_turn_angle + math.pi) % (2 * math.pi) - math.pi





    def _apply_action(self):


    def _check_collision(self):

        """Collision Check
        """
        if self.robot1.collision_check(10, top_wall=self.inner_walls["top"], bottom_wall=self.inner_walls["bottom"], left_wall=self.inner_walls["left"], right_wall=self.inner_walls["right"]):
            return True
        else:
            return False


    def _check_goal(self):

        """Goal Check
        """
        if  470 < self.robot1.pos_x < 485 and 370 < self.robot1.pos_y < 385:
            return True
        else:
            return False

    
    def step(self, action):
        self._apply_action(action)

        """Finding Robot Position
        """
        robot_position = (self.robot1.pos_x, self.robot1.pos_y)



        """Ray Direction and Distance Calulations
        """
        ray_direction_front = (math.cos(self.robot1.theta), -math.sin(self.robot1.theta))
        ray_direction_left = (math.cos(self.robot1.theta + math.pi/2), -math.sin(self.robot1.theta + math.pi/2))
        ray_direction_right = (math.cos(self.robot1.theta - math.pi/2), -math.sin(self.robot1.theta - math.pi/2))
        ray_direction_back = (math.cos(self.robot1.theta + math.pi), -math.sin(self.robot1.theta + math.pi))

        self.front_dist = closest_hit(robot_position, ray_direction_front, self.walls)
        self.left_dist = closest_hit(robot_position, ray_direction_left, self.walls)
        self.right_dist = closest_hit(robot_position, ray_direction_right, self.walls)
        self.back_dist = closest_hit(robot_position, ray_direction_back, self.walls)



        """Checking and Determining Speed
        """
        self.robot1.speed_check()
        self.robot1.total_velocity()      



        """Checking Robot Position and Next Move
        """
        self.robot1.boundaries_check(right_dist=self.right_dist, left_dist=self.left_dist, top_dist=self.front_dist, bottom_dist=self.back_dist)
        next_distance = self.robot1.predict_dist_moved(dt=self.dt)



        """Determining if next move is possible
        """
        if self.robot1.velo > 0:
            # moving forward
            if self.front_dist is None or self.front_dist > next_distance:
                self.robot1.pos_update(self.dt)

        elif self.robot1.velo < 0:
            # moving backward
            if self.back_dist is None or self.back_dist > next_distance:
                self.robot1.pos_update(self.dt)



        """Checking Terminated and Returning Step Info
        """
        terminated = self._check_collision() or self._check_goal()
        reward = 0  # placeholder until Day 8
        obs = self._get_obs()
        return obs, reward, terminated, False, {}