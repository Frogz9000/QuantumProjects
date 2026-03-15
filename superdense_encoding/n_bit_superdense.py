from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

def get_clean_input():
    raw_input = input("Please enter N bit classical binary to transmit(blank to exit): ")
    if raw_input == "":
        print("Exiting...")
    for i in raw_input:
        if i != "0" and i != "1":
            print("Invalid Input")
            raw_input = input("Please enter N bit classical binary to transmit(blank to exit): ")
    if ( len(raw_input) % 2 != 0):
        raw_input = "0"+raw_input
    return raw_input

classical_bits = get_clean_input()
while(classical_bits != ""):
    classic_len = len(classical_bits)
    print(classical_bits)
    qc = QuantumCircuit(classic_len)
    for i in reversed(range(0,classic_len,2)):
        qc.h(i)
        qc.cx(i,i+1)
        bits_to_encode = f"{classical_bits[i]}{classical_bits[i+1]}"
        if(bits_to_encode == "00"):
            qc.id(i)
        elif(bits_to_encode == "01"):
            qc.x(i)
        elif(bits_to_encode == "10"):
            qc.z(i)
        elif(bits_to_encode == "11"):
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

    classical_bits = get_clean_input()
