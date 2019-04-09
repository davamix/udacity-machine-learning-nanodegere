import numpy as np
import sys
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.alpha = 0.01
        self.gamma = 1.0

    def epsilon_greedy_probs(self, state, i_episode, eps=None):
        epsilon = 1.0 / i_episode
        
        if eps is not None:
            epsilon = eps
        
        policy_s = np.ones(self.nA) * epsilon / self.nA
        policy_s[np.argmax(self.Q[state])] = 1 - epsilon + (epsilon / self.nA)
        return policy_s
    
    def select_action(self, state, policy):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment
        - policy: 1D numpy array with policy.shape equal to the number of states

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        return np.random.choice(np.arange(self.nA), p=policy)

    def step(self, state, action, reward, next_state, done, policy):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        - policy: 1D numpy array with policy.shape equal to the number of states
        """
        self.Q[state][action] = self.Q[state][action] + (self.alpha * (reward + (self.gamma * np.dot(self.Q[next_state], policy)) - self.Q[state][action]))