import os
import torch
import data_setup, engine, model_builder, utils

from torchvision import transforms

# setup hyperparameters
NUM_EPOCHS = 5
BATCH_SIZE = 32
LEARNING_RATE = 0.001
HIDDEN_UNITS = 10

# setup directories
train_dir = "data/pizza_steak_sushi/train"
test_dir = "data/pizza_steak_sushi/test"

# Setup target device
device = "cuda" if torch.cuda.is_available() else "cpu"

# create transforms
data_transforms = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor()
])

# create Dataloader
train_dataloader, test_dataloader = data_setup.create_dataloaders(
    train_dir=train_dir,
    test_dir=test_dir,
    transform=data_transforms,
    batch_size=BATCH_SIZE
)

# create model
model = model_builder.TinyVGG(
    input_shape=3,
    hidden_units=HIDDEN_UNITS,
    output_shape=len(class_names)
)