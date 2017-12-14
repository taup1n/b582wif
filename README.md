# b582wif
takes blockchain.info "address - rawb58" format and converts raw base58 keys into wallet import format (WIF).

## dependencies
pip install base58
the rest should be stock p2.7.

## usage
./b582wif.py filename
or
./b582wif.py filename > b58.txt
if you want to dump the output in a file.

filename should be in format "address - raw b58 private key".
