import random
import time
epsilon=0.3
gamma=0.9
alpha=0.1
vec=[[0.0 for _ in range(3)] for _ in range(2)]
reward=[1,5,2]
poss0=[[0.1,0.4,0.5],[0.4,0.2,0.4],[0.3,0.7,0.0]]
poss1=[[0.2,0.6,0.2],[0.5,0.25,0.25],[0.3,0.1,0.6]]
random.seed(time.time())
global_step=0
state0 = random.randint(0, 2)
t=random.random()
if(t>epsilon):
    action0=0 if vec[0][state0]>vec[1][state0] else 1
else:
    action0=random.randint(0,1)
print("begin state:",state0+1)
def findstate(state,action0):
    t=random.random()
    if action0==0:
        if t<poss0[state][0]:
            state1=0
        elif t<poss0[state][0]+poss0[state][1]:
            state1=1
        else:
            state1=2
    else:
        if t<poss1[state][0]:
            state1=0
        elif t<poss1[state][0]+poss1[state][1]:
            state1=1
        else:
            state1=2
    return state1
def iteration(state,action):
    global global_step
    t=random.random()
    if(t>epsilon):
        action1=0 if vec[0][state]>vec[1][state] else 1
    else:
        action1=random.randint(0,1)
    state1=findstate(state,action)
    vec[action][state]+= alpha*(reward[state1] + gamma*vec[action1][state1]-vec[action][state])
    global_step += 1
    return state1,action1
def run(state,action,T):
    for _ in range(0,T):
        state,action=iteration(state,action)
    print("step=",global_step,",final state:",state0+1)
    print("        state1                  state2                  state3")
    print("action1", end=' ')
    for j in range(2):
        print(vec[0][j], end='\t')
    print(vec[0][2])
    print("action2", end=' ')
    for j in range(2):
        print(vec[1][j], end='\t')
    print(vec[1][2])
    return state,action
state0,action0=run(state0,action0,100)
state0,action0=run(state0,action0,1000)
state0,action0=run(state0,action0,10000)
state0,action0=run(state0,action0,20000)
