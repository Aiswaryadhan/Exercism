def to_rna(dna_strand):
    relations = {"G": "C", "C": "G", "A": "U", "T":"A"}
    transcription = ""
    for char in dna_strand:
        transcription += relations[char]
    return transcription
