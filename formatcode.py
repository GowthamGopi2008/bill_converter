import pandas as pd
import clipboard

class BillFormatter():
    def __init__(self):
        pass
    
    supplier = ["PASH","PADT"]

    def Invalid(self):
        print("Invalid Invoice Number")

    def FindSupplier(self, text):
        if text[:2] == "IR":
            return "PADT"
        elif text[:2] == "HR":
            return "PASH"
        else:
            self.Invalid()


    def Format(self, invoice):
        df = pd.read_excel("C:/Users/Gowtham Gopi/Downloads/"+invoice+".xls")

        sup = self.FindSupplier(invoice)
        
        # Format Method for Popular Auto Spares and Popular Auto Distributors
        if sup == self.supplier[0] or sup == self.supplier[1]:
            df = df.drop([0,1])

        path = "C:/X/Bills/"+invoice+".csv"
        clipboard.copy(invoice)
        df.to_csv(path,index=False,sep="\t",header=False)
            





