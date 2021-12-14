from net import layer

class brain:
    layer1=layer()
    layer2=layer()
    layer3=layer()
    def brain(self, layer1, layer2, layer3):
        self.layer1=layer1
        self.layer2=layer2
        self.layer3=layer3

    def fire_all(self, inputs):
        out1=self.layer1.fire_layer(inputs)
        out2=self.layer2.fire_layer(out1)
        return self.layer3.fire_layer(out2)
    
    def brain_merge(self, other:brain):
        return brain(self.layer1.layer_sex(other.layer1), self.layer2.layer_sex(other.layer2), self.layer3.layer_sex(other.layer3))