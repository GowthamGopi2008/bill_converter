import pandas as pd
import clipboard

class BillFormatter():
    def __init__(self):
        pass
    
    supplier = ["PASH","PADT", "UTA"]

    def Invalid(self):
        print("Invalid Invoice Number")

    def FindSupplier(self, text):
        if text[:2] == "IR":
            print("PADT")
            return "PADT"
        elif text[:2] == "HR":
            print("PASH")
            return "PASH"
        elif text[:4] == "5005":
            print("UTA")
            return "UTA"
        else:
            self.Invalid()


    def Format(self, invoice):
        print(invoice)
        pre_path = "C:/Users/Gowtham Gopi/Downloads/"

        sup = self.FindSupplier(invoice)

        # Format Method for Popular Auto Spares and Popular Auto Distributors
        if sup == self.supplier[0] or sup == self.supplier[1]:
            df = pd.read_excel(pre_path+invoice+".xls")
            df = df.drop([0,1])
        elif sup == self.supplier[2]:
            f_name = "VISHNU "+invoice
            df = pd.read_excel(pre_path+f_name+".xlsx")
            # df = df.drop(0)
            df = df.sort_values(by=df.columns[1])
            invoice = invoice[6:]

        path = "C:/X/Bills/"+invoice+".csv"
        clipboard.copy(path)
        df.to_csv(path,index=False,sep="\t",header=False)
            





