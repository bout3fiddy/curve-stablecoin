import brownie
import pytest
from brownie import ZERO_ADDRESS


def test_mint(alice, bob, stablecoin):
    tx = stablecoin.mint(bob, 10**18, {"from": alice})

    assert stablecoin.balanceOf(bob) == 10**18
    assert stablecoin.totalSupply() == 10**18
    assert tx.events["Transfer"].values() == [ZERO_ADDRESS, bob, 10**18]
    assert tx.return_value is True


def test_mint_reverts_caller_is_invalid(bob, stablecoin):
    with brownie.reverts():
        stablecoin.mint(bob, 10**18, {"from": bob})


@pytest.mark.parametrize("idx", [0, 1])
def test_mint_reverts_receiver_is_invalid(alice, stablecoin, idx):
    receiver = [ZERO_ADDRESS, stablecoin][idx]
    with brownie.reverts():
        stablecoin.mint(receiver, 10**18, {"from": alice})
