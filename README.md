# cars model on Raspberry PI

Train simply an automl model using h2o automl (see `cars_model.ipynb`) notebook

Resulting mojo can be used on the RPI for scoring, bring .zip and .jar file to RPI and see (`h2o_PI_score_test.py`). You must install the h2o python package and java on the raspberry pi. This script displays the prediction on a led matrix, so the that needs to be setup as well.