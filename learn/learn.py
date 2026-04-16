from tinygrad import Tensor, nn
from tinygrad.device import Device

Device.DEFAULT = "CUDA"


class Model:
  def __init__(self):
    self.l1 = nn.Conv2d(1, 32, kernel_size=(3, 3))
    self.l2 = nn.Conv2d(32, 64, kernel_size=(3, 3))
    self.l3 = nn.Linear(1600, 10)

  def __call__(self, x: Tensor) -> Tensor:
    x = self.l1(x).relu().max_pool2d((2, 2))
    x = self.l2(x).relu().max_pool2d((2, 2))
    return self.l3(x.flatten(1).dropout(0.5))


from tinygrad.nn.datasets import mnist

X_train, Y_train, X_test, Y_test = mnist()
# print(X_train.shape, X_train.dtype, Y_train.shape, Y_train.dtype)
# (60000, 1, 28, 28) dtypes.uchar (60000,) dtypes.uchar

model = Model()
acc = (model(X_test).argmax(axis=1) == Y_test).mean()
# NOTE: tinygrad is lazy, and hasn't actually run anything by this point
# print(acc.item())  # ~10% accuracy, as expected from a random model

optim = nn.optim.Adam(nn.state.get_parameters(model))
batch_size = 128


def step():
  Tensor.training = True
  samples = Tensor.randint(batch_size, high=X_train.shape[0])
  X, Y = X_train[samples], Y_train[samples]
  optim.zero_grad()
  loss = model(X).sparse_categorical_crossentropy(Y).backward()
  optim.step()
  return loss


from tinygrad import TinyJit

jit_step = TinyJit(step)

import timeit

# timeit.repeat(jit_step, repeat=5, number=1)
# [4.4055279530002736, 1.084696724999958, 0.0032243920031760354, 3.306299913674593e-05, 2.1119001758052036e-05]

for step in range(7000):
  loss = jit_step()
  if step % 100 == 0:
    Tensor.training = False
    acc = (model(X_test).argmax(axis=1) == Y_test).mean().item()
    print(f"step {step:4d}, loss {loss.item():.2f}, acc {acc * 100.0:.2f}%")

"""
step    0, loss 48.02, acc 13.54%
step  100, loss 0.34, acc 95.05%
step  200, loss 0.14, acc 96.53%
step  300, loss 0.26, acc 96.81%
step  400, loss 0.15, acc 96.98%
step  500, loss 0.06, acc 97.28%
step  600, loss 0.17, acc 97.44%
step  700, loss 0.13, acc 97.37%
step  800, loss 0.02, acc 97.47%
step  900, loss 0.10, acc 97.48%
step 1000, loss 0.10, acc 97.72%
step 1100, loss 0.20, acc 97.82%
step 1200, loss 0.10, acc 97.95%
step 1300, loss 0.10, acc 97.81%
step 1400, loss 0.03, acc 97.92%
step 1500, loss 0.04, acc 98.32%
step 1600, loss 0.01, acc 97.49%
step 1700, loss 0.08, acc 98.22%
step 1800, loss 0.11, acc 98.29%
step 1900, loss 0.05, acc 98.35%
step 2000, loss 0.04, acc 98.38%
step 2100, loss 0.06, acc 98.56%
step 2200, loss 0.06, acc 98.30%
step 2300, loss 0.04, acc 98.46%
step 2400, loss 0.06, acc 98.59%
step 2500, loss 0.09, acc 98.44%
step 2600, loss 0.07, acc 98.44%
step 2700, loss 0.06, acc 98.47%
step 2800, loss 0.03, acc 98.50%
step 2900, loss 0.11, acc 98.50%
step 3000, loss 0.03, acc 98.38%
step 3100, loss 0.01, acc 98.64%
step 3200, loss 0.03, acc 98.49%
step 3300, loss 0.03, acc 98.67%
step 3400, loss 0.03, acc 98.63%
step 3500, loss 0.03, acc 98.60%
step 3600, loss 0.04, acc 98.76%
step 3700, loss 0.01, acc 98.66%
step 3800, loss 0.02, acc 98.75%
step 3900, loss 0.01, acc 98.58%
step 4000, loss 0.13, acc 98.64%
step 4100, loss 0.04, acc 98.68%
step 4200, loss 0.02, acc 98.44%
step 4300, loss 0.08, acc 98.76%
step 4400, loss 0.03, acc 98.83%
step 4500, loss 0.01, acc 98.82%
step 4600, loss 0.01, acc 98.80%
step 4700, loss 0.04, acc 98.88%
step 4800, loss 0.06, acc 98.66%
step 4900, loss 0.06, acc 98.83%
step 5000, loss 0.01, acc 98.75%
step 5100, loss 0.03, acc 98.66%
step 5200, loss 0.04, acc 98.80%
step 5300, loss 0.02, acc 98.78%
step 5400, loss 0.03, acc 98.73%
step 5500, loss 0.15, acc 98.92%
step 5600, loss 0.03, acc 98.86%
step 5700, loss 0.03, acc 98.89%
step 5800, loss 0.01, acc 98.91%
step 5900, loss 0.04, acc 98.94%
step 6000, loss 0.00, acc 98.69%
step 6100, loss 0.08, acc 98.77%
step 6200, loss 0.01, acc 98.95%
step 6300, loss 0.05, acc 98.88%
step 6400, loss 0.06, acc 98.85%
step 6500, loss 0.01, acc 98.92%
step 6600, loss 0.01, acc 98.74%
step 6700, loss 0.01, acc 98.84%
step 6800, loss 0.14, acc 98.59%
step 6900, loss 0.04, acc 98.90%
"""
