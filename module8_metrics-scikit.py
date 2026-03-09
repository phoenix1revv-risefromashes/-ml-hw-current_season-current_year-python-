# Mostly I build this one with the code stru from module 7 and adding the precision and recall

import numpy as np
from sklearn.metrics import precision_score, recall_score


class ClassificationMetrics:

    def __init__(self):
        self.points = None  # will store our dataset as a numpy array later

    def load_points(self, points: np.ndarray):
        # convert the list of points into a numpy array
        self.points = np.array(points, dtype=int)

    def precision(self) -> float:
        # scikit-learn calculates precision: TP / (TP + FP)
        return float(precision_score(self.points[:, 0], self.points[:, 1]))

    def recall(self) -> float:
        # scikit-learn calculates recall: TP / (TP + FN)
        return float(recall_score(self.points[:, 0], self.points[:, 1]))


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

    # collect N points from the user — x is true label, y is predicted label, both must be 0 or 1
    print(f"\nEnter {N} points (x = true label, y = predicted label, each must be 0 or 1):")
    points = np.empty((N, 2), dtype=int)

    for i in range(N):
        while True:
            try:
                x_val = int(input(f"  Point {i + 1} (x - true label)     : "))
                y_val = int(input(f"  Point {i + 1} (y - predicted label) : "))
                if x_val not in (0, 1) or y_val not in (0, 1):
                    print("  X  Both values must be either 0 or 1. Try again.\n")
                    continue
                points[i] = [x_val, y_val]
                break
            except ValueError:
                print("  X  Please enter 0 or 1.\n")

    # build the model and load data
    model = ClassificationMetrics()
    model.load_points(points)

    precision = model.precision()
    recall = model.recall()


    print(f"""
    
    
--------------------------------------------------
  Method  : Binary Classification Metrics (we used 0 for FALSE and 1 for TRUE)
  Library : Scikit-learn (precision_score, recall_score)
  Dataset : {N} samples
--------------------------------------------------  
  
  
--------------------------------------------------
  Precision = {precision:.6f}
  Recall    = {recall:.6f}
--------------------------------------------------


--------------------------------------------------
  Precision: of all predicted positives, how many
             were actually positive? (TP / (TP + FP))
             
             
  Recall   : of all actual positives, how many were
             correctly predicted? (TP / (TP + FN))
--------------------------------------------------""")


if __name__ == "__main__":
    main()
