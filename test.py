import dmc2gym
import copy
env = dmc2gym.make(domain_name='cheetah', task_name='run', seed=1)
global_init_obs = env.reset()

test_env = copy.deepcopy(env)
next_obs = global_init_obs
blueprint_ep_ret = 0
blueprint_step_until_dead = 0
while True:

    action = test_env.action_space.sample()

    print(action)

    next_obs, rs, ds, infos = test_env.step(action)
    print(next_obs.shape)

    if ds:
        break

del test_env

