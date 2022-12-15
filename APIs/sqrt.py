import itertools
import shape, zeros_like
from math import e

def sqrt_1(X):
	shape_input = shape.shape_1(X)
	output = zeros_like.zeros_like_1(X)

	for indices in itertools.product(*[list(range(j)) for j in shape_input]):
		x = X
		for index in indices:
			x = x[index]
		out = output
		for i, index in enumerate(indices):
			if i + 1 == len(indices):
				out[index] = x ** 0.5 if x >= 0 else float("nan")
			else:
				out = out[index]
	if len(shape_input) == 0: 	# Not an array
		return X ** 0.5 if X >= 0 else float("nan")

	return output

def test_sqrt():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.uniform
	for i in range(30):
		A = jrr(key, (), minval=-5, maxval=5)
		res1 = np.sqrt(A)
		res2 = np.asarray(sqrt_1(A.tolist()))
		assert(np.allclose(res1, res2, equal_nan=True))
		A = jrr(key, (2, 6), minval=-5, maxval=5)
		res1 = np.sqrt(A)
		res2 = np.asarray(sqrt_1(A.tolist()))
		assert(np.allclose(res1, res2, equal_nan=True))