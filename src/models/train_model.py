# -*- coding: utf-8 -*-
"""
@author: JulienWuthrich
"""
import repackage
repackage.up()


class Model(object):

    def __init__(self, verbose=1, n_jobs=1, random_state=42):
        self.verbose = verbose
        self.n_jobs = n_jobs
        self.score = None
        self.random_state = random_state

    def fit(self):
        pass

    def predict(self):
        pass

    def feature_importance(self):
        pass
