import shape, zeros, itertools

def transpose_1(a, axes = None):
	shape_inp = shape.shape_1(a)
	if axes == None:
		axes = [i for i in range(len(shape_inp))][::-1]

	shape_out = [shape_inp[axes[i]] for i in range(len(shape_inp))]

	out = zeros.zeros_1(shape_out)

	for indices in itertools.product(*[list(range(j)) for j in shape_inp]):
		x = a
		for index in indices:
			x = x[index]
		o = out
		for i, index in enumerate([indices[axes[j]] for j in range(len(indices))]):
			if i+1 == len(indices):
				o[index] = x
			else:
				o = o[index]
	return out

def test_transpose():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	A = jrr(key, (2, 5, 3, 7), 0, 10)
	assert(np.array_equal(A.transpose(1,3,0,2), np.asarray(transpose_1(A.tolist(), (1,3,0,2)))))

	A = jrr(key, (2, 5, 3, 7), 0, 10)
	assert(np.array_equal(A.transpose(), np.asarray(transpose_1(A.tolist()))))
