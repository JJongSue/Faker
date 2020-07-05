from abc import abstractmethod, abstractproperty, ABCMeta
import numpy as np

class Evaluator(metaclass=ABCMeta):
    """Base class for evaluation functions."""
    
    @abstractproperty
    def worst_score(self):
        """
        The worst performance score.
        :return float.
        """
        pass
    @abstractproperty
    def mode(self):
        """
        the mode for performance score, either 'max' or 'min'
        e.g. 'max' for accuracy, AUC, precision and recall,
              and 'min' for error rate, FNR and FPR.
        :return: str.
        """
        pass

    @abstractmethod
    def score(self, fid, sample_images):
        """
        Performance metric for a given prediction.
        This should be implemented.
        :param fid: FID object to calculate fid.
        :param sample_images: np.ndarray, shape: (N, 128, 128, 3).
        :return float.
        """
        pass

    @abstractmethod
    def is_better(self, curr, best, **kwargs):
        """
        Function to return whether current performance score is better than current best.
        This should be implemented.
        :param curr: float, current performance to be evaluated.
        :param best: float, current best performance.
        :return bool.
        """
        pass

    
class FIDEvaluator(Evaluator):
    """Evaluator with FID score"""
    
    @property
    def worst_score(self):
        """The worst performance score."""
        return 1000.0

    @property
    def mode(self):
        """The mode for performance score."""
        return 'min'

    def score(self, sess, fid, model,**kwargs):
        """Compute Recall for a given predicted bboxes"""
        batch_size_eval = kwargs.pop('batch_size_eval', 50)
        eval_sample_size = kwargs.pop('eval_sample_size', 10000)
        n_iter = eval_sample_size // batch_size_eval
        fid.reset_FID()
        for i in range(n_iter):
            z_eval = np.random.uniform(-1.0, 1.0, size=(batch_size_eval, model.z_dim)).astype(np.float32)
            eval_generated = model.generate(sess, z_eval, verbose=False, **kwargs)
            fid.extract_inception_features(eval_generated)
        score = fid.calculate_FID()
        return score

    def is_better(self, curr, best, **kwargs):
        """
        Return whether current performance scores is better than current best,
        with consideration of the relative threshold to the given performance score.
        :param kwargs: dict, extra arguments.
            - score_threshold: float, relative threshold for measuring the new optimum,
                               to only focus on significant changes.
        """
        score_threshold = kwargs.pop('score_threshold', 1e-4)
        relative_eps = 1.0 - score_threshold
        return curr < best * relative_eps