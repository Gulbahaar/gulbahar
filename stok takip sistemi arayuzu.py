import dbm
from json import loads
import pickle
import tkinter as tk
from tkinter import messagebox
class Product():
    def __init__( self, kategori, isim, marka, tanim, stok, fiyat, link ):
        self.kategori = kategori
        self.isim = isim
        self.marka = marka
        self.tanim = tanim
        self.stok = stok
        self.fiyat = fiyat
        self.link = link
        if type(self.fiyat)==str or type(self.stok)==str:
            try:
                self.fiyat = float(fiyat)
                self.stok = int(stok)
            except:
                raise Exception("Fiyat veya stok degiskenleri float/int yapisinda veya numerik string yapisinda olmalidir")
    
    def fiyat_arttir(self, artis_miktari):
        self.fiyat += artis_miktari
    def kampanya(self, yuzde):
        self.fiyat *= (1-yuzde) 
    def bir_adet_sat(self, bir):
        self.stok -= bir
        return "Kategori: {} | {} - {}, {}TL, stok: {}".format(self.kategori, self.isim, self.marka, self.fiyat, self.stok)#{} : self.model_id, 
    def __str__(self):
        return "Kategori: {} | {} - {}, {}TL, stok: {}".format(self.kategori, self.isim, self.marka, self.fiyat, self.stok)#{} : self.model_id, 
class App():
    def __init__(self, parent):
        self.parent = parent
        self.program()
    def program(self):
        frame_1 = tk.Frame(self.parent,highlightthickness=5)
        frame_1.pack(anchor=tk.CENTER, padx=0, pady=0)
        self.lb_1 = tk.Listbox(frame_1, exportselection=0,highlightbackground="Black",highlightthickness=4)
        kategori_list = ["Yiyecek", "İcecek", "Giyim", "Elektronik", "Ev"]
        [self.lb_1.insert(index, aktor) for index, aktor in enumerate(kategori_list)]
        self.lb_1.grid(rowspan=3, column=0)
        list_1 = ["İsim", "Marka", "Tanim","Stok", "Fiyat", "Link"]
        for index, eleman in enumerate(list_1):
            tk.Label(frame_1, text=eleman).grid(row=0, column=index+1)
            if eleman == "İsim":
                self.isim_var = tk.StringVar()
                self.isim = tk.Entry(frame_1, textvariable= self.isim_var)
                self.isim.grid(row=2, column=index+1, padx=10)
            elif eleman == "Marka":
                self.marka_var = tk.StringVar()
                self.marka = tk.Entry(frame_1, textvariable= self.marka_var)
                self.marka.grid(row=2, column=index+1, padx=10)
            elif eleman == "Tanim":
                self.tanim_var = tk.StringVar()
                self.tanim = tk.Entry(frame_1, textvariable= self.tanim_var)
                self.tanim.grid(row=2, column=index+1, padx=10)
            elif eleman == "Stok":
                self.stok_var = tk.IntVar()
                self.stok = tk.Entry(frame_1, textvariable= self.stok_var)
                self.stok.grid(row=2, column=index+1, padx=10)
            elif eleman == "Fiyat":
                self.fiyat_var = tk.IntVar()
                self.fiyat_var.set(float())
                self.fiyat = tk.Entry(frame_1, textvariable= self.fiyat_var)
                self.fiyat.grid(row=2, column=index+1, padx=10)
            elif eleman == "Link":
                self.link_var = tk.StringVar()
                self.link = tk.Entry(frame_1, textvariable= self.link_var)
                self.link.grid(row=2, column=index+1, padx=10)
                ekle_click = tk.Button(frame_1, text="Ekle", command=self.ekle_click)
                ekle_click.grid(row=1, column=7, padx=20)
                frame_2 = tk.Frame(self.parent, highlightbackground="Black", highlightthickness=4)
                frame_2.pack(anchor=tk.CENTER, padx=0, pady=10)
                self.lb_2 = tk.Listbox(frame_2, width=150, exportselection=0)
                self.lb_2.grid(rowspan=3, column=0)
                sat_click = tk.Button(frame_2, text="1 Adet Sat", command=self.sat_click)
                sat_click.grid(row=1, column=1, padx=20)
 
    def ekle_click(self):
        self.kategori = self.lb_1.get(tk.ANCHOR)
        try:
            self.stok_var.get()
        except tk.tkinter.TclError:
            tk.messagebox.showerror("Error", "Stok degeri sadece rakamlardan olusabilir.")
            return
        try:
            self.fiyat_var.get()
        except tk.tkinter.TclError:
            tk.messagebox.showerror("Error", "Fiyat degeri sadece rakamlardan olusabilir.")
            return
        if self.kategori == "":
            tk.messagebox.showerror("Error", "Kategori secmediniz.")
        elif self.isim_var.get() == "":
            tk.messagebox.showerror("Error", "Urun İsim'i boş birakilmaz." )
        elif self.marka_var.get() == "":
            tk.messagebox.showerror("Error", "Urun Marka'si boş birakilmaz.")
        elif self.tanim_var.get() == "":
            tk.messagebox.showerror("Error", "Urun Tanim'i boş birakilmaz." )
        elif self.stok_var.get() == "":
            tk.messagebox.showerror("Error", "Urun Stok'u boş birakilmaz." )
        elif self.fiyat_var.get() == "":
            tk.messagebox.showerror("Error", "Urun Fiyat'i boş birakilmaz." )
        elif self.link_var.get() == "":
            tk.messagebox.showerror("Error", "Urun Link'i boş birakilmaz." )
        else:
            sayac = 0
            while sayac <= 10:
                list_1 = list()
                product_i = "product_{}".format(sayac)
                list_1.append(product_i)
                for self.im in list_1:
                    print(self.im)
                    self.im = Product(self.kategori,self.isim_var.get() , self.marka_var.get(),self.tanim_var.get(), self.stok_var.get() ,self.fiyat_var.get(), self.link_var.get())
                with dbm.open("veri_tabani.db", "c") as file:
                    file [str(sayac)] = pickle.dumps(self.im)
                    for ke in file.keys():
                        self.lb_2.insert(tk.END, pickle.loads(file [ke]).__str__())
                sayac += 1
                break
 
#print(list_1)
#with dbm.open("veri_tabani.db", "c") as file:
# file ["0"] = pickle.dumps(self.product_1)
# for ke in file.keys():
# self.lb_2.insert(tk.END, pickle.loads(file [ke]).__str__())
            print(" Kategori : ", self.kategori , "\n","İsim : " , self.isim_var.get() , "\n","Marka : " , self.marka_var.get(), "\n","Tanim : " , self.tanim_var.get(), "\n","Stok : " , self.stok_var.get() , "\n","Fiyat : " , self.fiyat_var.get(), "\n","Link : " , self.link_var.get())
    def sat_click(self):
        self.lb_2.delete(tk.END)
        with dbm.open("veri_tabani.db", "c") as file:
            for ke in file.keys():
                sd = pickle.loads(file [ke]).bir_adet_sat(1)
                file [ke] = pickle.dumps(pickle.loads(file [ke]).stok - 1)
                print(pickle.loads(file [ke]))
                print(type(file [ke]))
                #print(pickle.loads(file [ke]))
                self.lb_2.insert(tk.END, sd )
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
main()