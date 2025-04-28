import torch
from torch import nn
import matplotlib.pyplot as plt

# Setup device agnostic code
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# creating weights and bias
weight = 0.7
bias = 0.3

# creating range values
start = 0
end = 1
step = 0.02

# Create X and y (feature labels)
X = torch.arange(start, end, step).unsqeeze(dim=1)
y = weight * X + bias

# split data
# 80 % training data and 20 % testing data
train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

# plot_predictions(X_train, y_train, X_test, y_test)

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()

        # creating model parameters
        self.linear_layer = nn.Linear(in_features = 1,
                                      out_features = 1)
        
        # defining the forward computation
        def forward(self, x:torch.Tensor) -> torch.Tensor:
            return self.linear_layer(x)

torch.manual_seed(42)
model_1 = LinearRegressionModel()
model_1.to(device) # the device variable was set above to be "cuda" if available or "cpu" if not
next(model_1.parameters()).device

# creating loss function
loss_fn = nn.L1Loss()

# creating optimizer
optimizer = torch.optim.SGD(params = model_1.parameters(),lr=0.01) 

# number of epochs
epochs = 1000

# putting the data on the available device
X_train = X_train.to(device)
X_test = X_test.to(device)
y_train = y_train.to(device)
y_test = y_test.to(device)

for epoch in range(epochs):
    # Training
    model_1.train()

    # 1. forward pass
    y_pred = model_1(X_train)

    # 2. calculate loss
    loss = loss_fn(y_pred, y_train)

    # 3. zero grad optimizer
    optimizer.zero_grad()

    # 4. loss backwards
    loss.backward()

    # 5. step the optimizer
    optimizer.zero_grad()

    # Testing
    # model in evaluation mode for testing (inference)
    model_1.eval()
    
    with torch.inference_mode():
        test_pred = model_1(X_test)

        test_loss = loss_fn(test_pred, y_test)

    if epochs % 100 == 0:
        print(f"Epochs: {epoch} | Train loss: {loss} | Test loss: {test_loss}")

if __name__ == "__main__":
    # Find our model's learned parameters
    from pprint import pprint # pprint = pretty print, see: https://docs.python.org/3/library/pprint.html 
    print("The model learned the following values for weights and bias:")
    pprint(model_1.state_dict())
    print("\nAnd the original values for weights and bias are:")
    print(f"weights: {weight}, bias: {bias}")
