# from features_organizer import FeaturesOrganizer
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import seaborn as sns
from collections import Counter

def mean_and_cov(all_data, labels, n_states, n_feature):
	""" Compute the means and covariance matrix for each state 

	Return a vector of scalar and a vector of matrix corresponding to the mean 
	of the distribution and the covariance
	"""

	data = [[]]
	for i in range(n_states - 1):
		data.append([])

	for i in range(len(labels)):
		num_state = labels[i]
		if(len(data[num_state])<=0):
			data[num_state].append(all_data[i])
		else:
			data[num_state] = np.vstack((data[num_state], all_data[i]))

	sigma = np.zeros(((n_states,n_feature,n_feature)))
	mu = np.zeros((n_states, np.sum(n_feature)))

	for i in range(n_states):
		mu[i] = np.mean(data[i], axis=0)
		sigma[i] = np.cov(data[i].T)

	return mu, sigma



# def generate_list_features(n_features, possible_features):
# 	list_features = []
# 	dim_features = []
# 	for i in range(n_features):
# 		id_feature = int(np.floor(np.random.rand() * (len(possible_features[0]))))

# 		while((possible_features[0][id_feature] in list_features) or 
# 			((possible_features[0][id_feature] == 'CoMZ') and ('centerOfMass' in list_features)) or
# 			((possible_features[0][id_feature] == 'centerOfMass') and ('CoMZ' in list_features))):

# 			id_feature = int(np.floor(np.random.rand() * (len(possible_features[0]))))
# 		list_features.append(possible_features[0][id_feature])
		

# 	for id_feature in range(len(list_features)):
# 		index = possible_features[0].index(list_features[id_feature])
# 		dim_features.append(possible_features[1][index])

# 	return list_features, dim_features

# def update_list_name_features(list_features, list_all_features, list_name_features):
# 	name_features = []
# 	for features in list_features:
# 		index = list_all_features.index(features)
# 		name_features.append(list_name_features[index])
# 	return name_features


# def slide_windows(data, size_window):
# 	win = int(size_window/2)
# 	data_out = []

# 	for i in np.arange(win, len(data)-win, win):
# 		average = np.mean(data[i-win : i+win+1], axis=0)
# 		data_out.append(average)

# 	data_windows = np.zeros((np.shape(data_out)))
# 	for i in range(len(data_out)):
# 		data_windows[i,:] = data_out[i]
# 	return data_windows


# def all_data_concatenate(list_features, all_data):
# 	data_conc = []
# 	for features in list_features:
# 		data = all_data.get_data_by_features(features)
# 		if(len(data_conc)<=0):
# 			data_conc = data
# 		else:
# 			data_conc = np.hstack((data_conc, data))
# 	return data_conc

# def set_name_ouput(list_features, all_features, name_features):
# 	features_sorted = sorted(all_features)
# 	id_feature = all_features.index(list_features[0])
# 	name_output_file = name_features[id_feature]
# 	name_output = []
# 	name_output.append(name_features[id_feature])
# 	for i in range(1, len(list_features)):
# 		id_feature = all_features.index(list_features[i])
# 		name_output_file += '_' + name_features[id_feature]
# 		name_output.append(name_features[id_feature])
# 	name_output = sorted(name_output)
# 	name_output_file = name_output[0]
# 	for i in range(1, len(name_output)):
# 		name_output_file += '_' + name_output[i]
# 	return name_output_file

# def compute_confusion_matrix(pred_labels, real_labels, list_states):
# 	n_states = len(list_states)
# 	confusion_matrix = np.zeros((n_states, n_states)).astype(int)
# 	confusion_next = np.zeros((n_states, n_states)).astype(int)
# 	confusion_prev = np.zeros((n_states, n_states)).astype(int)
# 	confusion_error = np.zeros((n_states, n_states)).astype(int)

# 	for state in list_states:
# 		index = list_states.tolist().index(state)
# 		print(index, state)
# 	print(Counter(real_labels))
# 	print(Counter(pred_labels))

# 	# print(np.shape(real_labels), np.shape(pred_labels))
# 	for j in range(len(real_labels)):
# 		index_real = list_states.tolist().index(real_labels[j])
# 		index_pred = list_states.tolist().index(pred_labels[j])
# 		confusion_matrix[index_real, index_pred] += 1
# 		if(index_real != index_pred):
# 			if(j < len(real_labels) - 1):
# 				next_index = list_states.tolist().index(real_labels[j + 1])
# 			else:
# 				next_index = index_real
# 			if(j > 0):
# 				prev_index = list_states.tolist().index(real_labels[j - 1])
# 			else:
# 				prev_index = index_real
			
# 			if(next_index == index_pred):
# 				confusion_next[next_index, index_pred] += 1
# 				confusion_error[next_index, index_pred] += 1
# 			elif(prev_index == index_pred):
# 				confusion_prev[prev_index, index_pred] += 1
# 				confusion_error[prev_index, index_pred] += 1
# 			else:
# 				confusion_error[index_real, index_pred] += 1
			
# 		else:
# 			confusion_error[index_real, index_pred] += 1

# 	# print(confusion_prev)
# 	# print(confusion_next)
# 	# print(confusion_matrix)
# 	# print(confusion_error)


# 	# c = csv.writer(open(path + 'confusion_matrix.csv', "w", newline=''))
# 	# c.writerow(list_states)
# 	# for i in range(n_states):
# 	# 	line = [list_states[i]]
# 	# 	for j in range(n_states):
# 	# 		line.append(confusion_matrix[i, j])
# 	# 	c.writerow(line)

# 	return confusion_matrix.astype(int), confusion_error.astype(int)


# def normalize_data(data, xmin, xmax):
# 	data_norm = 2*(data - xmin)/(xmax - xmin) - 1
# 	return data_norm

# # def compute_results(model, path):
# # 	data_test = model.get_data_test()
# # 	print('size', np.shape(data_test))
# # 	index = model.get_test_set_index()
# # 	print('index', index)
# # 	labels = model.get_ref_labels(index[0])
# # 	print(len(labels))
# # 	list_states = model.get_list_states()

# # 	obs = data_test[0][0]
# # 	Z = model.predict(obs)

# # 	pred_labels = []
# # 	for j in range(len(Z)):
# # 		pred_labels.append(list_states[Z[j]])

# # 	list_states = model.get_list_states()

# # 	confusion_matrix = compute_confusion_matrix(pred_labels, labels, list_states, path)
# # 	return confusion_matrix



# # save confusion matrix in csv file
# def save_confusion_matrix(name_file, path, confusion_matrix, labels):
# 	c = csv.writer(open(path + name_file + '_confusion.csv', "w", newline=''))
# 	line = []
# 	for i in range(len(labels)):
# 		line.append(labels[i].title())
# 	c.writerow(line)
# 	for i in range(len(labels)):
# 		line = [labels[i].title()]
# 		for j in range(len(labels)):
# 			line.append(confusion_matrix[i, j])
# 		c.writerow(line)
# 	return

# def plot_confusion_matrix2(path, name, title, confusion_matrix, labels, save=0):
# 	real_len, pred_len = np.shape(confusion_matrix)

# 	precision_map = np.zeros((real_len, pred_len))
# 	recall_map = np.zeros((real_len, pred_len))
# 	for i in range(real_len):
# 		for j in range(pred_len):
# 			precision_map[i, j] = confusion_matrix[i, j] / np.sum(confusion_matrix[i])
# 			recall_map[i, j] = confusion_matrix[i, j] / np.sum(confusion_matrix[:,j])


# 	precision_map = np.around(precision_map, 4)*100
# 	recall_map = np.around(recall_map, 4)*100

# 	precision_pd = pd.DataFrame(data = precision_map, 
# 				index = labels
# 				, columns = labels
# 				)


# 	recall_pd = pd.DataFrame(data = recall_map, 
# 			index = labels
# 			,columns = labels
# 			)

# 	# recall_total, prec_total, F1_score = np.around(compute_score(confusion_matrix), 4)*100

# 	fig = plt.figure()
# 	sns.set(font_scale = 1.5)
# 	# ax1 = plt.subplot("121")
# 	sns.heatmap(recall_pd, vmax=100., annot=True, fmt='g', cbar=False)
# 	# ax1.set_title('Recall (%) map - Total = ' + str(recall_total))
# 	plt.yticks(rotation=0) 
# 	plt.xticks(rotation=45)
# 	plt.ylabel('Real labels')
# 	plt.xlabel('Predict labels')

# 	plt.title('Recall')

# 	if(save):
# 		plt.savefig(name + '_recall.pdf', bbox_inches='tight')

# 	fig = plt.figure()

# 	# ax2 = plt.subplot("122")
# 	sns.heatmap(precision_pd, vmax=100., annot=True, label='big', fmt='g', cbar=False)
# 	# ax2.set_title('Precision (%) map - Total = ' + str(prec_total))
# 	plt.yticks(rotation=0)
# 	plt.xticks(rotation=45)
# 	plt.ylabel('Real labels')
# 	plt.xlabel('Predict labels')

# 	plt.title('Precision')

# 	if(save):
# 		plt.savefig(name + '_precision.pdf', bbox_inches='tight')

# 	return


# def plot_confusion_matrix(path, name, title, confusion_matrix, labels, save=0):
# 	real_len, pred_len = np.shape(confusion_matrix)

# 	fig = plt.figure(figsize=(12,10))
# 	sns.set(font_scale = 2.5)
# 	plt.title(title, fontsize=35)
# 	# ax1 = plt.subplot("121")
# 	sns.heatmap(confusion_matrix, annot=True, fmt='g', cbar = False)
# 	# ax1.set_title('Recall (%) map - Total = ' + str(recall_total))
# 	plt.yticks(rotation=0) 
# 	plt.xticks(rotation=45)
# 	plt.ylabel('Real labels', fontsize=30)
# 	plt.xlabel('Predicted labels', fontsize=30)

# 	if(save):
# 		plt.savefig(path + name + '.pdf', bbox_inches='tight')
# 	return

# def plot_confusion_matrix_df(confusion_matrix):
# 	print('aaa\n', confusion_matrix)
# 	real_len, pred_len = np.shape(confusion_matrix)

# 	fig = plt.figure()
# 	sns.set(font_scale = 1.5)
# 	# ax1 = plt.subplot("121")
# 	sns.heatmap(confusion_matrix, annot=True, fmt='g', cbar = False)
# 	# ax1.set_title('Recall (%) map - Total = ' + str(recall_total))
# 	plt.yticks(rotation=0) 
# 	plt.xticks(rotation=45)
# 	plt.ylabel('Real labels')
# 	plt.xlabel('Predict labels')

# 	plt.title('Confusion Matrix')

# 	return fig

# def save_tab_score(name_file, path, features, scores):
# 	scores = np.around(np.asarray(scores)*100, decimals = 2)
# 	c = csv.writer(open(path + name_file + '_performance.csv', "w", newline=''))
# 	c.writerow(['Features', 'Precision', 'Recall', 'F1-Score'])
# 	for i in range(len(scores)):
# 		line = [features[i]]
# 		for j in range(len(scores[i])):
# 			line.append(scores[i][j])
# 		c.writerow(line)
# 	return

# def read_confusion_file(path_file):
# 	confusion_matrix = np.zeros((1, 1))
# 	cr = csv.reader(open(path_file, "r"))
# 	# cr = csv.reader(open(path_model + name + '/' + name_csv_file,"r"))
# 	i = -1
# 	for row in cr:
# 		if(i == -1):
# 			labels = row
# 			confusion_matrix = np.zeros((len(labels), len(labels)))
# 			i += 1
# 		else:
# 			if(row == []):
# 				continue
# 			confusion_matrix[i] = row[1:]
# 			i += 1
# 	return confusion_matrix, labels





# def compute_score(confusion_matrix):
# 	n_states = len(confusion_matrix)
# 	precision = np.zeros((n_states, 1))
# 	recall = np.zeros((n_states, 1))

# 	for j in range(n_states):
# 		TP = confusion_matrix[j,j]
# 		recall[j] = TP/np.sum(confusion_matrix[j])
# 		precision[j] = TP/np.sum(confusion_matrix[:,j])
# 		if(np.isnan(recall[j])):
# 			recall[j] = 0
# 		if(np.isnan(precision[j])):
# 			precision[j] = 0
		
# 	prec_total = np.sum(precision)/n_states
# 	recall_total = np.sum(recall)/n_states
# 	F1_score = 2 * (prec_total * recall_total)/(prec_total + recall_total)

# 	return prec_total, recall_total, F1_score

# def get_accuracy(confusion_matrix):
# 	n_states = len(confusion_matrix)
# 	accuracy = np.sum(np.diag(confusion_matrix))/np.sum(confusion_matrix)
# 	return accuracy



# def update_best_features(best_features, best_scores, best_n_festures, scores, features_name
# 						, nb_features, n_best, best_path, path, size_window, win):
# 	if(best_scores[0][2] == 0):
# 		best_scores[0] = scores
# 		best_features.append(features_name)
# 		best_path.append(path)
# 		best_n_festures[0] = int(nb_features)
# 		win.append(size_window)
# 	else:
# 		for i in range(len(best_scores)):
# 			if(scores[2] > best_scores[i][2]):
# 				best_scores.insert(i, scores)
# 				best_features.insert(i, features_name)
# 				best_path.insert(i, path)
# 				best_n_festures.insert(i, int(nb_features))
# 				win.insert(i, size_window)
# 				if(len(best_scores) > n_best):
# 					del best_scores[-1]
# 					del best_features[-1]
# 					del best_n_festures[-1]
# 					del best_path[-1]
# 					del win[-1]
# 				break
				
# 			elif(i == (len(best_scores)-1)):
# 				best_scores.append(scores)
# 				best_features.append(features_name)
# 				best_n_festures.append(int(nb_features))
# 				best_path.append(path)
# 				win.append(size_window)
# 				if(len(best_scores) > n_best):
# 					del best_scores[-1]
# 					del best_features[-1]
# 					del best_n_festures[-1]
# 					del win[-1]
# 				break	
# 	return


# def csv_to_latex(csv_file):
# 	latex_tab = pd.read_csv(csv_file, sep=',', index_col = 0)
# 	return latex_tab.to_latex()


# def plot_labels(label_sequence, list_labels):

# 	return