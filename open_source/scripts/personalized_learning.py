python
import gym
from stable_baselines3 import PPO

# Create personalized environment
class PersonalizedEnv(gym.Env):
    def __init__(self, user_data):
        super(PersonalizedEnv, self).__init__()
        self.user_data = user_data
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(len(user_data),), dtype=float)
        self.action_space = gym.spaces.Discrete(2)

    def reset(self):
        return self.user_data

    def step(self, action):
        reward = self.compute_reward(action)
        done = True  # Example for simplicity
        info = {}
        return self.user_data, reward, done, info

    def compute_reward(self, action):
        # Define a reward function based on user data and action
        return 1 if action == 1 else 0

if __name__ == "__main__":
    user_data = [0.5, 0.2, 0.8]  # Example user data, replace with actual data
    env = PersonalizedEnv(user_data)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("personalized_model")

    obs = env.reset()
    action, _states = model.predict(obs)
    print(f"Predicted action: {action}")
