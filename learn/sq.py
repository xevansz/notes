import pandas as pd
from tinygrad.tensor import Tensor
from tinygrad.nn import Linear
from tinygrad.nn.optim import Adam
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/LinkedInLearning/artificial-intelligence-foundations-neural-networks-4381282/refs/heads/main/Advertising_2023.csv"
df = pd.read_csv(url, index_col=0)

# print(df.head(10))
#     digital     TV  radio  newspaper  sales
# 1    345.15  156.0   37.8       69.2   22.1
# 2     66.75   46.0   39.3       45.1   10.4
# 3     25.80   18.3   45.9       69.3    9.3
# 4    227.25  145.1   41.3       58.5   18.5
# 5    271.20  165.2   10.8       58.4   12.9
# 6     13.05    8.7   48.9       75.0    7.2
# 7     86.25   57.5   32.8       23.5   11.8
# 8    180.30  120.2   19.6       11.6   13.2
# 9     12.90    8.6    2.1        1.0    4.8
# 10   299.70  199.8    2.6       21.2   10.6

# print(df.describe())
#            digital          TV        radio    newspaper        sales
# count  1199.000000  1199.00000  1199.000000  1199.000000  1199.000000
# mean    135.472394   146.61985    23.240617    30.529942    14.005505
# std     135.730821    85.61047    14.820827    21.712507     5.202804
# min       0.300000     0.70000     0.000000     0.300000     1.600000
# 25%      24.250000    73.40000     9.950000    12.800000    10.300000
# 50%      64.650000   149.70000    22.500000    25.600000    12.900000
# 75%     256.950000   218.50000    36.500000    45.100000    17.400000
# max     444.600000   296.40000    49.600000   114.000000    27.000000

# print(df.shape)
# (1199, 5)

# print(df.isnull().sum())
# 0

# Data Set Features
X = df[["digital", "TV", "radio", "newspaper"]]
Y = df["sales"]


# Normalization
def tiny_normalize(x: Tensor, axis=-1, epsilon=1e-12):
  # L2 Norm calculation: sqrt(sum(x^2))
  denom = (x**2).sum(axis=axis, keepdim=True).sqrt()
  return x / (denom + epsilon)


# Use it just like Keras
X_tensor = Tensor(X.values)
x_norm = tiny_normalize(X_tensor)

# print(x_norm.numpy())
# [[0.89211961 0.4032179  0.0977028  0.17886333]
#  [0.66254734 0.45658693 0.39008405 0.44765371]
#  [0.29009225 0.20576311 0.51609436 0.77920128]
#  ...
#  [0.06744611 0.99272247 0.05163843 0.08536149]
#  [0.19480049 0.91868871 0.08898294 0.33188231]
#  [0.06744611 0.99272247 0.05163843 0.08536149]]


# model
class Mymodel:
  def __init__(self):
    self.l1 = Linear(4, 16)  # 4 -> 16
    self.l2 = Linear(16, 8)  # 16 -> 8
    self.l3 = Linear(8, 1)

  def __call__(self, x: Tensor) -> Tensor:
    x = self.l1(x).relu()
    x = self.l2(x).relu()
    return self.l3(x)


model = Mymodel()

# Collect all parameters from your layers
parameters = [model.l1.weight, model.l1.bias, model.l2.weight, model.l2.bias, model.l3.weight, model.l3.bias]


def get_loss(model, x, y):
  pred = model(x)

  y = y.reshape(-1, 1)

  mse = (pred - y).square().mean()
  rmse = mse.sqrt()

  return mse, rmse


# Training
# 1. Normalize (Result is a Tinygrad Tensor)
X_norm_tensor = (X_tensor - X_tensor.min(axis=0)) / (X_tensor.max(axis=0) - X_tensor.min(axis=0) + 1e-10)

# 2. Convert to NumPy for the split
X_norm_np = X_norm_tensor.numpy()
Y_values = Y.values.reshape(-1, 1)

# 3. Split the NumPy arrays
x_train, x_test, y_train, y_test = train_test_split(X_norm_np, Y_values, test_size=0.4, random_state=101)

# 4. Convert back to Tinygrad Tensors for the model
X_train, Y_train = Tensor(x_train), Tensor(y_train)
X_test, Y_test = Tensor(x_test), Tensor(y_test)

optimizer = Adam(parameters, lr=0.01)

epochs = 1000

train_losses = []
val_losses = []

print(f"Training start for {epochs} epochs")
for i in range(epochs):
  Tensor.training = True
  mse, rmse = get_loss(model, X_train, Y_train)

  optimizer.zero_grad()
  mse.backward()
  optimizer.step()

  # Record Training Loss
  train_losses.append(mse.numpy())

  # Validation
  Tensor.training = False  # Turn off gradient tracking for validation
  val_mse, _ = get_loss(model, X_test, Y_test)

  # Record Validation Loss
  val_losses.append(val_mse.numpy())

  if i % 100 == 0 or i == epochs - 1:
    print(f"Epoch {i + 1:02d} | Train MSE: {mse.numpy():.4f} | Val MSE: {val_mse.numpy():.4f}")

# Test
test_mse, test_rmse = get_loss(model, X_test, Y_test)
print("Final Results")
print(f"Test MSE: {test_mse.numpy():.4f}")
print(f"Test RMSE: {test_rmse.numpy():.4f}")

# plot
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(train_losses, label="Training Loss (MSE)")
plt.plot(val_losses, label="Validation Loss (MSE)")
plt.title("Model Loss Progression")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()
