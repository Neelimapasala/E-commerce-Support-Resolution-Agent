import os

def load_policies(policy_dir="policies"):
    policies = {}
    for file in os.listdir(policy_dir):
        with open(os.path.join(policy_dir, file), "r", encoding="utf-8") as f:
            policies[file] = f.read()
    return policies
