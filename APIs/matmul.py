import shape
import itertools
import util
import dot

def matmul_1(X, Y):
	X_shape = shape.shape_1(X)
	Y_shape = shape.shape_1(Y)

	X_shape_batch = X_shape[:-2]
	Y_shape_batch = Y_shape[:-2]

	X_dim_batch = len(X_shape_batch)
	Y_dim_batch = len(Y_shape_batch)

	output_shape = util.broadcast_shape(X_shape_batch, Y_shape_batch)
	output_dim = len(output_shape)

	output_array = util.create_array(output_shape)

	for indices in itertools.product(*[list(range(j)) for j in output_shape]):
		x = X
		for i, index in enumerate(indices[output_dim-X_dim_batch:]):
			x = x[index % X_shape[i]]
		y = Y
		for i, index in enumerate(indices[output_dim-Y_dim_batch:]):
			y = y[index % Y_shape[i]]

		out = output_array
		for i, index in enumerate(indices):
			if i + 1 == len(indices):
				out[index] = dot.dot_1(x, y)
			else:
				out = out[index]

	if len(indices) == 0: 	# Not an array
		output_array = dot.dot_1(x, y)
		
	return output_array

def test_matmul():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	op = np.matmul

	A = jrr(key, (2, 4, 3), 0, 10)
	B = jrr(key, (3,), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(matmul_1(A.tolist(), B.tolist()))))

	A = jrr(key, (5,), 0, 10)
	B = jrr(key, (5, 2), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(matmul_1(A.tolist(), B.tolist()))))

	A = jrr(key, (5,), 0, 10)
	B = jrr(key, (5,), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(matmul_1(A.tolist(), B.tolist()))))

	A = jrr(key, (6, 5), 0, 10)
	B = jrr(key, (5, 7), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(matmul_1(A.tolist(), B.tolist()))))

	A = jrr(key, (8, 1, 7, 4), 0, 10)
	B = jrr(key, (1, 5, 4, 3), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(matmul_1(A.tolist(), B.tolist()))))

	A = jrr(key, (3, 2), 0, 10)
	B = jrr(key, (5, 2, 4), 0, 10)
	assert(np.array_equal(op(A, B),np.asarray(matmul_1(A.tolist(), B.tolist()))))