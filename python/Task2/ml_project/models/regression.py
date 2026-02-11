class LinearRegModel:
    def __init__(self):
        self.coefficients = None
        self.intercept = None
    
    def fit(self, X, y):
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        n = len(X)
        
        X_means = [sum(col) / n for col in zip(*X)]
        y_mean = sum(y) / n
        
        if len(X[0]) == 1:
            numerator = sum((X[i][0] - X_means[0]) * (y[i] - y_mean) for i in range(n))
            denominator = sum((X[i][0] - X_means[0]) ** 2 for i in range(n))
            
            if denominator == 0:
                self.coefficients = [0]
            else:
                self.coefficients = [numerator / denominator]
            
            self.intercept = y_mean - self.coefficients[0] * X_means[0]
        else:
            self.coefficients = [0] * len(X[0])
            self.intercept = y_mean
    
    def predict(self, X):
        if self.coefficients is None:
            raise ValueError("Model must be fitted before making predictions")
        
        if isinstance(X[0], (int, float)):
            X = [[x] for x in X]
        
        predictions = []
        for x in X:
            pred = self.intercept + sum(coef * val for coef, val in zip(self.coefficients, x))
            predictions.append(pred)
        
        return predictions