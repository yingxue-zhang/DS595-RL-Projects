#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
from collections import defaultdict
#-------------------------------------------------------------------------
'''
    Monte-Carlo
    In this problem, you will implememnt an AI player for Blackjack.
    The main goal of this problem is to get familar with Monte-Carlo algorithm.
    You could test the correctness of your code
    by typing 'nosetests -v mc_test.py' in the terminal.

    You don't have to follow the comments to write your code. They are provided
    as hints in case you need.
'''
#-------------------------------------------------------------------------

def initial_policy(observation):
    """A policy that sticks if the player score is >= 20 and his otherwise

    Parameters:
    -----------
    observation

    Returns:
    --------
    action: 0 or 1
        0: STICK
        1: HIT
    """
    ############################
    # YOUR IMPLEMENTATION HERE #
    # get parameters from observation
    score, dealer_score, usable_ace = observation
    # action
    if score >= 20:
        action = 0
    else:
        action = 1
    ############################
    return action

def mc_prediction(policy, env, n_episodes, gamma = 1.0):
    """Given policy using sampling to calculate the value function
        by using Monte Carlo first visit algorithm.

    Parameters:
    -----------
    policy: function
        A function that maps an obversation to action probabilities
    env: function
        OpenAI gym environment
    n_episodes: int
        Number of episodes to sample
    gamma: float
        Gamma discount factor
    Returns:
    --------
    V: defaultdict(float)
        A dictionary that maps from state to value

    Note: at the begining of each episode, you need initialize the environment using env.reset()
    """
    # initialize empty dictionaries
    returns_sum = defaultdict(float)
    returns_count = defaultdict(float)
    # a nested dictionary that maps state -> value
    V = defaultdict(float)

    ############################
    # YOUR IMPLEMENTATION HERE #
    # loop each episode
    for i_episode in range(n_episodes):
        # initialize the episode
        state = env.reset()
        # generate empty episode list
        episode = []
        # loop until episode generation is done
        while True:

            # select an action
            action = policy(state)
            # return a reward and new state
            new_state, reward, done, _ = env.step(action)
            # append state, action, reward to episode
            episode.append((state, action, reward))
            # update state to new state
            state = new_state
            if done:
                break

        # loop for each step of episode, t = T-1, T-2,...,0
        G = 0
        states = set()
        for t in range(len(episode) - 1, -1, -1):
            state_t, action_t, reward_t = episode[t]
            # compute G
            G = gamma * G + reward_t
            # unless state_t appears in states
            if state_t not in states:
                states.add(state_t)
                # update return_count
                returns_count[state_t] += 1
                # update return_sum
                returns_sum[state_t] += G
                # calculate average return for this state over all sampled episodes
                V[state_t] = returns_sum[state_t] / returns_count[state_t]


    ############################

    return V

def epsilon_greedy(Q, state, nA, epsilon = 0.1):
    """Selects epsilon-greedy action for supplied state.

    Parameters:
    -----------
    Q: dict()
        A dictionary  that maps from state -> action-values,
        where Q[s][a] is the estimated action value corresponding to state s and action a.
    state: int
        current state
    nA: int
        Number of actions in the environment
    epsilon: float
        The probability to select a random action, range between 0 and 1

    Returns:
    --------
    action: int
        action based current state
    Hints:
    ------
    With probability (1 − epsilon) choose the greedy action.
    With probability epsilon choose an action at random.
    """
    ############################
    # YOUR IMPLEMENTATION HERE #
    greedy_action = -1
    greedy_q = - np.inf
    for action in range(nA):
        if Q[state][action] > greedy_q:
            greedy_action = action
            greedy_q = Q[state][action]
    random_action = random.randint(0, nA - 1)
    crit = random.random()
    if crit < 1 - epsilon:
        action = greedy_action
    else:
        action = random_action

    ############################
    return action

def mc_control_epsilon_greedy(env, n_episodes, gamma = 1.0, epsilon = 0.1):
    """Monte Carlo control with exploring starts.
        Find an optimal epsilon-greedy policy.

    Parameters:
    -----------
    env: function
        OpenAI gym environment
    n_episodes: int
        Number of episodes to sample
    gamma: float
        Gamma discount factor
    epsilon: float
        The probability to select a random action, range between 0 and 1
    Returns:
    --------
    Q: dict()
        A dictionary  that maps from state -> action-values,
        where Q[s][a] is the estimated action value corresponding to state s and action a.
    Hint:
    -----
    You could consider decaying epsilon, i.e. epsilon = epsilon-(0.1/n_episodes) during each episode
    and episode must > 0.
    """

    returns_sum = defaultdict(float)
    returns_count = defaultdict(float)
    # a nested dictionary that maps state -> (action -> action-value)
    # e.g. Q[state] = np.darrary(nA)
    Q = defaultdict(lambda: np.zeros(env.action_space.n))

    ############################
    # YOUR IMPLEMENTATION HERE #
    for i_episode in range(n_episodes):
        # define decaying epsilon
        epsilon = epsilon - (0.1/n_episodes)
        # initialize the episode
        state = env.reset()
        # generate empty episode list
        episode = []
        # loop until one episode generation is done
        while True:

            # get an action from epsilon greedy policy
            action = epsilon_greedy(Q, state, env.action_space.n, epsilon)
            # return a reward and new state
            new_state, reward, done, _ = env.step(action)
            # append state, action, reward to episode
            episode.append((state, action, reward))
            # update state to new state
            state = new_state
            if done:
                break

        # loop for each step of episode, t = T-1, T-2, ...,0
        G = 0
        states_actions = set()
        for t in range(len(episode) - 1, -1, -1):
            state_t, action_t, reward_t = episode[t]
            # compute G
            G = gamma * G + reward_t
            # unless the pair state_t, action_t appears in <state action> pair list
            if (state_t, action_t) not in states_actions:
                states_actions.add((state_t, action_t))
                # update return_count
                returns_count[state_t, action_t] += 1
                # update return_sum
                returns_sum[state_t, action_t] += G
                # calculate average return for this state over all sampled episodes
                Q[state_t][action_t] = returns_sum[state_t, action_t] / returns_count[state_t, action_t]
    return Q
