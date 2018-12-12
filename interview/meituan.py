# tensorflow_l2.py
import tensorflow as tf

X = tf.placeholder(tf.float32,[1092,784])
w = tf.Variable(tf.zeros([794, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.placeholder(tf.float32, [10])

y_pred = tf.matmul(w,x) + b

mse_loss = tf.reduce_mean(tf.reduce_sum(tf.square(y - y_pred)), reduction_indices=[1])
regularizer = tf.contrib.layers.l2_regularizer(regularizetion_rate)
regularization = regularizer(w)

loss = mse_loss + regularization

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-3)
train_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(100)
	sess.run(train_op, feed_dict={x:x_data, y:y_data})
	if i % 50 == 0:
		print(sess.run(loss, feed_dict={x:x_data, y:y_data}))

# quick_sort.py
def quick_sort(arr, start, end):
	if start < end:
		index = partition(arr, start, end)
		quick_sort(arr, start, index)
		quick_sort(arr, index+1, end)

def partition(a, start, end):
	i = start - 1
	for j in range(start, end):
		if a[j] <= a[end]:
			i += 1
			a[i], a[j] = a[j], a[i]
	a[i+1], a[end] = a[end], a[i+1]
	return i