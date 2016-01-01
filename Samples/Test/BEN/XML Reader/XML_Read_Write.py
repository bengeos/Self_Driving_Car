import numpy as np
import xml.etree.ElementTree as ET
Network_Shape = [2,3]
weights = [np.random.randn(i,j) for j,i in zip(Network_Shape[:-1],Network_Shape[1:])]
print(weights)

Network = ET.Element("NeuralNetwork")
for x in weights:
    layer = ET.SubElement(Network,"Layer")
    for y in x:
        Neuron = ET.SubElement(layer,"Neurone")
        for z in y:
            ET.SubElement(Neuron,"Weight").text = str(z)

tree = ET.ElementTree(Network)
tree.write("BEN.xml","UTF-8")

new_weight = np.array([])
bb = ET.parse('BEN.xml')
for lay in bb.findall('Layer'):
    lyr = np.array([])
    print('---------------------------------')
    for neurone in lay.findall("Neurone"):
        neurn = np.array([])
        for ww in neurone.findall("Weight"):
            neurn.append(ww.text)
            print(ww.text)
        lyr.append(neurn)
    new_weight.append(lyr)

print(new_weight)
