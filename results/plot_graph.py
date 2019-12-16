from sys import argv

# Text file parser

file_path = ''
action = '' # acc, loss, res

if len(argv) >= 2:
	file_path = argv[1]

if len(argv) >= 3:
	action = argv[2]

epoch_list = []
val_acc_list = []
train_acc_list = []
loss_list = []

best_epoch = 0
best_val_acc = 0.0
best_recall = 0.0
best_precision = 0.0
best_F1 = 0.0

with open(file_path, 'r') as f:
	for line in f.readlines():
		line = line.strip()
		elements = line.split(' ')

		if 'Evaluate' in line and 'accuracy' in line:
			epoch = int(elements[2])
			val_acc = float(elements[4])
			epoch_list.append(epoch)
			val_acc_list.append(val_acc)

			if val_acc > best_val_acc:
				best_val_acc = val_acc
				best_epoch = epoch

		if 'tarin accuracy' in line:
			epoch = int(elements[1])
			train_acc = float(elements[4])
			train_acc_list.append(train_acc)

		if 'loss' in line:
			epoch = int(elements[1])
			loss = float(elements[3])
			loss_list.append(loss)

		if 'precision' in line:
			precision = float(elements[4])
			if precision > best_precision:
				best_precision = precision

		if 'recall' in line:
			recall = float(elements[4])
			if recall > best_recall:
				best_recall = recall

		if 'F1' in line:
			F1 = float(elements[4])
			if F1 > best_F1:
				best_F1 = F1



def print_result():
	print(len(epoch_list))
	print(len(val_acc_list))
	print(len(train_acc_list))
	print(len(loss_list))
	print('best_val_acc: {}'.format(best_val_acc))
	print('best_epoch: {}'.format(best_epoch))
	print('best_precision: {}'.format(best_precision))
	print('best_recall: {}'.format(best_recall))
	print('best_F1: {}'.format(best_F1))


import matplotlib.pyplot as plt

def plot_acc():
	plt.plot(epoch_list, val_acc_list, label='val accuracy')
	plt.plot(epoch_list, train_acc_list[:len(epoch_list)], label='train accuracy')
	plt.xlabel('Epoch #')
	plt.ylabel('Accuracy')
	plt.legend()
	plt.show()

def plot_loss():
	plt.plot(epoch_list, loss_list[:len(epoch_list)], label='loss')
	plt.xlabel('Epoch #')
	plt.ylabel('Traning loss')
	plt.show()


if action == 'acc':
	plot_acc()

if action == 'loss':
	plot_loss()

if action == 'res':
	print_result()



