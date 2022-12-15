import itertools
import zeros

def eye_1(N, M=None, k = 0):
	if M is None:
		M = N

	out = zeros.zeros_1((N, M))

	i1 = 0 if 0 <= k else -k

	for i in range(i1, N):
		j = i+k
		if j >= 0 and j < M:
			out[i][j] = 1

	return out

def test_eye():
	import jax as jax
	import jax.numpy as np

	for N, M, k in itertools.product(*((1, 3, 5),(None, 1, 7),(0, -1, 1))):
		assert(np.allclose(np.eye(N, M, k), np.asarray(eye_1(N, M, k))))
