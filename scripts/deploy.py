from ape import accounts, project

def main():
    deployer = accounts.load("deployer-ctf-sepolia")
    project.Ctf.deploy("Ethereum", sender = deployer)
