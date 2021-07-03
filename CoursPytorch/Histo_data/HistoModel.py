def findConv2dOutShape(H_in,W_in,conv,pool=2):
  # get conv arguments
  kernel_size=conv.kernel_size
  stride=conv.stride
  padding=conv.padding
  dilation=conv.dilation

  H_out=np.floor((H_in+2*padding[0]-dilation[0]*(kernel_size[0]-1)-1)/stride[0]+1)
  W_out=np.floor((W_in+2*padding[1]-dilation[1]*(kernel_size[1]-1)-1)/stride[1]+1)
  if pool:
    H_out/=pool
    W_out/=pool
  return int(H_out),int(W_out)


import torch.nn as nn
import torch.nn.functional as F
class model_lit(pl.LightningModule):
    def __init__(self,initial_params,learning_rate=3e-4):
        super(model_lit, self).__init__()
        C_in,H_in,W_in = initial_params['input_shape']
        init_f=initial_params["initial_filters"]
        num_fc1=initial_params["num_fc1"]
        num_classes=initial_params["num_classes"]
        self.dropout_rate=initial_params["dropout_rate"]
        self.conv1 = nn.Conv2d(C_in, init_f, kernel_size=3)
        h,w=findConv2dOutShape(H_in,W_in,self.conv1)
        self.conv2 = nn.Conv2d(init_f, 2*init_f, kernel_size=3)
        h,w=findConv2dOutShape(h,w,self.conv2)
        self.conv3 = nn.Conv2d(2*init_f, 4*init_f, kernel_size=3)
        h,w=findConv2dOutShape(h,w,self.conv3)
        self.conv4 = nn.Conv2d(4*init_f, 8*init_f, kernel_size=3)
        h,w=findConv2dOutShape(h,w,self.conv4)
        # compute the flatten size
        self.num_flatten=h*w*8*init_f
        self.fc1 = nn.Linear(self.num_flatten, num_fc1)
        self.fc2 = nn.Linear(num_fc1, num_classes)
    
        self.learning_rate=learning_rate
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(),lr=self.learning_rate)
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv4(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, self.num_flatten)
        x = F.relu(self.fc1(x))
        x=F.dropout(x, self.dropout_rate)
        x = self.fc2(x)
        loss = F.cross_entropy(x, y)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 2, 2)
        x = F.relu(self.conv4(x))
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, self.num_flatten)
        x = F.relu(self.fc1(x))
        x=F.dropout(x, self.dropout_rate)
        x = self.fc2(x)
        loss = F.cross_entropy(x, y)
        metrics = {'val_loss': loss}
        self.log_dict(metrics)
        return metrics
