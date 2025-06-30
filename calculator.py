import tkinter as tk

def main():
    root = tk.Tk() 
    
    DiceGameLayout(root)
    root.mainloop()



def DiceGameLayout(root):
     
    label_1 = tk.Label(root,text="Dice Game")
    label_1.pack()

    label_2 = tk.Label(root,text="Computer")
    label_2.pack()

        # hiiii Seerat
        # Hi Stavros
        

    Text_Box_1 = tk.Entry(root, justify= "center")
    Text_Box_1.insert(0,"Computer")
    Text_Box_1.pack()

main()