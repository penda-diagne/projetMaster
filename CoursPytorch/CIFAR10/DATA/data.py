from torchvision import datasets

data_transform = transforms.Compose([transforms.RandomHorizontalFlip(p=1),
                                     transforms.RandomVerticalFlip(p=1),
                                     transforms.ToTensor(),])
path2data = "./data"
train_data = datasets.CIFAR10(path2data,train = True,download = True)
x_train = train_data.data
y_train = train_data.targets
x_test = test_data.data
y_test = test_data.targets
