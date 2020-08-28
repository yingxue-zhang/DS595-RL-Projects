#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gym
import numpy as np
import sys
from collections import defaultdict

from mc import *

"""
    This file includes unit test for mc.py
    You could test the correctness of your code by 
    typing 'nosetests -v mc_test.py' in the terminal
"""
env = gym.make('Blackjack-v0')

#---------------------------------------------------------------
def test_python_version():
    '''------On-policy Monte Carlo(50 points in total)------'''
    assert sys.version_info[0] == 3 # require python 3
    
#---------------------------------------------------------------
def test_initial_policy():
    '''initial_policy (2 points)'''
    state1 = (21, 10, True)
    action1 = initial_policy(state1)
    state2 = (18, 5, True)
    action2 = initial_policy(state2)
    
    assert np.allclose(action1,0)
    assert np.allclose(action2,1)
    
#---------------------------------------------------------------
def test_mc_prediction():
    '''mc_prediction (20 points)'''
    V_500k = mc_prediction(initial_policy, env, n_episodes=500000, gamma = 1.0)
    
    boundaries1 = [(18,4,False),(18,6,False),(18,8,False)]
    boundaries2 = [(18,4,True),(18,6,True),(18,8,True)]
    boundaries3 = [(20,4,False),(20,6,False),(20,8,False),(20,4,True),(20,6,True),(20,8,True)]

    
    assert len(V_500k) == 280
    for b in boundaries1:
        assert np.allclose(V_500k[b], -0.7, atol = 0.05)
    for b in boundaries2:
        assert np.allclose(V_500k[b], -0.4, atol = 0.1)
    for b in boundaries3:
        assert V_500k[b]>0.6
                     
#---------------------------------------------------------------
def test_epsilon_greedy():      
    '''epsilon_greedy (8 points)'''
    # just a test case, not related to blackjack
    Q = defaultdict(lambda: np.zeros(4))
    state = (14, 7, True)
    
    actions = []
    for _ in range(10000):
        action = epsilon_greedy(Q, state, 4,  epsilon=0.1)
        actions.append(action)
        
    assert np.allclose(1-np.count_nonzero(actions)/10000,0.925,atol=0.02)
    
#---------------------------------------------------------------
def test_mc_control_epsilon_greedy():
    '''mc_control_epsilon_greedy (20 points)'''
    boundaries_key = [(19,10,True),(19,4,True),(18,7,True),(17,9,True),(17,5,True),
             (17,8,False),(17,6,False),(15,6,False),(14,7,False)]
    boundaries_action = [0, 0, 0, 1, 1, 0, 0, 0, 1]
    
    count = 0
    for _ in range(2):
        Q_500k = mc_control_epsilon_greedy(env, n_episodes=1000000, gamma = 1.0, epsilon=0.1)
        policy = dict((k,np.argmax(v)) for k, v in Q_500k.items())
        print([policy[key] for key in boundaries_key])
        if [policy[key] for key in boundaries_key] == boundaries_action:
            count += 1
    
    
    assert len(Q_500k) == 280
    assert count >= 1 
