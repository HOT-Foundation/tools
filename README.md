# HOT helper tools

## Getting Started
```
git clone git@github.com:HOT-Foundation/tools.git
cd tools
pipenv install
pipenv shell
```

## Validate wallet
Check that wallet is ready to work with HOT asset or not.

### Usage
```
➜ ./validate.py --help
Usage: validate.py [OPTIONS] WALLET_ADDRESS

Options:
  --network TEXT  TESTNET | PUBLIC
  --help          Show this message and exit.
```

### Example

#### Passed
```
➜ ./validate.py GDRNLVBUS5GLAFB223Z7WM775566XINHIOR2QMUKRNI7E3SM42OBN4QL --network PUBLIC
Validating wallet address: GDRNLVBUS5GLAFB223Z7WM775566XINHIOR2QMUKRNI7E3SM42OBN4QL, network: PUBLIC
PASSED
```

#### Failed
```
➜ ./validate.py GADZFOERY6RYJGVNISOIE3ZDEDBWBKVDAJZKV6S7MK3JXBCGBDO7EY4E --network PUBLIC
Validating wallet address: GADZFOERY6RYJGVNISOIE3ZDEDBWBKVDAJZKV6S7MK3JXBCGBDO7EY4E, network: PUBLIC
FAILED: This wallet doesn't trust HOT asset.
```


## Make HOT Payment
Pay HOT to target address

### Usage
```
➜ ./payment.py --help
Usage: payment.py [OPTIONS] TARGET_ADDRESS AMOUNT

Options:
  --network [TESTNET|PUBLIC]
  --source_secret TEXT
  --help                      Show this message and exit.
```

### Example
```
➜ ./payment.py GDRNLVBUS5GLAFB223Z7WM775566XINHIOR2QMUKRNI7E3SM42OBN4QL 1 --network PUBLIC
Source secret:
###############   TX   #################
Payment 1 HOT from GDUAZ76BPJTQ4R4LWBEFUFNTYLIWWBRI4PXGTLQ5O5SW5NLF3W7KPBKS to GDRNLVBUS5GLAFB223Z7WM775566XINHIOR2QMUKRNI7E3SM42OBN4QL
Network: PUBLIC
Sequence: 71485311120572435
Hash: b'!p\xa07@\xca{\xf1N,\x01\xcao8G\xccX\xed\xe3\x19\x12$\x91\xd4\x8f\xd7nyH\x93t\xb0'
#########################################
Correct? [y/N]: y
Submitting...
success
```
