import perceval as pv
from perceval.components import BS, PS
import numpy as np

def addPrep(circuit, prepTheta, prepPhi):

    circuit.add(1, BS.H())
    circuit.add(1, PS(prepTheta/2))
    circuit.add(1, BS.H())
    circuit.add(2, PS(prepPhi))

def deAddPrep(circuit, prepTheta, prepPhi):
    circuit.add(2, PS(-prepPhi))
    circuit.add(1, BS.H())
    circuit.add(1, PS(-prepTheta/2))
    circuit.add(1, BS.H())

def removePrep(circuit, prepTheta, prepPhi):
    circuit.add(0, PS(-prepTheta/2))
    circuit.add(0, BS.H())
    circuit.add(0, PS(-prepPhi))
    circuit.add(0, BS.H())

    circuit.add(2, PS(-prepTheta/2))
    circuit.add(2, BS.H())
    circuit.add(2, PS(-prepPhi))
    circuit.add(2, BS.H())


def addEvolution(circuit, evTheta = None):
    if evTheta is None:
        evTheta = [ pv.P(f'Phi_{i}') for i in range(12) ]

    circuit.add(0, BS.H())
    circuit.add(2, BS.H())
    
    circuit.add(0, PS(evTheta[0]))
    circuit.add(2, PS(evTheta[1]))

    circuit.add(0, BS.H())
    circuit.add(2, BS.H())
    
    circuit.add(1, PS(evTheta[2]))
    circuit.add(3, PS(evTheta[3]))

    circuit.add(1, BS.H())
    circuit.add(1, PS(evTheta[4]))
    circuit.add(1, BS.H())

    circuit.add(0, PS(evTheta[5]))
    circuit.add(2, PS(evTheta[6]))

    circuit.add(0, BS.H())
    circuit.add(2, BS.H())

    circuit.add(0, PS(evTheta[7]))
    circuit.add(2, PS(evTheta[8]))

    circuit.add(0, BS.H())
    circuit.add(2, BS.H())

    circuit.add(1, PS(evTheta[9]))
    circuit.add(3, PS(evTheta[10]))

    circuit.add(1, BS.H())
    circuit.add(1, PS(evTheta[11]))
    circuit.add(1, BS.H())


# def addMeasure(circuit, )

def fullCircuit(evolTheta, prepTheta = 0, prepPhi = np.pi):
    c = pv.Circuit(4)
    
    addPrep(c, prepTheta=prepTheta, prepPhi=prepPhi)
    c.barrier()
    addEvolution(c, evolTheta)
    c.barrier()
    removePrep(c, prepTheta=prepTheta, prepPhi=prepPhi)
    
    return c


def getCircuitTest(prepTheta = 0, prepPhi = np.pi/2):
    c = pv.Circuit(4)
    
    addPrep(c, prepTheta=prepTheta, prepPhi=prepPhi)
    deAddPrep(c, prepTheta=prepTheta, prepPhi=prepPhi)
    
    return c

def getPsi(prepTheta = 0, prepPhi = np.pi):
    c = pv.Circuit(4)
    addPrep(c, prepTheta=prepTheta, prepPhi=prepPhi)
    return c
