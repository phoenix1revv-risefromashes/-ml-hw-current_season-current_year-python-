#This was actually the fun programming

import numpy as np

#Creating the blueprint of program

class KNNRegression:

    def __init__(self, k: int):
        self.k = k
        self.points = None  # will store our dataset as a numpy array later

    def load_points(self, points: np.ndarray):
        # convert the list of points into a numpy array
        self.points = np.array(points, dtype=float)

    def predict(self, x: float) -> float:
        x_vals = self.points[:, 0]  # all x values from dataset
        y_vals = self.points[:, 1]  # all y values from dataset

        # calculate how far each x in dataset is from our query x
        distances = np.abs(x_vals - x)

        # get the indices of the k closest points
        k_indices = np.argpartition(distances, self.k)[:self.k]

        # prediction = average y of the k nearest neighbours
        return float(np.mean(y_vals[k_indices]))


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

    # build the model and load data
    model = KNNRegression(k)
    model.load_points(points)

    # get query X and print prediction
    while True:
        try:
            X_query = float(input("\nEnter X to predict Y: "))
            break
        except ValueError:
            print("  X  Please enter a real number.\n")

    Y_pred = model.predict(X_query)

    # print a meaningful summary of the result
    print(f"""
    Here is the Summary:
    
--------------------------------------------------
  Method  : k-Nearest Neighbours (k-NN) Regression
  Dataset : {N} points  |  k = {k} neighbour(s)
  Query X : {X_query}
  
--------------------------------------------------
  Predicted Y = {Y_pred:.6f}
--------------------------------------------------

  The model found the {k} closest x value(s) to {X_query}
  and averaged their y values to produce the prediction.
--------------------------------------------------""")


if __name__ == "__main__":
    main()