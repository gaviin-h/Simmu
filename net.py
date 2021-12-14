import numpy as np
import random
class node: 
    weights=[]   
    base=0 
    def node(self, weights, base):
        self.weights=weights
        self.base=base
        return self

    def fire(self, inputs):
        return np.dot(inputs, self.weights)+self.base

class layer:
    nodes=[]
    outputs=[]
    def layer(self, nodes, weights, bases):
        for i in range(nodes):
            nodes.append(node(weights[i], bases[i]))
        return self

    def fire_layer(self, inputs):
        for node in self.nodes:
            self.outputs.append(node.fire(inputs))
        return self.outputs
        
    def combine(self, other: layer):
        resultant_weights=[]
        resultant_bases=[]
        for i in range(len(self.nodes)):
            resultant_bases.append(((self.nodes[i].base + other.nodes[i].base) / 2 ) * random.randrange(-0.2, -0.2, 0.02))
            resultant_weights.append(weight_sex(self.nodes[i].weights, other.nodes[i].weights))
        return layer(len(self.nodes), resultant_weights, resultant_bases)

def weight_sex(weights1, weights2):
    new_weights=[]
    for i in range(len(weights1)):
        new_weights.append(((weights1[i] + weights2[i])/ 2 ) + random.randrange(-0.1, 0.1, 0.2))
    return new_weights