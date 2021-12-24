import random
from net import layer
import numpy as np

class brain:
    layer1=layer()
    layer2=layer()
    layer3=layer()
   
    # default randomized layers
    def default_layer(layern):
        default_weights=np.zeros([4,4])
        bases=np.zeros([4])
        for i in range(4):
            default_weights[i, random.randint(0,3)]=random.randint(1,10)/10
            default_weights[i, random.randint(0,3)]=random.randint(1,10)/10
        return layer.layer(layern, default_weights, bases)  
    
    def default_first_layer(layern):
        default_weights=np.zeros([4,8])
        bases=np.zeros([4])
        for i in range(4):
            default_weights[i, random.randint(0,7)]=random.randint(1,10)/10
            default_weights[i, random.randint(0,7)]=random.randint(1,10)/10
            default_weights[i, random.randint(0,7)]=random.randint(1,10)/10
        return layer.layer(layern, default_weights, bases)

    def default_last_layer(layern):
        default_weights=np.zeros([5,4])
        bases=np.zeros([5])
        for i in range(5):
            default_weights[i, random.randint(0,3)]=random.randint(1,10)/10
            default_weights[i, random.randint(0,3)]=random.randint(1,10)/10
        return layer.layer(layern, default_weights, bases)
        
    # initialize a brain, default values given
    def brain(self, layer1=default_first_layer(layer1), layer2=default_layer(layer2), layer3=default_last_layer(layer3)):
        self.layer1=layer1
        self.layer2=layer2
        self.layer3=layer3

    # make next move
    def fire_all(self, inputs):
        out1=self.layer1.fire_layer(inputs)
        out2=self.layer2.fire_layer(out1)
        return self.layer3.fire_layer(out2)
    
    # combine with average from other brain
    def brain_merge(self, other:brain):
        return brain(self.layer1.layer_sex(other.layer1), self.layer2.layer_sex(other.layer2), self.layer3.layer_sex(other.layer3))
