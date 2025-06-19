from .huffman_tree import build_tree
from .frequency_analyzer import calculate_frequencies, create_priority_queue

def compress(input_file, output_file):
    # Calculer les frequences
    frequencies = calculate_frequencies(input_file)
    priority_queue = create_priority_queue(frequencies)
    
    # Construire l'arbre et les codes
    root = build_tree(priority_queue)
    codes = generate_codes(root) if root else {}
    
    #Preparer les donnees compressees
    bit_string = ""
    with open(input_file, 'rb') as f:
        while (byte := f.read(1)):
            bit_string += codes[byte[0]]
            
    # Gerer le padding
    padding = 8 - len(bit_string) % 8
    bit_string += '0' * padding
    
    # Convertir en octets
    data_bytes = bytearray()
    for i in range(0, len(bit_string), 8):
        data_bytes.append(int(bit_string[i:i+8], 2))
        
    # Ecrire le fichier compresse
    with open(output_file, 'wb') as f:
        # Ecrire l'en-tete (frequences)
        f.write(byte([len(frequencies)]))
        for byte, freq in frequencies.items():
            f.write(bytes([byte]))
            f.write(freq.to_bytes(8, 'little'))
            
        # Ecrire le padding et les donnees
        f.write(bytes([padding]))
        f.write(data_bytes)