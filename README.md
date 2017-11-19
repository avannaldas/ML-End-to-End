# ML-End-to-End

This is an End-to-End bare minimum boilerplate Machine Learning application.

Steps...
  1. Loads a toy dataset
  2. Performs dummy preprocess step through a data wrangler middleware
  3. Trains a model and saves it to disk
  4. Prediction service uses data_wrangler middleware to preprocess and predict the requests received through a Flask REST API layer.

Application contains...

  | File | Purpose |
  |------|---------|
  | ML Classifier Sample.ipynb | The classifier, where model is trained |
  | data_wrangler.py | Represents middleware to pre-processes data. Consumed by both, training and prediction steps | 
  | Prediction Service.ipynb | Flask REST API which consumes trained model through data_wrangler |
  | iris_clf_model.pkl | Model saved to disk |


P.S.: _This is a first cut boilerplate. I'm planning to improve, extend this as and when this can be prioritized, keeping it as generic as possible to be re-used. Ideas, suggestions, contributions welcome :)_
