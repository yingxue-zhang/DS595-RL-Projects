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
    observation:
    Returns:
    --------
    action: 0 or 1
        0: STICK
        1: HIT
    """
    ############################
    # YOUR IMPLEMENTATION HERE #
    # get parameters from observation

    # action

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
    """
    # initialize empty dictionaries
    returns_sum = defaultdict(float)
    returns_count = defaultdict(float)
    # a nested dictionary that maps state -> value
    V = defaultdict(float)
    
    ############################
    # YOUR IMPLEMENTATION HERE #
    # loop each episode

        # initialize the episode

        # generate empty episode list

        # loop until episode generation is done


            # select an action

            # return a reward and new state

            # append state, action, reward to episode

            # update state to new state

            
            

        # loop for each step of episode, t = T-1, T-2,...,0

            # compute G

            # unless state_t appears in states
            
                # update return_count
                
                # update return_sum

                # calculate average return for this state over all sampled episodes



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

        # define decaying epsilon



        # initialize the episode

        # generate empty episode list

        # loop until one episode generation is done


            # get an action from epsilon greedy policy

            # return a reward and new state

            # append state, action, reward to episode

            # update state to new state

            
        
        # loop for each step of episode, t = T-1, T-2, ...,0
        
            # compute G
            
            # unless the pair state_t, action_t appears in <state action> pair list
            
                # update return_count
                
                # update return_sum

                # calculate average return for this state over all sampled episodes
        
    return Q
