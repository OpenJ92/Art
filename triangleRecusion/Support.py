class Support:
    def __init__(self, seed):
        self.seed = seed
        self.tensor_ = self.make_tensor()

    def make_tensor(self):
        return 0

if __name__ == "__main__":
    import numpy as np

    A = np.random.random_sample(size = (3, 3))
    s = Support(A)


