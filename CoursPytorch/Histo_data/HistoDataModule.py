class HistoDataModule(pl.LightningDataModule):
    """ Cassava DataModule for Lightning """
    def __init__(self, root_dir, transform=None, batch_size=32):
        super().__init__()
        self.batch_size = batch_size
        self.root_dir = root_dir
        self.transform = transform
        
    def setup(self, path=None):
        histo_full = HistoDataset(self.root_dir, self.transform)
        len_data=len(thedata)
        len_train=int(0.8*len_data)
        len_val=len_data-len_train

        # Create train and validation datasets
        self.histo_train, self.histo_val = random_split(histo_full, [len_train, len_val])
        train_transformer = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomVerticalFlip(p=0.5),
        transforms.RandomRotation(45),
        transforms.RandomResizedCrop(96,scale=(0.8,1.0),ratio=(1.0,1.0)),
        transforms.ToTensor()])
        val_transformer = transforms.Compose([transforms.ToTensor()])
        self.histo_train.transform=train_transformer
        self.histo_val.transform=val_transformer
        
    def train_dataloader(self):
        return DataLoader(self.histo_train, batch_size=self.batch_size)
    
    def val_dataloader(self):
        return DataLoader(self.histo_val, batch_size=self.batch_size)
