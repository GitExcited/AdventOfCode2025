from pathlib import Path
from typing import List
import math

class Box:
    def __init__(self , x_coord, y_coord, z_coord):
        self.x :int = x_coord
        self.y : int = y_coord
        self.z : int =  z_coord
        self.circuit = None

    def add_to_circuit(self, circuit:"Circuit"):
        self.circuit = circuit

    @staticmethod
    def distance(  box1:"Box",  box2: "Box") -> float:
        #Euclidian distance in 3D
        return math.sqrt((box1.x-box2.x)**2 + (box1.y-box2.y)**2 + (box1.z -box2.z)**2)
    def __str__(self):
        return f"Box connected to circuit {self.circuit}, Coord: ({self.x},{self.y},{self.z})"

class Graph:
   def __init__(self):
       self.boxes : List[Box] = []
       self.edges : List[Edge] = []
       self.circuits : List[Circuit] = []
   def sort_edges(self):
       self.edges.sort(key = lambda e : e.distance )

   def connect_boxes(self, pairs : int):
       self.sort_edges()
       for i in range(0,pairs):
           b1= self.edges[i].first_box
           b2 = self.edges[i].second_box
           if b1.circuit is None and b2.circuit is None:
               new_circuit = Circuit()
               new_circuit.add_box(b1)
               new_circuit.add_box(b2)
               b1.circuit = new_circuit
               b2.circuit = new_circuit
               self.circuits.append(new_circuit)
           elif b1.circuit is None:
               b2.circuit.add_box(b1)
               b1.circuit = b2.circuit
           elif b2.circuit is None:
               b1.circuit.add_box(b2)
               b2.circuit = b1.circuit
           elif b1.circuit == b2.circuit:
               pass
           else:
               print(f"We are here because b1 circuit:{b1.circuit} and b2 circuit:{b2.circuit}")

               combined_circuit = Circuit()
               old_circuit_1 = b1.circuit
               old_circuit_2 = b2.circuit
               for el in old_circuit_1.junction_boxes:
                   combined_circuit.add_box(el)
                   el.circuit = combined_circuit
               for el in old_circuit_2.junction_boxes:
                   combined_circuit.add_box(el)
                   el.circuit = combined_circuit
               self.circuits.remove(old_circuit_1)
               self.circuits.remove(old_circuit_2)
               print(f"removed circuit: {old_circuit_1} and {old_circuit_2}")
               self.circuits.append(combined_circuit)

               # print(f" is b1 circuit in circuits? {b1.circuit in self.circuits}")
               # print(f" is b2 circuit in circuits? {b2.circuit in self.circuits}")

               print("We good")


   def sort_circuits(self):
       self.circuits.sort(key=lambda c: c.size, reverse=True)

class Edge:

    def __init__(self, box1: Box, box2: Box):
        self.first_box : Box = box1
        self.second_box : Box = box2
        self.distance : float  = Box.distance(box1,box2)


class Circuit:

    def __init__(self):
        self.junction_boxes: List[Box]= []
        self.size = 0

    def add_box(self, box:Box) -> None:
        self.junction_boxes.append(box)
        self.size += 1

def main():
    INPUT_PATH = Path("../inputs/day_08.txt")
    TEST = Path("../inputs/day_08_example.txt")
    graph = Graph()
    with open(INPUT_PATH) as file:
        for line in file:
            coordinates = line.strip().split(',')
            new_box = Box(x_coord = int(coordinates[0]),
                          y_coord = int(coordinates[1]),
                          z_coord = int(coordinates[2]))
            graph.boxes.append(new_box)
        print(f"i have {len(graph.boxes)}boxes")
        for i in range(0,len(graph.boxes)-1):
            for j in range (i+1, len(graph.boxes)):
                new_edge = Edge(box1 = graph.boxes[i], box2 = graph.boxes[j])
                graph.edges.append(new_edge)

    # i =0
    # for edge in graph.edges:
    #     if i < 100:
    #         print(f" edge: {edge.distance}")
    #         i+=1
    #     if i ==100 :
    #         break
    graph.connect_boxes( pairs = 1000)
    graph.sort_circuits()
    print(f" there are {len(graph.edges)} edges")
    for circuit in graph.circuits:
        print(f"Circuit: {circuit.size}")
    print(f"{graph.circuits[0].size *graph.circuits[1].size* graph.circuits[2].size}")

if __name__ =="__main__":
    main()


