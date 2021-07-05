from argparse import ArgumentParser
import HistoDataModule
import HistoModel
initial_parameters={'input_shape':(3,96,96),"initial_filters":8,"num_fc1":100,"num_classes":2,"dropout_rate":0.25}initial_parameters={'input_shape':(3,96,96),"initial_filters":8,"num_fc1":100,"num_classes":2,"dropout_rate":0.25}
histo_data = HistoDataModule.HistoDataModule(path_data, transform, batch_size=64)
histo_data.setup()
def main(hparams):
    model = HistoModel.model_lit(initial_parameters)
    trainer = Trainer(gpus=hparams.gpus,max_epochs=hparams.max_epochs,num_workers=hparams.num_workers)
    trainer.fit(model,histo_data)
    if __name__ == '__main__':
        parser = ArgumentParser()
        parser.add_argument('--gpus', default=None,required = True)
        parser.add_argument('--max_epochs', default=4,required = True)
        parser.add_argument('--num_workers', default=20,required = True)
        args = parser.parse_args() 
