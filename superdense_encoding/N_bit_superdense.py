from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

classical_bits = input("Please enter N bit classical binary to transmit: ")
while(classical_bits != ""):
    data = classical_bits
    data_len = len(data)
    if (data_len % 2 != 0):
        "0".join(data)
        data_len+=1
    qc = QuantumCircuit(data_len)
    for i in range(data_len/2):
        qc.h(i)
        qc.cx(i,i+1)
        bits_to_encode = f"{classical_bits[i+1]}{classical_bits[i]}"
        if(classical_bits == "00"):
            qc.id(i)
        elif(classical_bits == "01"):
            qc.x(i)
        elif(classical_bits == "10"):
            qc.z(i)
        elif(classical_bits == "11"):
            qc.z(i)
            qc.x(i)
    qc.cx(i,i+1)
    qc.h(i)
    
    print("Full Circuit:")
    print(qc.draw("text"))

    qc.measure_all()
    #simulate the circuit 
    sampler = StatevectorSampler()
    result = sampler.run([qc], shots=1024).result()
    print(f"Measurement of qubit output: {result[0].data.meas.get_counts()}")

    classical_bits = input("Enter Another 2 bit value or nothing to exit: ")
