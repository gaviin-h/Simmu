import numpy as np
import random

class layer:
    weights: np.array
    bases: np.array
    def layer(self, weights: np.array, bases: np.array):
        self.weights=weights
        self.bases=bases
        return self

    def fire_layer(self, inputs):
        return np.dot(inputs, self.weights) + self.bases
    ## doesnt work with numpy arrays FIX    
    def combine(self, other: layer):
        resultant_weights=np.array ## 
        resultant_bases=[] # 
        for i in range(len(self.nodes)):
            resultant_bases.append(((self.nodes[i].base + other.nodes[i].base) / 2 ) * random.randrange(-0.2, -0.2, 0.02))
            resultant_weights.append(weight_sex(self.nodes[i].weights, other.nodes[i].weights))
        return layer(len(self.nodes), resultant_weights, resultant_bases)

def weight_sex(weights1, weights2):
    new_weights=[]
    for i in range(len(weights1)):
        new_weights.append(((weights1[i] + weights2[i])/ 2 ) + random.randrange(-0.1, 0.1, 0.2))
    return new_weights