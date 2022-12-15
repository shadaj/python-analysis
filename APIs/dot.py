import shape
import zeros
import itertools
import transpose
import mul

def dot_1(X, Y):
	X_shape = shape.shape_1(X)
	Y_shape = shape.shape_1(Y)

	X_dim = len(X_shape)
	Y_dim = len(Y_shape)

	if Y_dim == 0 or X_dim == 0:
		return mul.mul_1(X, Y)

	if Y_dim > 1:
		axes = [i for i in range(Y_dim)]
		axes[-1], axes[-2] = axes[-2], axes[-1]
		Y_t = transpose.transpose_1(Y, axes = axes)
	else:
		Y_t = Y

	Y_shape = shape.shape_1(Y_t)

	assert X_shape[-1] == Y_shape[-1]

	out_shape = X_shape[:-1] + Y_shape[:-1]
	out_array = zeros.zeros_1(out_shape)

	out_dim = len(out_shape)

	for indices in itertools.product(*[list(range(j)) for j in (out_shape + X_shape[-1:])]):
		x_indices = indices[:X_dim-1] + indices[-1:]
		y_indices = indices[X_dim-1:]
		x = X
		for index in x_indices:
			x = x[index]
		y = Y_t
		for index in y_indices:
			y = y[index]

		out = out_array
		for i, index in enumerate(indices[:-1]):
			if i + 1 == len(indices) - 1:
				out[index] += x * y
			else:
				out = out[index]

		if len(indices) == 1: 	# Not an array
			out_array += x * y
		
	return out_array

def test_dot():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	op = np.dot

	A = jrr(key, (), 0, 10)
	B = jrr(key, (), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))

	A = jrr(key, (), 0, 10)
	B = jrr(key, (3,), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))

	A = jrr(key, (2, 4, 3), 0, 10)
	B = jrr(key, (3,), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))

	A = jrr(key, (5,), 0, 10)
	B = jrr(key, (5, 2), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))

	A = jrr(key, (5,), 0, 10)
	B = jrr(key, (5,), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))

	A = jrr(key, (6, 5), 0, 10)
	B = jrr(key, (5, 7), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))

	A = jrr(key, (8, 1, 2, 1, 7, 4), 0, 10)
	B = jrr(key, (2, 5, 4, 3), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))

	A = jrr(key, (3, 2), 0, 10)
	B = jrr(key, (5, 2, 4), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(dot_1(A.tolist(), B.tolist()))))