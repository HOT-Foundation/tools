#!/usr/bin/env python
import click
from stellar_base import exceptions
from stellar_base.address import Address
from stellar_base.builder import Builder
from stellar_base.horizon import Horizon

from config import configs


@click.command()
@click.argument('wallet_address')
@click.option('--network', default='TESTNET', help='TESTNET | PUBLIC')
def validate(wallet_address: str, network: str) -> str:
    # Check wallet exists or not and check wallet have trust HTKN yet
    print('Validating wallet address: {}, network: {}'.format(wallet_address, network))
    config = configs[network]
    try:
        wallet = Address(wallet_address, horizon_uri=config['HORIZON_URL'], network=network)
        wallet.get()
        if _is_trust_hot(wallet, config):
            print('PASSED')
        else:
            print('FAILED: This wallet doesn\'t trust HOT asset.')
    except exceptions.StellarAddressInvalidError as e:
        print('FAILED: {}'.format(e))
    except (exceptions.HorizonError) as e:
        print('FAILED: Wallet not found.')
    except Exception as e:
        print('FAILED: {}'.format(e))

def _is_trust_hot(wallet, config):
    for balance in wallet.balances:
        if 'asset_code' in balance and balance['asset_code'] == 'HOT' and balance['asset_issuer'] == config['ISSUER_HOT']:
            return True
    return False

if __name__ == '__main__':
    validate()
