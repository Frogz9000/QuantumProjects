from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
classical_2_bit = input("Please enter 2 bit classical binary to transmit: ")


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
if(classical_2_bit == "00"):
    qc.id(0)
elif(classical_2_bit == "01"):
    qc.x(0)
elif(classical_2_bit == "10"):
    qc.z(0)
elif(classical_2_bit == "11"):
    qc.z(0)
    qc.x(0)
print("Transmission Circuit:")
print(qc.draw("text"))


print("Full Circuit:")
qc.cx(0,1)
qc.h(0)
print(qc.draw("text"))

qc.measure_all()
#simulate the circuit 
sampler = StatevectorSampler()
result = sampler.run([qc], shots=1024).result()
print(result[0].data.meas.get_counts())