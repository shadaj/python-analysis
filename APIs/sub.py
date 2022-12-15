import shape
import util
import itertools

def sub_1(X, Y):
	X_shape = shape.shape_1(X)
	Y_shape = shape.shape_1(Y)

	X_dim = len(X_shape)
	Y_dim = len(Y_shape)

	out_shape = util.broadcast_shape(X_shape, Y_shape)
	out_array = util.create_array(out_shape)
	out_dim = len(out_shape)

	for indices in itertools.product(*[list(range(j)) for j in out_shape]):
		x = X
		for i, index in enumerate(indices[out_dim-X_dim:]):
			x = x[index % X_shape[i]]
		y = Y
		for i, index in enumerate(indices[out_dim-Y_dim:]):
			y = y[index % Y_shape[i]]

		out = out_array
		for i, index in enumerate(indices):
			if i + 1 == len(indices):
				out[index] = x - y
			else:
				out = out[index]

	if len(out_shape) == 0: 	# Not an array
		return X - Y
	else:
		return out_array

def test_sub():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	A = jrr(key, (8, 1, 2, 1, 3, 1), 0, 10)
	B = jrr(key, (2, 5, 3, 1), 0, 10)
	op = operator.sub
	assert(np.array_equal(op(A, B),np.asarray(sub_1(A.tolist(), B.tolist()))))

	A = jrr(key, (3, 1), 0, 10)
	B = jrr(key, (2, 5, 3, 1), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(sub_1(A.tolist(), B.tolist()))))

	A = jrr(key, (), 0, 10)
	B = jrr(key, (), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(sub_1(A.tolist(), B.tolist()))))

	A = jrr(key, (2, 4, 3), 0, 10)
	B = jrr(key, (), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(sub_1(A.tolist(), B.tolist()))))