---
layout: page
title: "Using fNIRS neural data to Improve RL Agent Learning"
subheadline: "Reinforcement Learning Project"
teaser: "Project Highlights and Summary"
permalink: "/rlproject/"
header:
    image_fullwidth: "pacman.jpg"
---

## Highlights
* Project focused on using fNIRS brain data as a physiological input to an RL agent playing pacman. 
* The RL agent, which was either a deep-Q network or a dueling deep-Q network, used human demonstrations to help teach itself to play pacman. Human demonstrations are commonly used in this way to improve RL agent learning, but demonstrations where the human makes a mistake can actually be counterproductive. The brain data, therefore, was used as a physiological input to (hopefully) help the RL agent distinguish between good and bad demonstrations. 
* The hypothesis was that demonstrations given during times of high mental workload would be more likely to contain mistakes under the assumption that the player may have been overwhelmed at the time. 

## Summary

### Project Diagram
![RL Project Diagram](/ebuntel/ebuntel.github.io/assets/img/RLProjectDiagram.jpg)

## Technologies Used
* Python
* Jupyter notebook
* Tensorflow and tf-agents
* OpenAI Gym
* Deep Q-networks, Dueling Deep Q-networks
