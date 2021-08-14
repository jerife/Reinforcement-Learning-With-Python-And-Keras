import tkinter as tk
from tkinter import Button
import time
import numpy as np
from PIL import ImageTk, Image
from environment_prac import GraphicDisplay, Env
import random

class ValueIteration:
    def __init__(self, env):
        self.env = env
        self.value_table = [[0.0] * env.width for _ in range(env.height)]
        self.discount_factor = 0.9

    def value_iteration(self):
        next_value_table = [[0.0] * env.width for _ in range(env.height)]

        for state in self.env.get_all_states():
            if state == [2,2]:
                next_value_table[state[0]][state[1]] = 0.0
                continue

            value_list = []

            for action in env.possible_actions:
                next_state = self.env.state_after_action(state, action)
                reward = self.env.get_reward(state, action)
                next_value = self.get_value(next_state)

                value = reward + self.discount_factor * next_value
                value_list.append(value)

            next_value_table[state[0]][state[1]] = round(max(value_list), 2)

        self.value_table = next_value_table

    def get_action(self, state):
        action_list = []
        max_value = -99999

        if state == [2, 2]:
            return []

        for action in self.env.possible_actions:

            next_state = self.env.state_after_action(state, action)
            reward = self.env.get_reward(state, action)
            next_value = self.get_value(next_state)
            value = (reward + self.discount_factor * next_value)

            if value > max_value:
                max_value = value
                action_list.clear()
                action_list.append(value)
            elif value == max_value:
                action_list.append(value)

            return action_list

    def get_value(self, state):
        return round(self.value_table[state[0]][state[1]], 2)

if __name__ == '__main__':
    env = Env()
    value_iteration = ValueIteration(env)

    for _ in range(10):
        print("Complete to update value_fn: {}".format(_))
        value_iteration.value_iteration()
        print("value table {}".format(_))
        for i in value_iteration.value_table:
            print(i)

        print(" ")

    print(value_iteration.get_action([3,2]))