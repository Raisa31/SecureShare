import random
from math import ceil
from decimal import Decimal
import numpy as np
import util

FIELD_SIZE = 10**5

def reconstruct_secret(shares):
	sums = 0
	for j, share_j in enumerate(shares):
		xj, yj = share_j
		prod = Decimal(1)
		for i, share_i in enumerate(shares):
			xi, _ = share_i
			if i != j:
				prod *= Decimal(Decimal(xi)/(xi-xj))
		prod *= yj
		sums += Decimal(prod)
	return (int(round(Decimal(sums), 0)))


def polynom(x, coefficients):
	point = 0
	for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
		point += x ** coefficient_index * coefficient_value
	return point


def coeff(t, secret):
	coeff = [random.randrange(0, FIELD_SIZE) for _ in range(t - 1)]
	coeff.append(secret)
	return coeff


def generate_shares(n, m, secret):
	coefficients = coeff(m, secret)
	shares = []
	usedSet = set()
	for i in range(1, n+1):
		x = random.randrange(1, FIELD_SIZE)
		while x in usedSet:
			x = random.randrange(1, FIELD_SIZE)
		usedSet.add(x)
		shares.append((x, polynom(x, coefficients)))

	return shares

def to_rgb(v):
    return np.array([int(v[1:3],16), int(v[3:5],16) , int(v[5:7],16)])

def storeShares(i, j, solution, shares):
	for k in range(0, len(solution)):
		solution[k][i][j] = shares[k]


# Driver code
def generate_and_reconstruct_image(args):
	n = args.n_shares
	t = args.threshold
	secretImage = "encoded_image.png"
	secret, mode = util.genHex(secretImage)

	solution = [[[(0,0) for k in range(len(secret[0]))] for j in range(len(secret))] for i in range(n)]

	for i in range(0, len(secret)):
		for j in range(0, len(secret[0])):
				shares = generate_shares(n, t, int(secret[i][j][1:],16))
				storeShares(i, j, solution, shares)

	reconstructed_secret = [[0 for k in range(len(secret[0]))] for j in range(len(secret))]
	secret_len = set()
	for i in range(0, len(solution[0])):
			for j in range(0, len(solution[0][0])):
				col = []
				for k in range(0, len(solution)):
					col.append(solution[k][i][j])
				pool = random.sample(col, t)

				reconstructed_secret[i][j] = '#' + util.padded_hex(reconstruct_secret(pool), 6)[2:]
				secret_len.add(len(reconstructed_secret[i][j]))
				
	util.genImg('img_reconst.png', reconstructed_secret, mode)