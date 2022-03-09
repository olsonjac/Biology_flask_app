from flask import Flask, request, render_template
app = Flask(__name__)
if __name__== '__main__':
  app.run(debug=False, host="0.0.0.0")

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def my_form_post():
    DnaSeq = request.form['DnaSeq']
    DnaSeq = DnaSeq.upper()
    if len(DnaSeq) % 3 != 0:
      error = " invalid input: please enter DNA bases in groups of 3 and make sure you only use the bases (A,T,C,G)"
      return render_template("error.html",
                             error=error)
    if DnaSeq.isdigit():
      error =" no numbers allowed"
      return render_template("error.html",
                             error=error)


   #print("DNA: "+ DnaSeq)
    rna = ""

# Generate the RNA string
    for base in DnaSeq:
    # Replace all occurrences of T with U
      if base == "T":
        rna += "A"
      elif base == "A":
        rna += "U"
      elif base == "C":
        rna += "G"
      elif base == "G":
         rna += "C"

    #makes a list of rna then prints rna and codon list
    rna_seq = [(rna[i:i+3]) for i in range(0,len(rna), 3)]
    #return "RNA Sequence: " + ",".join(rna_seq) 

    # mRNA Codon dictionary that will be used to translate the RNA sequence into the amino acid sequence. 
    rna_codon_dict = {"UUU" : "Phe", "CUU" : "Leu", "AUU" : "Ile", "GUU" : "Val",
           "UUC" : "Phe", "CUC" : "Leu", "AUC" : "Ile", "GUC" : "Val",
           "UUA" : "Leu", "CUA" : "Leu", "AUA" : "Ile", "GUA" : "Val",
           "UUG" : "Leu", "CUG" : "Leu", "AUG" : "Met", "GUG" : "Val",
           "UCU" : "Ser", "CCU" : "Pro", "ACU" : "Thr", "GCU" : "Ala",
           "UCC" : "Ser", "CCC" : "Pro", "ACC" : "Thr", "GCC" : "Ala",
           "UCA" : "Ser", "CCA" : "Pro", "ACA" : "Thr", "GCA" : "Ala",
           "UCG" : "Ser", "CCG" : "Pro", "ACG" : "Thr", "GCG" : "Ala",
           "UAU" : "Tyr", "CAU" : "His", "AAU" : "Asn", "GAU" : "Asp",
           "UAC" : "Tyr", "CAC" : "His", "AAC" : "Asn", "GAC" : "Asp",
           "UAA" : "STOP", "CAA" : "Gln", "AAA" : "Lys", "GAA" : "Glu",
           "UAG" : "STOP", "CAG" : "Gln", "AAG" : "Lys", "GAG" : "Glu",
           "UGU" : "Cys", "CGU" : "Arg", "AGU" : "Ser", "GGU" : "Gly",
           "UGC" : "Cys", "CGC" : "Arg", "AGC" : "Ser", "GGC" : "Gly",
           "UGA" : "STOP", "CGA" : "Arg", "AGA" : "Arg", "GGA" : "Gly",
           "UGG" : "Trp", "CGG" : "Arg", "AGG" : "Arg", "GGG" : "Gly" 
           }
    #this blocks creates an empty amino_acid list
    #it finds the value for each codon in the dictonary and appends it to this list which is then printed
    rna_seq = list(rna_seq)
    amino_acid=[]
    for x in range(len(rna_seq)):
      amino_acid.append(rna_codon_dict[rna_seq[x]])
    #amino_acid = ",".join(amino_acid)
    return render_template("results.html",
                           amino_acid=amino_acid,
                           rna_seq=rna_seq,
                           Dna_Seq=DnaSeq)
