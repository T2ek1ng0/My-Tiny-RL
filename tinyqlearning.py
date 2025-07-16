import random
import time
from torch.utils.tensorboard import SummaryWriter

# 初始化TensorBoard写入器
writer = SummaryWriter()
epsilon=0.3
gamma=0.9
alpha=0.1
vec=[[0.0 for _ in range(3)] for _ in range(2)]
reward=[1,5,2]
poss0=[[0.1,0.4,0.5],[0.4,0.2,0.4],[0.3,0.7,0.0]]
poss1=[[0.2,0.6,0.2],[0.5,0.25,0.25],[0.3,0.1,0.6]]
random.seed(time.time())
state0 = random.randint(0, 2)
print("begin state:",state0+1)
global_step = 0  # 全局步数计数器
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
def iteration(state):
    global global_step  # 使用全局步数计数器
    t=random.random()
    if(t>epsilon):
        action=0 if vec[0][state]>vec[1][state] else 1
    else:
        action=random.randint(0,1)
    state1=findstate(state,action)
    vec[action][state]+= alpha*(reward[state1] + gamma*max(vec[0][state1],vec[0][state1])-vec[action][state])
    # 记录当前步骤的所有Q值
    for i in range(2):
        for j in range(3):
            writer.add_scalar(f'Q_Value/Action_{i+1}_State_{j+1}', vec[i][j], global_step)
    
    global_step += 1  # 步数加1
    return state1
def run(state,T):
    for _ in range(0,T):
        state=iteration(state)
    print("episode=",T,",final state:",state0+1)
    print("        state1                  state2                  state3")
    print("action1", end=' ')
    for j in range(2):
        print(vec[0][j], end='\t')
    print(vec[0][2])
    print("action2", end=' ')
    for j in range(2):
        print(vec[1][j], end='\t')
    print(vec[1][2])
    return state
state0=run(state0,100)
state0=run(state0,1000)
state0=run(state0,10000)
state0=run(state0,20000)

# 关闭写入器
writer.close()