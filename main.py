import time
from tkinter import *
import networkx as nx
import tkinter as tk
import random
import matplotlib.pyplot as plt
root = Tk()
root.geometry("500x700")
root.configure(bg = 'powderblue')
root.title(" BigBossCoding ")
minColor = 0
G = nx.Graph()
NodeList = []
listEdges=[]
iterate = 0
selectedColour = 0
color_Selection = []
def printcolour1():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("lightcoral")
def printcolour2():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("blue")
def printcolour3():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("firebrick")
def printcolour4():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("chocolate")
def printcolour5():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("darkolivegreen")
def printcolour6():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("blueviolet")
def printcolour7():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("magenta")
def printcolour8():
    global selectedColour
    selectedColour= selectedColour + 1
    color_Selection.append("teal")

def iteratenumber():
    global iterate
    xa = int(inputtxt.get("1.0", "end-1c"))
    iterate = xa
    inputtxt.delete("1.0", "end-1c")
    Displayuc.destroy()
    Display.pack()
    Display.place(relx=0.5, y=250, anchor=CENTER)

def NodeAddFunc(node):
    if G.has_node(node) == False:
        G.add_node(node)
        NodeList.append(node)
        return NodeList
def NodeEdge():
    global i
    i = 0
    x = inputtxt.get("1.0", "end-1c")
    nodeconnections = x.splitlines()
    print(nodeconnections)
    for i in range(len(nodeconnections)):
        listEdges.append(nodeconnections[i])
        s = listEdges[i].split()
        NodeAddFunc(s[0])
        NodeAddFunc(s[len(s) - 1])
        G.add_edge(s[0], s[len(s) - 1])
        i = i + 1
    inputtxt.delete("1.0", "end-1c")
    Display.destroy()
    minColorFinder()
    textcolourselect= Label(root, text="Select at least " + str(minColor + 1) +" colours:")
    textcolourselect.configure(font = ("Times New Roman", 20), bg = 'powderblue')
    textcolourselect.place(relx=0.5,y=50, anchor=CENTER)
    Displayiki.pack()
    inputtxt.destroy()
    Displayrenk1.pack()
    Displayrenk2.pack()
    Displayrenk3.pack()
    Displayrenk4.pack()
    Displayrenk5.pack()
    Displayrenk6.pack()
    Displayrenk7.pack()
    Displayrenk8.pack()
    Displayiki.place(relx=0.5,y=100, anchor=CENTER)
    Displayrenk1.place(relx=0.5, y=150, anchor=CENTER)
    Displayrenk2.place(relx=0.5, y=200, anchor=CENTER)
    Displayrenk3.place(relx=0.5, y=250, anchor=CENTER)
    Displayrenk4.place(relx=0.5, y=300, anchor=CENTER)
    Displayrenk5.place(relx=0.5, y=350, anchor=CENTER)
    Displayrenk6.place(relx=0.5, y=400, anchor=CENTER)
    Displayrenk7.place(relx=0.5, y=450, anchor=CENTER)
    Displayrenk8.place(relx=0.5, y=500, anchor=CENTER)



def minColorFinder():
    global minColor

    ColoredNodes = {}
    node_color = []
    color_map = ["lightcoral", "gray", "lightgray", "firebrick", "red", "chocolate", "darkorange", "moccasin", "gold",
                 "yellow", "darkolivegreen", "chartreuse", "forestgreen", "lime", "mediumaquamarine", "turquoise",
                 "teal", "cadetblue", "dogerblue", "blue", "slateblue", "blueviolet", "magenta", "lightsteelblue"]
    for node in G:
        x = 0
        if len(ColoredNodes) == 0:
            node_color.append(color_map[x])
            ColoredNodes[node] = color_map[x]
        elif len(ColoredNodes) > 0:
            for node2 in ColoredNodes:
                if G.has_edge(node, node2) and color_map[x] == ColoredNodes.get(node2):
                    x = x + 1
                    if (x > minColor):
                        minColor = x

            node_color.append(color_map[x])
            ColoredNodes[node] = color_map[x]



def colorFunc():
    global iterate
    ColoredNodes = {}
    node_color = []

    nx.draw(G, node_size=1000, node_color = "gray", with_labels=True)
    plt.show(block=False)
    plt.pause(2)
    plt.close()

    time.sleep(2)
    plt.close()
    Displayiki.destroy()
    x = 0

    Displayrenk1.destroy()
    Displayrenk2.destroy()
    Displayrenk3.destroy()
    Displayrenk4.destroy()
    Displayrenk5.destroy()
    Displayrenk6.destroy()
    Displayrenk7.destroy()
    Displayrenk8.destroy()
    textcolourselect = Label(root, text="These are the following graphs:")
    textcolourselect.configure(font=("Times New Roman", 20), bg='powderblue')
    textcolourselect.place(relx=0.5, y=50, anchor=CENTER)


    if(iterate> len(NodeList)):
        iterate= len(NodeList)
    for i in range(iterate):
        if len(ColoredNodes) == 0:
            node_color.append(color_Selection[x])
            ColoredNodes[NodeList[i]] = color_Selection[x]
            for y in range(len(NodeList)-(i+1)):
                node_color.append("gray")
            nx.draw(G, node_size=1000, node_color=node_color, with_labels=True)

            plt.show(block=False)
            plt.pause(2)
            plt.close()
            for y in range(len(NodeList) - (i + 1)):
                node_color.remove("gray")

        elif len(ColoredNodes) > 0:
            for neighbours in G.neighbors(NodeList[i]):
                for node2 in ColoredNodes:
                    while G.has_edge(NodeList[i], node2) and color_Selection[x] == ColoredNodes.get(node2):
                        x = x + 1
                        if (x >= len(color_Selection)):
                            x = 0

            node_color.append(color_Selection[x])
            ColoredNodes[NodeList[i]] = color_Selection[x]

            for y in range(len(NodeList) - (i + 1)):
                node_color.append("gray")

            nx.draw(G, node_size=1000, node_color=node_color, with_labels=True)
            plt.show(block=False) #ben burda kapatıyom
            plt.pause(2)
            plt.close()
            for y in range(len(NodeList) - (i + 1)):
                node_color.remove("gray")
            print(node_color)
    for i in range(len(NodeList)-iterate):
        node_color.append("gray")
    nx.draw(G,node_size=1000,node_color=node_color, with_labels=True)

    plt.show(block=False)



inputtxt = Text(root, height = 13,
                width = 20,
                bg = "beige")
Display = Button(root, height = 2,
                 width = 30,
                 text ="Connect nodes",
                 command = lambda:NodeEdge())
Displayiki = Button(root, height = 2,
                 width = 30,
                 text ="SHOW GRAPH",
                 command = lambda:colorFunc())
Displayuc = Button(root, height = 2,
                 width = 30,
                 text ="Enter iteration number",
                 command = lambda:iteratenumber())

Displayrenk1 = Button(root, height = 2,
                 width = 30,
                 text ="lightcoral",
                 bg = "lightcoral",
                 command = lambda:printcolour1())
Displayrenk2 = Button(root, height = 2,
                 width = 30,
                 text ="blue",
                 bg = "blue",
                 command = lambda:printcolour2())
Displayrenk3 = Button(root, height = 2,
                 width = 30,
                 text ="firebrick",
                 bg = "firebrick",
                 command = lambda:printcolour3())
Displayrenk4 = Button(root, height = 2,
                 width = 30,
                 text ="chocolate",
                 bg = "chocolate",
                 command = lambda:printcolour4())
Displayrenk5 = Button(root, height = 2,
                 width = 30,
                 text ="Dark olivegreen",
                 bg = "darkolivegreen",
                 command = lambda:printcolour5())
Displayrenk6 = Button(root, height = 2,
                 width = 30,
                 text ="Blue Violet",
                 bg = "blueviolet",
                 command = lambda:printcolour6())
Displayrenk7 = Button(root, height = 2,
                 width = 30,
                 text ="Magenta",
                 bg = "magenta",
                 command = lambda:printcolour7())
Displayrenk8 = Button(root, height = 2,
                 width = 30,
                 text ="Teal",
                 bg = "teal",
                 command = lambda:printcolour8())


inputtxt.pack()
Displayuc.pack()
Displayuc.place(relx=0.5,y=250, anchor=CENTER)


mainloop()
#babalarCoding2022
#BigBossCoding2022