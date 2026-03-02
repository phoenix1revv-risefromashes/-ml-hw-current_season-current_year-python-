# Hmmm.. Same idea as before we previously did, but now we are using Scikit-learn for the ML part


import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class KNNRegression:

    def __init__(self, k: int):
        self.k = k
        self.points = None  # will store our dataset as a numpy array later
        self.model = KNeighborsRegressor(n_neighbors=k)  # scikit-learn does the heavy lifting

    def load_points(self, points: np.ndarray):
        # convert the list of points into a numpy array
        self.points = np.array(points, dtype=float)

    def train(self):
        x_vals = self.points[:, 0].reshape(-1, 1)  # scikit-learn needs x as a 2D array
        y_vals = self.points[:, 1]
        self.model.fit(x_vals, y_vals)  # train the model on our data

    def predict(self, x: float) -> float:
        # reshape x into the 2D format scikit-learn expects
        # Access the single element from the predicted array to avoid DeprecationWarning
        return float(self.model.predict(np.array([[x]]))[0])

    def label_variance(self) -> float:
        # variance of all y values in the training dataset
        return float(np.var(self.points[:, 1]))








def main():

    # read N with validation
    while True:
        try:
            N = int(input("Enter N (number of data points (positive integer only please): "))
            if N <= 0:
                print("  X  N must be greater than 0. Try again.\n")
                continue
            break
        except ValueError:
            print("  X  Please enter a whole number.\n")

    # read k with validation — also check k <= N right away
    while True:
        try:
            k = int(input("Enter k (number of neighbours (positive integers only please)): "))
            if k <= 0:
                print("  X  k must be greater than 0. Try again.\n")
                continue
            if k > N:
                print(f"  X  k ({k}) can't be greater than N ({N}). Enter a value between 1 and {N}.\n")
                continue
            break
        except ValueError:
            print("  X  Please enter a whole number.\n")

    # collect N points from the user
    print(f"\nEnter {N} points (x then y for each):")
    points = np.empty((N, 2), dtype=float)

    for i in range(N):
        while True:
            try:
                x_val = float(input(f"  Point {i + 1} (x) : "))
                y_val = float(input(f"  Point {i + 1} (y): "))
                points[i] = [x_val, y_val]
                break
            except ValueError:
                print("  X  Please enter a real number (e.g. 3.5).\n")

    # build the model, load data and train
    model = KNNRegression(k)
    model.load_points(points)
    model.train()

    # get query X and print prediction
    while True:
        try:
            X_query = float(input("\nEnter X to predict Y: "))
            break
        except ValueError:
            print("  X  Please enter a real number.\n")

    Y_pred = model.predict(X_query)
    variance = model.label_variance()





   
    print(f"""
--------------------------------------------------
  Method  : k-Nearest Neighbours (k-NN) Regression
  Library : Scikit-learn (KNeighborsRegressor)
  Dataset : {N} points  |  k = {k} neighbour(s)
  Query X : {X_query}
  
--------------------------------------------------
  Predicted Y        = {Y_pred:.6f}
  Variance of labels = {variance:.6f}
--------------------------------------------------

  The model found the {k} closest x value(s) to {X_query}
  and averaged their y values to produce the prediction.
  
  and,
  
  Variance here represents how spread out the y values are
  across the entire training dataset.
--------------------------------------------------""")


if __name__ == "__main__":
    main()