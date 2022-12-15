from numpy import array
import shape, zeros, prod
import itertools

def get_array_index(index_along_axis, cum_input_size_along_axis):
	for i, size in enumerate(cum_input_size_along_axis):
		if index_along_axis < size:
			return i-1, index_along_axis - cum_input_size_along_axis[i-1]

def concatenate_1(axis=0, *arrays):
	assert len(arrays) > 0
	shape_input = shape.shape_1(arrays[0])
	assert len(shape_input) > 0
	num_arrays = len(arrays)
	cum_input_size_along_axis = [0]
	shape_output = list(shape_input)
		
	if axis is not None:
		shape_output[axis] = 0
		for i in range(num_arrays):
			shape_axis = shape.shape_1(arrays[i])[axis]
			shape_output[axis] += shape_axis
			cum_input_size_along_axis.append(shape_output[axis])
		# shape_output[axis] *= num_arrays
		if axis < 0:
			axis += len(shape_input)
		output = zeros.zeros_1(shape_output)
		axis_m = axis
	else:
		shape_output = [0]
		for i in range(num_arrays):
			x = shape.shape_1(arrays[i])
			shape_output[0] += prod.prod_1(shape.shape_1(arrays[i]))
		# shape_output[0] *= num_arrays
		output = zeros.zeros_1(shape_output)
		axis_m = 0

	if axis is not None:
		for indices in itertools.product(*[list(range(j)) for j in shape_output]):
			indx, rem = get_array_index(indices[axis_m], cum_input_size_along_axis)
			x = arrays[indx]

			for i, index in enumerate(indices):
				if i != axis_m:
					x = x[index]
				else:
					x = x[rem]

			out = output
			for i, index in enumerate(indices):
				if i+1 == len(shape_output):
					out[index] = x
				else:
					out = out[index]
	else:
		count = 0
		for inp_array in arrays:
			for indices in itertools.product(*[list(range(j)) for j in shape.shape_1(inp_array)]):
				x = inp_array
				for i, index in enumerate(indices):
					x = x[index]
				output[count] = x
				count += 1
	return output

def test_concatenate():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	op = np.concatenate

	A = jrr(key, (3, 5, 7), 0, 10)
	B = jrr(key, (3, 5, 7), 0, 10)
	D = jrr(key, (3, 8), 0, 10)
	E = jrr(key, (3, 7), 0, 10)
	C = jrr(key, (1,), 0, 10)

	for arrays, axis in itertools.product(*[((A,B), (A,), (C,)), (0, 1, -1, None)]):
		if arrays[0].ndim == 1 and axis == 1:
			continue
		Alist = [i.tolist() for i in arrays]
		assert(np.array_equal(op(arrays, axis),np.asarray(concatenate_1(axis, *Alist))))
	for arrays, axis in itertools.product(*[((E, D)), (-1, None)]):
		Alist = [i.tolist() for i in arrays]		
		lhs = op(arrays, axis)
		rhs = np.asarray(concatenate_1(axis, *Alist))
		assert(np.array_equal(lhs,rhs))
