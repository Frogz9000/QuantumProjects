from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

classical_4_bit = input("Please enter 4 bit classical binary to transmit: ")
while(classical_4_bit != ""):
    bits = 0b001
    qc = QuantumCircuit(4)
    for (i in bits.bit_length()):
        qc.h(0)
        qc.cx(0,1)
    if(classical_4_bit == "00"):
        qc.id(0)
    elif(classical_4_bit == "01"):
        qc.x(0)
    elif(classical_4_bit == "10"):
        qc.z(0)
    elif(classical_4_bit == "11"):
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
    print(f"Measurement of qubit output: {result[0].data.meas.get_counts()}")

    classical_4_bit = input("Enter Another 2 bit value or nothing to exit: ")
