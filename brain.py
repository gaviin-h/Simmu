import random
from net import layer
import numpy as np

class brain:
    layer1=layer()
    layer2=layer()
    layer3=layer()
   
    def default_layer(layern):
        default_weights=np.zeros([4,4])
        bases=np.zeros([4,1])
        for i in range(4):
            default_weights[i, random.randint(0,3)]=random.randint(-10,10)/10
        return layer.layer(layern, 4, default_weights, bases)  

    def brain(self, layer1=default_layer(layer1), layer2=default_layer(layer2), layer3=default_layer(layer3)):
        self.layer1=layer1
        self.layer2=layer2
        self.layer3=layer3

    def fire_all(self, inputs):
        out1=self.layer1.fire_layer(inputs)
        out2=self.layer2.fire_layer(out1)
        return self.layer3.fire_layer(out2)
    
    def brain_merge(self, other:brain):
        return brain(self.layer1.layer_sex(other.layer1), self.layer2.layer_sex(other.layer2), self.layer3.layer_sex(other.layer3))

#########################
#   inputs: np.array
#       getpos[0]
#       getpos[1]
#       nearby minis
#       nearby food
#       color of nearby minis
#       