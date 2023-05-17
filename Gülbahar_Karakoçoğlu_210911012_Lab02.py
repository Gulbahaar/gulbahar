class Product(object):
    """Represents product in defination
    attributes:
    product name
    product brand
    category list
    product cost
    ethernet link
    stock quantity
    product defination
    """
    def __init__(self,product_name = "",product_brand = "",category_list = [],product_cost = 0,ethernet_link ="",stock_quantity = 0,product_defination = ""):
        self.product_name = product_name
        self.product_brand = product_brand
        self.category_list = category_list
        self.product_cost = float(product_cost)
        self.ethernet_link = ethernet_link
        self.stock_quantity = stock_quantity
        self.product_defination = product_defination
    def zam(self,zam_miktari):
        cst = (self.product_cost * zam_miktari) / 100
        self.product_cost += cst
        return self.product_cost
    def iskonto(self,iskonto_miktari):
        cst = (self.product_cost * iskonto_miktari) / 100
        self.product_cost -= cst
        return self.product_cost
class Wallet(object):
    """Represents wallet in money
    attributes:
    wallet name
    wallet limit
    spending
    Percent
    """
    def __init__(self,wallet_name = "",wallet_limit = 0,spending_money = 0,Percent = 0):
        self.wallet_name = wallet_name
        self.wallet_limit = float(wallet_limit)
        self.spending_money = spending_money
        self.Percent = float(Percent)
    def spending(self,product,num):
        cst = product.product_cost
        self.spending_money += cst*num
    def percent(self):
        self.Percent = (100*self.spending_money)/self.wallet_limit
    def remain(self):
        self.wallet_limit -= self.spending_money

    def print_info(self):
        self.percent()
        self.remain()
        print("Wallet name:{},sum of spending:{},remaining money:{},spending percent:{}".format(self.wallet_name,self.spending_money,self.
wallet_limit,self.Percent))
k_1 = Product("Duracell ince","Duracell",["Ev Yasam","pil"],"39.90","https://cdn.getir.com/product/57ab080887014a03008aaebd_tr_1597245028415.jpeg","10","4lu")
k_2 = Product("semsiye","yagmurkovan",["Ev Yasam","semsiye"],"94.90","https://cdn.getir.com/product/5d974be3bcb5847fb4d7ba65_tr_1570201391034.jpeg","10","siyah")
k_3 = Product("Play-Doh Mini Oyun Seti","Play-Doh",["Ev Yasam","OyunOyuncak"],"69.90","https://cdn.getir.com/product/603fb869648eaa0535fc6088_tr_1614853862147.jpeg","10","1")
k_4 = Product("cat food","purina",["pet"],"73.90","https://cdn.getir.com/product/5ab4b21481179a000461d17c_tr_1601931749594.jpeg","10","800gr")
k_5 = Product("tooth paste","colgate",["home and life","personel care"],"64.90","https://cdn.getir.com/product/5c3f4bdcf9ba5f0001e7b0d9_tr_1609902603858.jpeg","10","optic white")
w1 = Wallet("Personel wallet",2000)
k_1.iskonto(15.70)
w1.spending(k_1,3)
k_2.zam(2.45)
w1.spending(k_2,2)
k_3.zam(1.5)
w1.spending(k_3,4)
k_4.iskonto(3.45)
w1.spending(k_4,2)
k_5.iskonto(14)
w1.spending(k_5,3)
w1.print_info()
