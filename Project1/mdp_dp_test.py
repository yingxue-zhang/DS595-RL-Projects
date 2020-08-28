#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mdp_dp import *
import gym
import sys
import numpy as np

from gym.envs.registration import register

"""
    This file includes unit test for mdp_dp.py
    You could test the correctness of your code by 
    typing 'nosetests -v mdp_dp_test.py' in the terminal
"""
# Evaluate non-deterministic
env = gym.make("FrozenLake-v0")
env = env.unwrapped


# Evaluate deterministic
register(
    id='Deterministic-4x4-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
            'is_slippery': False})
env2 = gym.make("Deterministic-4x4-FrozenLake-v0")

#---------------------------------------------------------------
def test_python_version():
    '''------Dynamic Programming for MDP (100 points in total)------'''
    assert sys.version_info[0] == 3 # require python 3

#---------------------------------------------------------------
def test_policy_evaluation():
    '''policy_evaluation (20 points)'''
    random_policy1 = np.ones([env.nS, env.nA]) / env.nA
    V1 = policy_evaluation(env.P,env.nS,env.nA, random_policy1,tol=1e-8)
    test_v1 = np.array([0.004, 0.004, 0.01 , 0.004, 0.007, 0. , 0.026, 0. , 0.019,
       0.058, 0.107, 0. , 0. , 0.13 , 0.391, 0. ])

    np.random.seed(595)
    random_policy2 = np.random.rand(env.nS, env.nA)
    random_policy2 = random_policy2/random_policy2.sum(axis=1)[:,None]
    V2 = policy_evaluation(env.P,env.nS,env.nA, random_policy2,tol=1e-8)
    test_v2 = np.array([0.007, 0.007, 0.017, 0.007, 0.01 , 0. , 0.043, 0. , 0.029,
       0.093, 0.174, 0. , 0. , 0.215, 0.504, 0. ])

    assert np.allclose(test_v1,V1,atol=1e-3)
    assert np.allclose(test_v2,V2,atol=1e-3)
    


#---------------------------------------------------------------
def test_policy_improvement():
    '''policy_improvement (20 points)'''
    np.random.seed(595)
    V1 = np.random.rand(env.nS)
    new_policy1 = policy_improvement(env.P, env.nS, env.nA, V1)
    test_policy1 = np.array([[1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [0., 0., 0., 1.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.],
       [1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [0., 0., 0., 1.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [0., 0., 1., 0.],
       [1., 0., 0., 0.]])

    V2 = np.zeros(env.nS)
    new_policy2 = policy_improvement(env.P, env.nS, env.nA, V2)
    test_policy2 = np.array([[1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.]])
    
    assert np.allclose(test_policy1,new_policy1)
    assert np.allclose(test_policy2,new_policy2)

    
#---------------------------------------------------------------
def test_policy_iteration():
    '''policy_iteration (20 points)'''
    random_policy1 = np.ones([env.nS, env.nA]) / env.nA

    np.random.seed(595)
    random_policy2 = np.random.rand(env.nS, env.nA)
    random_policy2 = random_policy2/random_policy2.sum(axis=1)[:,None]

    policy_pi1, V_pi1 = policy_iteration(env.P, env.nS, env.nA, random_policy1,tol=1e-8)
    policy_pi2, V_pi2 = policy_iteration(env.P, env.nS, env.nA, random_policy2,tol=1e-8)

    optimal_policy = np.array([[1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.]])
    optimal_V = np.array([0.069, 0.061, 0.074, 0.056, 0.092, 0., 0.112, 0., 0.145,
       0.247, 0.3 , 0., 0., 0.38 , 0.639, 0.])


    policy_pi3, V_pi3 = policy_iteration(env2.P, env2.nS, env2.nA, random_policy1,tol=1e-8)
    optimal_policy2 = np.array([[0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [0., 1., 0., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 1., 0.],
       [1., 0., 0., 0.]])
    optimal_V2 = np.array([0.59 , 0.656, 0.729, 0.656, 0.656, 0. , 0.81 , 0. , 0.729,
       0.81 , 0.9  , 0. , 0. , 0.9 , 1. , 0. ])


    assert np.allclose(policy_pi1,optimal_policy)
    assert np.allclose(V_pi1,optimal_V,atol=1e-3)
    assert np.allclose(policy_pi2,optimal_policy)
    assert np.allclose(V_pi2,optimal_V,atol=1e-3)
    assert np.allclose(policy_pi3,optimal_policy2)
    assert np.allclose(V_pi3,optimal_V2,atol=1e-3)


#---------------------------------------------------------------
def test_value_iteration():
    '''value_iteration (20 points)'''
    np.random.seed(10000)
    V1 = np.random.rand(env.nS)
    policy_vi1, V_vi1 = value_iteration(env.P, env.nS, env.nA, V1, tol= 1e-8)

    V2 = np.zeros(env.nS)
    policy_vi2, V_vi2 = value_iteration(env.P, env.nS, env.nA, V2, tol= 1e-8)

    optimal_policy = np.array([[1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 0., 1.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.]])
    optimal_V = np.array([0.069, 0.061, 0.074, 0.056, 0.092, 0. , 0.112, 0. , 0.145,
        0.247, 0.3  , 0. , 0. , 0.38 , 0.639, 0. ])

    policy_vi3, V_vi3 = value_iteration(env2.P, env2.nS, env2.nA, V2)

    optimal_policy2 = np.array([[0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [0., 1., 0., 0.],
       [0., 1., 0., 0.],
       [1., 0., 0., 0.],
       [1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 1., 0.],
       [1., 0., 0., 0.]])
    optimal_V2 = np.array([0.59 , 0.656, 0.729, 0.656, 0.656, 0. , 0.81 , 0. , 0.729,
       0.81 , 0.9  , 0. , 0. , 0.9 , 1. , 0. ])

    
    assert np.allclose(policy_vi1,optimal_policy)
    assert np.allclose(V_vi1,optimal_V,atol=1e-3)
    assert np.allclose(policy_vi2,optimal_policy)
    assert np.allclose(V_vi2,optimal_V,atol=1e-3)
    assert np.allclose(policy_vi3,optimal_policy2)
    assert np.allclose(V_vi3,optimal_V2,atol=1e-3)

#---------------------------------------------------------------            
def test_render_single():
    '''render_single (20 points)'''                 
    print("\n" + "-"*25 + "\nBeginning Policy Iteration\n" + "-"*25)
    random_policy = np.ones([env.nS, env.nA]) / env.nA
    p_pi, V_pi = policy_iteration(env.P, env.nS, env.nA, random_policy,tol=1e-8)
    r_pi = render_single(env, p_pi, False, 50)
    print("total rewards of PI: ",r_pi)
    
    print("\n" + "-"*25 + "\nBeginning Value Iteration\n" + "-"*25)
    V = np.zeros(env.nS)
    p_vi, V_vi = value_iteration(env.P, env.nS, env.nA, V,tol=1e-8)
    r_vi = render_single(env, p_vi, False, 50)
    print("total rewards of VI: ",r_vi)
    
    
    assert r_pi > 30
    assert r_vi > 30