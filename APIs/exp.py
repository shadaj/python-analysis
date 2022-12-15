import itertools
import shape, zeros_like
from math import e

def exp_1(X):
	shape_input = shape.shape_1(X)
	output = zeros_like.zeros_like_1(X)

	for indices in itertools.product(*[list(range(j)) for j in shape_input]):
		x = X
		for index in indices:
			x = x[index]
		out = output
		for i, index in enumerate(indices):
			if i + 1 == len(indices):
				out[index] = e ** x
			else:
				out = out[index]
	if len(shape_input) == 0: 	# Not an array
		return e ** X

	return output

def test_exp():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.uniform
	for i in range(30):
		A = jrr(key, (), minval=-5, maxval=5)
		res1 = np.exp(A)
		res2 = np.asarray(exp_1(A.tolist()))
		assert(np.allclose(res1, res2, equal_nan=True))
		A = jrr(key, (2, 6), minval=-5, maxval=5)
		res1 = np.exp(A)
		res2 = np.asarray(exp_1(A.tolist()))
		assert(np.allclose(res1, res2, equal_nan=True))