import numpy as np
from matplotlib import pyplot as plt
import xml.etree.ElementTree as ET
from xml.dom import minidom

Network_Shape = [2,3]
weights = [np.random.randn(i,j) for j,i in zip(Network_Shape[:-1],Network_Shape[1:])]
print(np.shape(weights))


def Save(Weights):
        Network = ET.Element("Neural_Network")
        for x in Weights:
            layer = ET.SubElement(Network,"Layer")
            for y in x:
                Neurone = ET.SubElement(layer,"Neurone")
                for z in y:
                    ET.SubElement(Neurone,"Weight").text = str(z)
        tree = ET.ElementTree(Network)
        tree.write("BEN.xml","UTF-8")

def ReadXML(File_Name):
    count = 0
    Neural_Network = []
    doc = minidom.parse(File_Name)
    Networks = doc.getElementsByTagName("Neural_Network")
    for Network in Networks:
        Layers = Network.getElementsByTagName("Layer")
        Neural_Layer = []
        for Neurones in Layers:
            Neurones = Neurones.getElementsByTagName("Neurone")
            Neural_Neurone = []
            for Weights in Neurones:
                Neural_Weight = []
                Params = Weights.getElementsByTagName("Weight")
                for Weight in Params:
                    The_Data = float (Weight.firstChild.data)
                    Neural_Weight.append(The_Data)
                    print(The_Data)
                    count = count + 1;
                Neural_Neurone.append(np.array(Neural_Weight))
            Neural_Layer.append(Neural_Neurone)
        Neural_Network.append(Neural_Layer)

    print("There are: ",count)
    print(Neural_Network)

Save(weights)
ben = ReadXML("BEN.xml")