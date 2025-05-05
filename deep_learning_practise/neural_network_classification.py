from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch import nn

# make 1000 samples
n_samples = 1000

# create circles
# random state to get the smae value with noise
X, y = make_circles(n_samples, noise = 0.03, random_state= 42)
print(f"First 5 X features:\n{X[:5]}")
print(f"\nFirst 5 y labels:\n{y[:5]}")

circles = pd.DataFrame({"X1": X[:, 0],
                        "X2": X[:, 1],
                        "label": y})

print(circles.head(10))
print(circles.label.value_counts())

plt.scatter(x=X[:, 0],
            y=X[:, 1],
            c=y,
             cmap=plt.cm.RdYlBu)

# View the first example of features and labels
X_sample = X[0]
y_sample = y[0]
print(f"Values for one sample of X: {X_sample} and the same for y: {y_sample}")
print(f"Shapes for one sample of X: {X_sample.shape} and the same for y: {y_sample.shape}")

# loading data into tensors
X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float)

# split sata into traina and test

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42
                                                    )

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

# build a model

# Make device agnostic code
device = "cuda" if torch.cuda.is_available() else "cpu"

# X -> input feature y -> label

# 1. Construct a model class that subclasses the nn>Module
class CircleModelV0(nn.Module):
    def __init__(self):
        super().__init__()
        # 2. Create 2 nn.linear layers capable of handling X and y input and output shapes
        self.layer_1 = nn.Linear(in_features=2, out_features=5)
        self.layer_2 = nn.Linear(in_features=5, out_features=1)

    # 3. define the forward method
    def forward(self, x):
        # return the output of layer_2, a single feature,the same feature as y
        return self.layer_2(self.layer_1(x))

# 4. Instantiate the model and then send it to the target device
model_0 = CircleModelV0().to(device)

# trying with nn.Sequential
model_0 = nn.Sequential(
    nn.Linear(in_features=2, out_features=5),
    nn.Linear(in_features=5, out_features=1)
).to(device)

# Make predictions with the model
untrained_preds = model_0(X_test.to(device))
print(f"Length of predictions: {len(untrained_preds)}, Shape: {untrained_preds.shape}")
print(f"Length of test samples: {len(y_test)}, Shape: {y_test.shape}")
print(f"\nFirst 10 predictions:\n{untrained_preds[:10]}")
print(f"\nFirst 10 test labels:\n{y_test[:10]}")

# 5. create a loss function
# with sigmoid built in
loss_fn = nn.BCEWithLogitsLoss()

# 6. create an optimizer
optimizer = torch.optim.SGD(params=model_0.parameters(),
                            lr=0.1)

# writing an accuracy function
def accuracy_fn(y_true, y_pred):
    # calculates where two tensors are equal
    correct = torch.eq(y_true, y_pred).sum().item()
    acc = (correct / len(y_pred)) * 100
    return acc

# 7. train model

# view the first 5 predictions of the forwards pass on the test data
# output of a model is a in the form of logits
y_logits = model_0(X_test.to(device))[:5]

# use sigmoid to convert the logits to probabilities
y_pred_probs = torch.sigmoid(y_logits)

# find the predicted labels (rounding the prediction probabilities)
y_preds = torch.round(y_pred_probs)
y_pred_labels = torch.round(torch.sigmoid(model_0(X_test.to(device))[:5]))

# removing extra dimension
y_pred_labels = y_pred_labels.squeeze()

print(f"First 5 predictions:\n{y_pred_labels[:5]}")

torch.manual_seed(42)

# set the number of epochs
epochs = 100

# putting the data on the target device
X_train, y_train = X_train.to(device), y_train.to(device)
x_test, y_test = X_test.to(device), y_test.to(device)

# building training and eval loop
for epohs in range(epochs):
    
    # training
    model_0.train()

    # 1. Forward pass (model outputs raw logits)
    y_logits = model_0(X_train).squeeze()
    # logits -> probabilities -> prediction labels
    y_pred = torch.round(torch.sigmoid(y_logits))

    # 2. Calculate the loss and accuracy
    loss = loss_fn(y_logits, y_train)
    acc = accuracy_fn(y_true=y_train, y_pred=y_pred)

    # 3. Optimizer zero grad
    optimizer.zero_grad()

    # 4. loss backwards
    loss.backward()

    # 5. optimizer step
    optimizer.step()

    # testing
    model_0.eval()
    with torch.inference_mode():
        # 1.forward pass
        test_logits = model_0(x_test).squeeze()
        test_pred = torch.round(torch.sigmoid(test_logits))
        # 2. calculate the loss and acccuracy
        test_loss = loss_fn(test_logits, y_test)
        test_acc = accuracy_fn(y_true=y_test, y_pred=test_pred)

    # printing the results for 1-10 epochs
    if epochs % 10 == 0:
        print(f"Epoch: {epohs} | "
              f"Train loss: {loss:.5f} | "
              f"Train acc: {acc:.2f}% | "
              f"Test loss: {test_loss:.5f} | "
              f"Test acc: {test_acc:.2f}%")
        print(f"First 10 test predictions:\n{test_pred[:10]}")
