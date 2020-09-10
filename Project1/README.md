
# DS595/CS525 2020 Fall Individual Project 1
# Dynamic Programming of Markov Decision Process

#### Due Date
* Thursday September 24, 2020(23:59)

#### Total Points
* 100 (One Hundred)

## Goal

In this assignment, you will be asked to implement policy iteration and value iteration for the Frozen Lake environment from [OpenAI Gym](https://gym.openai.com/envs/#toy_text) and play the game with the algorithms you implemented. This project will be completed in Python 3.

<img src="https://github.com/yingxue-zhang/DS595CS525-RL-Projects/blob/master/Project1/img/hw1.png" width="80%">
<img src="https://github.com/yingxue-zhang/DS595CS525-RL-Projects/blob/master/Project1/img/details_fl.png" width="80%">


## Deliverables

Please compress your mdp_dp.py file into a zipped file (firstName_lastName_hw1.zip) and submit it to Canvas.

## Grading
* policy evaluation (20 points)
* policy improvement (20 points)
* policy iteration (20 points)
* value iteration (20 points)
* rander game (20 points)

## Hints
* Policy Evaluation<br/>
<span style="color:red">**Please note that reward can be defined on (state), (state, action), (state, action, next_state). In this assignment, we define the reward on (state,action,next_state).** The following pseudocode is the general method.</span>
<img src="https://github.com/yingxue-zhang/DS595CS525-RL-Projects/blob/master/Project1/img/pe.png" width="80%" >

* Policy Iteration<br/>
<img src="https://github.com/yingxue-zhang/DS595CS525-RL-Projects/blob/master/Project1/img/pi.png" width="80%" >

* Value Iteration<br/>
<img src="https://github.com/yingxue-zhang/DS595CS525-RL-Projects/blob/master/Project1/img/vi.png" width="80%" >


## Setup
* Install [Python 3](https://www.python.org/downloads/)
* interminal, type: pip [install gym](https://pypi.org/project/gym/0.7.2/)
* interminal, type: pip [install nose](https://pypi.org/project/nose/)

## Guidelines
* Implement functions in mdp_dp.py
* Evaluate functions by typing "nosetests -v mdp_dp_test.py" in terminal (you need put mdp_dp.py and mdp_dp_test.py in the same folder)
* If you got error using "nosetests -v mdp_dp_test.py" due to python version (sometimes, nosetests will use python2.7 by default), try: python3 -m nose -v mdp_dp_test.py

## Tips for Python and OpenAI Gym
[Python Documentation](https://www.python.org/doc/)

[Python Tutorial](https://www.geeksforgeeks.org/python-programming-language/)

[OpenAI Gym Documentation](https://gym.openai.com/docs/)
