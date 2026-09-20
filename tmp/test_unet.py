import torch, torch.nn as nn
x = torch.randn(1, 3, 256, 256)
conv = nn.Conv2d(3, 64, 3, padding=1)
y = conv(x)
print(f"input: {x.shape} -> output: {y.shape}")   # 应为 [1,64,256,256]
print("PyTorch OK")
