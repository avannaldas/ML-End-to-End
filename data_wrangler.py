def pre_process_data(d):
	# do whatever required
	return d

def predict(d):
	from sklearn.externals import joblib
	model = joblib.load('iris_clf_model.pkl')
	return model.predict(d)

def pre_process_and_predict(d):
	return predict(pre_process_data(d))
