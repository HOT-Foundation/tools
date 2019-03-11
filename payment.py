#!/usr/bin/env python
import urllib
from decimal import Decimal
from getpass import getpass

import click
from stellar_base import exceptions
from stellar_base.address import Address
from stellar_base.builder import Builder
from stellar_base.keypair import Keypair

from config import configs
from validate import validate


@click.command()
@click.argument('target_address')
@click.argument('amount')
@click.option('--network', default='TESTNET', type=click.Choice(['TESTNET', 'PUBLIC']))
@click.option('--source_secret', prompt=True, hide_input=True)
def payment(target_address: str, amount: str, network, source_secret):
    config = configs[network]
    src_address = Keypair.from_seed(source_secret).address().decode()
    builder = Builder(secret=source_secret, horizon_uri=config['HORIZON_URL'], network=network)
    builder.append_payment_op(destination=target_address, asset_code='HOT',
            asset_issuer=config['ISSUER_HOT'], amount=amount)
    builder.sign()
    print("###############   TX   #################")
    print('Payment {} HOT from {} to {}'.format(amount, src_address, target_address))
    print('Network: {}'.format(network))
    print('Sequence: {}'.format(builder.sequence))
    print('Hash: {}'.format(builder.hash()))
    print("#########################################")
    click.confirm('Correct?', abort=True)
    print('Submitting...')
    builder.submit()
    print('success')
    return True

if __name__ == '__main__':
    payment()
