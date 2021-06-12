import torch.cuda


def gpuAvailable():
    if torch.cuda.is_available():
        print("GPU available")
    else:
        print("GPU unavailable")

gpuAvailable()
