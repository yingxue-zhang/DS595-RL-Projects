#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gym
import numpy as np
import sys
from collections import defaultdict
from collections import Counter

from td import *
"""
    This file includes unit test for td.py
    You could test the correctness of your code by 
    typing 'nosetests -v td_test.py' in the terminal
"""

env = gym.make('CliffWalking-v0')
#---------------------------------------------------------------
def test_python_version():
    '''------Temporal Difference(50 points in total)------'''
    
    assert sys.version_info[0] == 3 # require python 3
    
#---------------------------------------------------------------
def test_epsilon_greedy():      
    '''epsilon_greedy (0 point)'''
    Q = defaultdict(lambda: np.zeros(4))
    state = 5
    
    actions = []
    for _ in range(10000):
        action = epsilon_greedy(Q, state, 4,  epsilon=0.1)
        actions.append(action)
        
    assert np.allclose(1-np.count_nonzero(actions)/10000,0.925,atol=0.02)
    
#---------------------------------------------------------------
def test_sarsa():
    '''SARSA (25 points)'''
    test_policy = np.array([[ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2],
       [ 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0]])
    
    Q_s = sarsa(env, n_episodes = 50000, gamma=1.0, alpha=0.01, epsilon=0.1)
    policy_q = np.array([np.argmax(Q_s[key]) if key in Q_s else -1 for key 
                          in np.arange(48)]).reshape((4,12))
    print(policy_q)
    assert np.allclose(policy_q.shape,(4,12))
    assert np.allclose(policy_q[2:,],test_policy)
    
#---------------------------------------------------------------
def test_q_learning():
    '''Q_learning (25 points)'''
    Q_q = q_learning(env,n_episodes = 10000, gamma=1.0, alpha=0.01, epsilon=0.1)
    policy_q = np.array([np.argmax(Q_q[key]) if key in Q_q else -1 for key 
                         in np.arange(48)]).reshape((4,12))
    test_policy = np.array([[ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2],
       [ 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0]])
    
    print(policy_q)
    assert np.allclose(policy_q.shape,(4,12))
    assert np.allclose(policy_q[2:,],test_policy)
