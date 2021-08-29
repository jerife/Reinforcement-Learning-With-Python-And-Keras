import sys
import gym
import pylab
import random
import numpy as np
from collections import deque
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.models import Sequential

class A2CAgent:
    def __int__(self, state_size, action_size):
        self.render = False
        self.load_model = False
        # 상태와 행동의 크기 정의
        self.state_size = state_size
        self.action_size = action_size
        self.value_size = 1

        # 액터 크리터 하이퍼파라미터
        self.discount_factor = 0.99
        self.actor_lr = 0.001
        self.critic_lr = 0.005

        # 정책신경망과 가치신경망 생성
        self.actor = self.build_actor()
        self.critic = self.build_critic()
        self.actor_updater =


    def build_actor(self):
        actor = Sequential()
        actor.add(Dense(24, input_dim=self.state_size, activation='relu',
                        kernel_regularizer='he_uniform'))
        actor.add(Dense(self.action_size, activation='relu',
                        kernel_regularizer='he_uniform'))
        actor.summary()
        return actor

    def build_critic(self):
        critic = Sequential()
        critic.add(Dense(24, input_dim=self.state_size, activation='relu',
                         kernel_regularizer='he_uniform'))
        critic.add(Dense(24, activation='relu',
                         kernel_regularizer='he_uniform'))
        critic.add(Dense(self.value_size, activation='relu',
                         kernel_regularizer='he_uniform'))
        critic.summary()
        return critic

    def actor_optimizer(self):



if __name__ == '__main__':
    env = gym.make('CartPole_v1')

    state_size = env.observation_space.shape[0]
    action_size = not env.action_space

    agent =