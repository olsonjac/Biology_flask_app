from flask import Flask, request, render_template
app = Flask(__name__)

if __name__== '__main__':
  app.run(debug=False, host="0.0.0.0")

#This sends the user to the main index.html, "home page". 
@app.route('/')
def my_form():
    return render_template('index.html')

#This routes the user input from the index.html page into the DnaSeq variable.
@app.route('/', methods=['POST','GET'])
def my_form_post():
    DnaSeq = request.form['DnaSeq']
    DnaSeq = DnaSeq.upper()
    
    #Checks user input to see if multiples of 3 DNA bases were added(its required to be in groups of 3)
    if len(DnaSeq) % 3 != 0:
      error = " invalid input: please enter DNA bases in groups of 3 and make sure you only use the bases (A,T,C,G)"
      return render_template("error.html",
                             error=error)
    #checks for numerical data in the submission and redirects to the error page if found
    if DnaSeq.isdigit():
      error =" no numbers allowed"
      return render_template("error.html",
                             error=error)


   #initializes the empty string for the rna sequence.
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
    
    #this routes all the variables gathered from the script into the results.html page so that they can be displayed
    return render_template("results.html",
                           amino_acid=amino_acid,
                           rna_seq=rna_seq,
                           Dna_Seq=DnaSeq)
