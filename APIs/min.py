import shape, ones, add, ones_like, mul, zeros_like
import itertools

def min_1(a, axis=None, keepdims=None, initial=None, where=None):
	shape_input = shape.shape_1(a)
	dim_input = len(shape_input)

	if axis is None:
		axis = [i for i in range(dim_input)]
	elif isinstance(axis, int):
		axis = [axis]
	for i in range(len(axis)):
		if axis[i] < 0:
			axis[i] += dim_input

	if where is not None:
		where_numeric = ones_like.ones_like_1(where)
		for indices in itertools.product(*[list(range(j)) for j in shape.shape_1(where)]):
			out = where_numeric
			inn = where
			for i, index in enumerate(indices):
				inn = inn[index]
				if i + 1 == len(indices):
					out[index] = 1 if inn else 0 
				else:
					out = out[index]
		where_numeric = add.add_1(zeros_like.zeros_like_1(a), where_numeric)
		a = add.add_1(zeros_like.zeros_like_1(where_numeric), a)
	else:
		where_numeric = ones_like.ones_like_1(a)

	new_shape_input = shape.shape_1(a)
	new_dim_input = len(new_shape_input)

	shape_output = []
	index_flags = []
	for i_raw in range(new_dim_input):
		if i_raw < new_dim_input - dim_input:
			index_flags.append(None)
		else:
			i = i_raw - (new_dim_input - dim_input)
			if i in axis:
				if keepdims:
					shape_output.append(1)
					index_flags.append(False)
				else:
					index_flags.append(None)
			else:
				if shape_input[i] == new_shape_input[i_raw]:
					shape_output.append(shape_input[i])
					index_flags.append(True)
				else:
					shape_output.append(1)
					index_flags.append(False)

	output = ones.ones_1(shape_output)
	if initial is not None:
		output = mul.mul_1(output, initial)
	else:
		output = mul.mul_1(output, float("inf"))


	for indices in itertools.product(*[list(range(j)) for j in new_shape_input]):
		inp = a
		whr = where_numeric
		out = output
		prev_out = [out, None]
		for i, index in enumerate(indices):
			inp = inp[index]
			whr = whr[index]
			if index_flags[i] == True:
				prev_out = [out, index]
				out = out[index]
			elif index_flags[i] == False:
				prev_out = [out, 0]
				out = out[0]
		if whr == 1:
			if prev_out[1] is not None:
				if inp < prev_out[0][prev_out[1]]:
					prev_out[0][prev_out[1]] = inp
			else:
				if inp < output:
					output = inp 	#Reduction results in a singleton value
				
	return output

def test_min():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	A = jrr(key, (2, 5, 3, 4), -10, 10)
	whr = jrr(key, (5,1,4), 0, 2)
	for a, axis, keepdims, initial, where in itertools.product(*[(A), (None, 1, -1, [0,-1]), (True, False), (None, 7), (None, whr)]):
		try:
			res1 = np.min(A, axis=axis, keepdims=keepdims, initial=initial, where=where)
		except:
			continue
		wherel = where.tolist() if where is not None else None
		res2 = np.asarray(min_1(A.tolist(), axis=axis, keepdims=keepdims, initial=initial, where=wherel))  
		assert(np.allclose(res1, np.asarray(res2)))