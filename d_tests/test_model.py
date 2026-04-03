"""Testes do modelo baseline."""

import numpy as np

from students_habits.cleaner import clean
from students_habits.loader import load_dataset
from students_habits.model.evaluator import r2, rmse
from students_habits.model.trainer import FEATURES, train


def test_train_returns_correct_shape(dataset_path):
    df = clean(load_dataset(dataset_path))
    coef = train(df)
    assert coef.shape == (len(FEATURES) + 1,)


def test_evaluator_metrics_are_finite(dataset_path):
    df = clean(load_dataset(dataset_path))
    coef = train(df)
    assert np.isfinite(rmse(df, coef))
    assert -1.0 <= r2(df, coef) <= 1.0
