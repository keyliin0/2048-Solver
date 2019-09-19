#### Installation
```
pip install pygame gym-2048 gym
```

Download the repository then run

```
python main.py
```

#### How it works

Take each state and pass it to the search function which will return the best action.

For the search we try to simulate every 4 possible combinaison of actions, we have 4 possible actions (Up, Down, Right, Left) and we want to make 4 consecutive actions so we have 4^4 possible moves in total to simulate.

In the end we pick the action  that leads to the highest fitness fuction. 

The fitness function here is the sum of all the merged tiles while simulating the 4 actions.

![alt text](https://raw.githubusercontent.com/keyliin0/2048-Solver/master/Screenshot.jpg)
