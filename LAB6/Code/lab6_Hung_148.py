import tkinter as tk
class ProductListBox:
    def __init__(self,root):
        self.root = root
        self.root.title("Listbox sản phẩm")
        self.root.geometry('300x250')
        self.create_widgets()
    
    def create_widgets(self):
        self.lbl = tk.Label(root,text="Sản phẩm:")
        self.lbl.pack()

        product = ['Chuối','Thanh long','Táo','Cam','Quýt','Ổi','Xoài']
        self.listbox = tk.Listbox(self.root,selectmode=tk.MULTIPLE)
        self.listbox.pack()

        for i in product:
            self.listbox.insert(tk.END, f"{i}")

        self.select_button = tk.Button(self.root,text="Chọn",command=self.on_select)
        self.select_button.pack(pady=10)

    def on_select(self):
        selected_products = [self.listbox.get(index) for index in self.listbox.curselection()]
        print("Sản phẩm được chọn là: ", selected_products)

if __name__ == '__main__':
    root = tk.Tk()
    app = ProductListBox(root)
    root.mainloop()
     
