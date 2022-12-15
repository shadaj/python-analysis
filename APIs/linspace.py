import sub, div, add, mul, shape
import transpose

def linspace_1(start, stop, num=50, endpoint=True, retstep=False, axis=0):
	diff = sub.sub_1(stop, start)
	out_shape = shape.shape_1(diff)
	if axis < 0:
		axis += (len(out_shape)+1)
	if endpoint:
		step = div.div_1(diff, num-1)
	else:
		step = div.div_1(diff, num)
	start_broadcast = add.add_1(start, mul.mul_1(0, step))

	res = []
	for i in range(num):
		res.append(start_broadcast)
		start_broadcast = add.add_1(start_broadcast, step)

	transpose_axis = []
	for i in range(len(out_shape)):
		if i == axis:
			transpose_axis.append(0)
		transpose_axis.append(i+1)
	if axis == len(out_shape):
		transpose_axis.append(0)

	res = transpose.transpose_1(res, transpose_axis)

	if retstep:
		return res, step
	else:
		return res

def test_linspace():
	import jax as jax
	import jax.numpy as np
	import operator
	import itertools
	key = jax.random.PRNGKey(2022)
	jrr = jax.random.randint
	A = jrr(key, (3, 2), 0, 10)
	B = jrr(key, (1, 3, 1), 0, 10)

	As = jax.numpy.asarray(7)
	Bs = jax.numpy.asarray(7)
	for start, stop, num, endpoint, retstep, axis in itertools.product(*[(A, As), (B, Bs), (17,), (True, False), (True, False), (0, 1, -1)]):
		if axis == 1 and start.ndim == 0 and stop.ndim == 0:
			continue
		res1 = np.linspace(start, stop, num=num, endpoint=endpoint, retstep=retstep, axis=axis)
		res2 = linspace_1(start.tolist(), stop.tolist(), num=num, endpoint=endpoint, retstep=retstep, axis=axis)
		if retstep:
			res2 = (np.asarray(res2[0]), np.asarray(res2[1]))
			assert(np.allclose(res1[0], res2[0]) and np.allclose(res1[1], res2[1]))
		else:
			assert(np.allclose(res1, np.asarray(res2)))