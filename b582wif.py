#!/usr/bin/env python

# b582wif by taup1n
# takes list of raw b58 blockchain.info private keys in 'addr - key' format 
# transmutes into wif for easy import into more civilized wallets

import sys, base58, hashlib, binascii, os.path

def b2h(bytestr):
    return ''.join(["%02x" % ord(x) for x in bytestr]).strip()

if len(sys.argv) < 2:
	sys.exit("usage: " + sys.argv[0] + " filename")

filename = sys.argv[1]

if not os.path.isfile(filename):
	sys.exit("file not found.")

keypairs = []

with open(filename) as f:
	for line in f:
		keypairs.append(line.strip().split('-'))
for pair in keypairs:
	try:
		x,y = pair[0].strip(),pair[1].strip()
		hexkey = "80" + b2h(base58.b58decode((y))).strip()
		r1 = hashlib.sha256(binascii.unhexlify(hexkey)).hexdigest()
		r2 = hashlib.sha256(binascii.unhexlify(r1)).hexdigest()
		keycsum = hexkey + r2[:8]
		print base58.b58encode(binascii.unhexlify(keycsum))
	except IndexError:
		print "error in file format."
