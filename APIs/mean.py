import shape, zeros, add, zeros_like, ones_like, mul
import itertools

def mean_1(a, axis=None, keepdims=None, where=None):
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

	output = zeros.zeros_1(shape_output)
	divisor = zeros.zeros_1(shape_output)

	for indices in itertools.product(*[list(range(j)) for j in new_shape_input]):
		inp = a
		out = output
		div = divisor
		whr = where_numeric
		prev_div = [div, None]
		prev_out = [out, None]
		for i, index in enumerate(indices):
			inp = inp[index]
			whr = whr[index]
			if index_flags[i] == True:
				prev_out = [out, index]
				prev_div = [div, index]
				out = out[index]
				div = div[index]
			elif index_flags[i] == False:
				prev_out = [out, 0]
				prev_div = [div, 0]
				out = out[0]
				div = div[0]
		if whr == 1:
			if prev_out[1] is not None:
				prev_div[0][prev_div[1]] += 1
				prev_out[0][prev_out[1]] += inp
			else:
				divisor += 1
				output += inp 	#Reduction results in a singleton value
				
	for indices in itertools.product(*[list(range(j)) for j in shape_output]):
		out = output
		div = divisor
		prev_out = [out, None]
		for i, index in enumerate(indices):
			prev_out = [out, index]
			out = out[index]
			div = div[index]
		if prev_out[1] is not None:
			if div == 0:
				prev_out[0][prev_out[1]] = float("nan")
			else:	
				prev_out[0][prev_out[1]] /= div
		else:
			if div == 0:
				output = float("nan")
			else:
				output /= div 	#Reduction results in a singleton value

	return output

def test_mean():
	import jax as jax
	import jax.numpy as np
	import operator
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	A = jrr(key, (2, 5, 3, 4), 0, 10)
	whr = jrr(key, (5,1,4), 0, 2)
	for a, axis, keepdims, where in itertools.product(*[(A), (None, 1, -1, [0,-1]), (True, False), (None, whr)]):
		res1 = np.mean(A, axis=axis, keepdims=keepdims, where=where)
		wherel = where.tolist() if where is not None else None
		res2 = np.asarray(mean_1(A.tolist(), axis=axis, keepdims=keepdims, where=wherel))
 
		assert(np.allclose(res1, np.asarray(res2), equal_nan=True))