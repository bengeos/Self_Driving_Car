import numpy as np
import xml.etree.ElementTree as ET
Network_Shape = [3,5,4,3]
weights = [np.random.randn(i,j) for j,i in zip(Network_Shape[:-1],Network_Shape[1:])]
#print(weights)

# Network = ET.Element("NeuralNetwork")
# for x in weights:
#     layer = ET.SubElement(Network,"Layer")
#     for y in x:
#         Neuron = ET.SubElement(layer,"Neurone")
#         for z in y:
#             ET.SubElement(Neuron,"Weight").text = str(z)
#
# tree = ET.ElementTree(Network)
# tree.write("BEN.xml","UTF-8")
#
# new_weight = []
# bb = ET.parse('BEN.xml')
# for lay in bb.findall('Layer'):
#     lyr = []
#     print('---------------------------------')
#     for neurone in lay.findall("Neurone"):
#         neurn = []
#         for ww in neurone.findall("Weight"):
#             neurn.append(float(ww.text))
#             print(ww.text)
#         lyr.append(neurn)
#     new_weight.append(np.array(lyr))
# print('***************New Weight*************************')
# print(new_weight)
# print('***************Old Weight*************************')
# print(weights)
def Save(Weights):
        Network = ET.Element("Neural_Network")
        for x in Weights:
            layer = ET.SubElement(Network,"Layer")
            for y in x:
                Neurone = ET.SubElement(layer,"Neurone")
                for z in y:
                    ET.SubElement(Neurone,"Weight").text = str(z)
        tree = ET.ElementTree(Network)
        tree.write("MLP_WEIGHT.xml","UTF-8")

def ReadXML(File_Name):
    doc = ET.parse(File_Name)
    Nets = []
    for Layers in doc.findall('Layer'):
        Neur = []
        for Neurones in Layers.findall('Neurone'):
            Param = []
            for Weights in Neurones.findall('Weight'):
                Param.append(float(Weights.text))
            Neur.append(Param)
        Nets.append(np.array(Neur))
    return Nets
Save(weights);
new_weight = ReadXML('MLP_WEIGHT.xml')
print('***************New Weight*************************')
print(new_weight)
print('***************Old Weight*************************')
print(weights)