# Inidividual Project 3
# Deep Q-learning Network(DQN)
Please don't revise test.py, environment.py and agent.py

#### Due Date
* Thursday October 22, 2020 (23:59)

#### Total Points
* 100 (One Hundred)

* How to elvaluate
  * You should submit your lastest trained model and python code before leaderboard due date. TA will run your code to make sure the result is consistent with your screenshot. 
* How to grade
  * Top 3 students on the leaderboard can get 10 bonus points for project 3.
  

## Installation
Type the following command to install OpenAI Gym Atari environment in your **virutal environment**.

`$ pip install opencv-python-headless gym==0.10.4 gym[atari]`

Please refer to [OpenAI's page](https://github.com/openai/gym) if you have any problem while installing.

## How to run :
training DQN:
* `$ python main.py --train_dqn`

testing DQN:
* `$ python test.py --test_dqn`

## Goal
In this project, you will be asked to implement DQN to play [Breakout](https://gym.openai.com/envs/Breakout-v0/). This project will be completed in Python 3 using [Pytorch](https://pytorch.org/). The goal of your training is to get averaging reward in 100 episodes over **40 points** in **Breakout**, with OpenAI's Atari wrapper & unclipped reward. For more details, please see the [slides](https://docs.google.com/presentation/d/1CbYqY5DfXQy4crBw489Tno_K94Lgo7QwhDDnEoLYMbI/edit?usp=sharing).

<img src="https://github.com/yingxue-zhang/DS595CS525-RL-Projects/blob/master/Project3/materials/project3.png" width="80%" >

## Deliverables
Please compress all the below files into a zipped file and submit the zip file (firstName_lastName_hw3.zip) to Canvas.

* **Trained Model**
  * Model file
  * If your model is too large for Canvas, upload it to a cloud space and write download.sh to download the model

* **PDF Report**
  * Set of Experiments Performed: 
    * Include a section describing the set of experiments that you performed
    * what structures you experimented with (i.e., number of layers, number of neurons in each layer)
    * what hyperparameters you varied (e.g., number of epochs of training, batch size and any other parameter values, weight initialization schema, activation function)
    * what kind of loss function you used and what kind of optimizer you used.
  * Special skills: Include the skills which can improve the generation quality. Here are some [tips](https://arxiv.org/pdf/1710.02298.pdf) may help. (Optional)
  * Visualization: Learning curve of DQN. 
    * X-axis: number of time steps
    * Y-axis: average reward in last 30 episodes.

* **Python Code**
  * All the code you implemented including sample codes.

## Grading
* **Trained Model (50 points)**
  * Getting averaging reward in 100 episodes over **40 points** in Breakout will get full credits. 
  * For every average reward below 40, you will be taken off 2 points. i.e., you will be taken off 2 points, if getting averaging reward in 100 episodes is 39 and taken off 4 points, if averaging reward is 38, so on so forth.

* **PDF Report (30 points)**
  * Set of parameters performed: 20 points
  * Visualization: 10 points
  
* **Python Code (20 points)**
  * You can get full credits if the scripts can run successfully, otherwise you may loss some points based on your error.

## Hints
* [Naive Pytorch Tutorial](https://github.com/yingxue-zhang/DS595CS525-RL-Projects/blob/master/Project3/materials/Pytorch_tutorial.ipynb)
* [Official Pytorch Tutorial](https://pytorch.org/tutorials/)
* [Official DQN Pytorch Tutorial](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html)
* [Official DQN paper](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)
* [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/pdf/1710.02298.pdf)
* [DQN Tutorial on Medium](https://medium.com/@jonathan_hui/rl-dqn-deep-q-network-e207751f7ae4)

## Tips for Using GPU on Google Cloud
* [How to use Google Cloud Platform](https://docs.google.com/document/d/1JfIG_yBi-xEIdT6KP1-eUpgLDoY3t2QrAKULB9yf01Q/edit?usp=sharing)
* [How to use Pytorch on GPU](https://docs.google.com/document/d/1i8YawKjEwg7qpfo7Io4C_FvSYiZxZjWMLkqHfcZMmaI/edit?usp=sharing)
* Other choice for GPU
  * Use your own GPU
  * Apply [Ace account](https://arc.wpi.edu/computing/accounts/ace-accounts/) from WPI 
