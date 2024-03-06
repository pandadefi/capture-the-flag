from ape import Contract
from pytest import fixture


@fixture
def deployer(accounts):
    return accounts[0]

@fixture
def player(accounts):
    return accounts[1]

@fixture
def contract(project, deployer):
    return project.Ctf.deploy("Ethereum", sender = deployer)
