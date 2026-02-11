class KNNModel:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def train(self, X, y):
        if X and not isinstance(X[0], (list, tuple)):
            self.X_train = [[x] for x in X]
        else:
            self.X_train = X
        self.y_train = y
    
    def _euclidean_distance(self, point1, point2):
        return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5
    
    def predict(self, X):
        if self.X_train is None or self.y_train is None:
            raise ValueError("Model must be trained before making predictions")
        
        if X and not isinstance(X[0], (list, tuple)):
            X = [[x] for x in X]
        
        predictions = []
        
        for x in X:
            distances = []
            for i, x_train in enumerate(self.X_train):
                dist = self._euclidean_distance(x, x_train)
                distances.append((dist, self.y_train[i]))
            
            distances.sort(key=lambda x: x[0])
            k_nearest = distances[:self.k]
            
            k_labels = [label for _, label in k_nearest]
            
            prediction = max(set(k_labels), key=k_labels.count)
            predictions.append(prediction)
        
        return predictions