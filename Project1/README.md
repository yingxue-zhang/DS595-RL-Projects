
# DS595/CS525 2019 Fall Individual Project 1
# Dynamic Programming of Markov Decision Process

#### Due Date
* Thursday September 12, 2019(23:59)

#### Total Points
* 100 (One Hundred)

## Goal

In this assignment, you will be asked to implement policy iteration and value iteration for the Frozen Lake environment from [OpenAI Gym](https://gym.openai.com/envs/#toy_text) and play the game with the algorithms you implemented. This project will be completed in Python 3.

<img src="https://github.com/huiminren/DS595CS525-RL-HW/blob/master/project1/img/hw1.png" width="80%">
<img src="https://github.com/huiminren/DS595CS525-RL-HW/blob/master/project1/img/details_fl.png" width="80%">

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
<img src="https://github.com/huiminren/DS595CS525-RL-HW/blob/master/project1/img/pe.png" width="80%" >

## Setup
* Install [Python 3](https://www.python.org/downloads/)
* pip [install gym](https://pypi.org/project/gym/0.7.2/)
* pip [install nose](https://pypi.org/project/nose/)

## Guidelines
* Implement functions in mdp_dp.py
* Evaluate functions by typing "nosetests -v mdp_dp_test.py" (put mdp_dp.py and mdp_dp_test.py in the same folder)

## Tips for Python and OpenAI Gym
[Python Documentation](https://www.python.org/doc/)

[Python Tutorial](https://www.geeksforgeeks.org/python-programming-language/)

[OpenAI Gym Documentation](https://gym.openai.com/docs/)
