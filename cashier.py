import pandas as pd

#Class berikut untuk melakukan CRUD pada sebuah transaksi
class transaction:
    def __init__(self):
        self.list = []

    def add_item(self, name, qty, price):
        #Method berikut untuk melakukan menambahkan item
        #Argument: name: nama barang, qty: jumlah barang, price: harga barang 
        try:
            self.name = name
            self.qty = qty
            self.price = price
            self.list.append([name, qty, price])
            return self.list
        finally:
            pass
        

    def update_item_name(self, name, updateName):   
        #Method berikut untuk melakukan merubah nama item
        #Argument: name: nama barang yang ingin diubah, updateName: Nama Barang yang akan menggantikan nama lama
        i = 0
        while i < len(self.list):
            if self.list[i][0] == name:
                self.list[i][0] = updateName
                break
            elif i == len(self.list)-1 :
                print(f"item {name} is not found")            
            i +=1     
        return self.list
    
    def update_item_qty(self, name, updateQty):
        #Method berikut untuk melakukan merubah qty item
        #Argument: name: qty barang yang ingin diubah, updateQty: Qty yang akan menggantikan qty lama
        i = 0
        while i < len(self.list):
            if self.list[i][0] == name:
                self.list[i][1] = updateQty
                break
            elif i == len(self.list)-1 :
                print(f"item {name} is not found")            
            i +=1     
        return self.list

    def update_item_price(self, name, updatePrice):
        #Method berikut untuk melakukan merubah harga item
        #Argument: name: harga barang yang ingin diubah, updatePrice: harga yang akan menggantikan harga lama
        i = 0
        while i < len(self.list):
            if self.list[i][0] == name:
                self.list[i][2] = updatePrice
                break
            elif i == len(self.list)-1 :
                print(f"item {name} is not found")            
            i +=1     
        return self.list 

    def delete_item(self, name):
        #Method berikut untuk melakukan menghapus sebuah item
        #Argument: name: nama barang yang ingin didelete berikut dengan quantity dan harga pada tabel
        i = 0
        while i < len(self.list):
            if self.list[i][0] == name:
                del self.list[i]
                break
            elif i == len(self.list)-1 :
                print(f"item {name} is not found")            
            i +=1     
        return self.list

    def reset_transaction(self):
        self.list = [] 

    def check_order(self):
        #Method berikut untuk melakukan mengecek apakah data type yang diinput sudah benar
        for x, y, z in self.list:
            if type(x) == str and type(y) == int and type(z) == int:
                print("Pemesanan Sudah Benar")
                
            else:
                print("Terdapat Kesalahan Input")
                break
        
        print(self.list)
    

    
    def total_harga(self):
        column_name = ["Name", "Qty", "Price"]
        df = pd.DataFrame(data=self.list, columns=column_name)
        df["Total Harga"]= df["Qty"]*df["Price"]
        print(df)

        if 200000< df["Total Harga"].sum()<=300_000 :
            total = df["Total Harga"].sum()*0.95
            print(f"Anda mendapatkan diskon 5%. Total Belanja Anda menjadi Rp {total}")
        elif 300000< df["Total Harga"].sum()<=500_000 :
            total = df["Total Harga"].sum()*0.92
            print(f"Anda mendapatkan diskon 8%. Total Belanja Anda menjadi Rp {total}")
        elif df["Total Harga"].sum()>500_000:
            total = df["Total Harga"].sum()*0.90
            print(f"Anda mendapatkan diskon 10%. Total Belanja Anda menjadi Rp {total}")
        else:
            total = df["Total Harga"].sum()
            print(f"Total Belanja Anda adalah Rp {total}")



