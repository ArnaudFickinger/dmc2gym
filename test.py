import dmc2gym
import copy
env = dmc2gym.make(domain_name='cheetah', task_name='run', seed=1)
test_env = copy.deepcopy(env)