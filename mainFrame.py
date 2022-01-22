import math
import random
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog as fd
from Algo import *
import matplotlib.pyplot as plt
import numpy as np

class MFrame(Frame):

    def __init__(self, window):
        Frame.__init__(self, window)
        self.configure(bg="#a6cff5")
        self.canvas = Canvas(
            self,
            bg="#a6cff5",
            height=782,
            width=1100,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=r"assets/background.png")
        self.background = self.canvas.create_image(
            563.0, 396.0,
            image=self.background_img)

        self.entry0_img = PhotoImage(file=f"assets/img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            419.0, 203.0,
            image=self.entry0_img)
        self.entry0 = Text(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)
        self.entry0.place(
            x=173, y=152,
            width=492,
            height=100)

        self.entry1_img = PhotoImage(file=f"assets/img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            419.0, 377.0,
            image=self.entry1_img)

        self.entry1 = Text(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.entry1.place(
            x=173, y=326,
            width=492,
            height=100)



        self.entry2_img = PhotoImage(file=f"assets/img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(
            968.0, 158.5,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.entry2.place(
            x=937.0, y=141,
            width=62.0,
            height=33)

        self.entry3_img = PhotoImage(file=f"assets/img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(
            810.0, 232,
            image=self.entry3_img)

        self.entry3 = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)

        self.entry3.place(
            x=779.0, y=215,
            width=62.0,
            height=33)

        self.img0 = PhotoImage(file=f"assets/img0.png")
        self.img0_hover = PhotoImage(file="assets/img0_hover.png")
        self.b0 = Label(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b0.place(
            x=714, y=326,
            width=157,
            height=58)
        self.changeOnHover(self.b0, self.img0, self.img0_hover)
        self.b0.bind("<Button-1>", func=lambda e: self.btn_clicked("insertion"))


        self.img1 = PhotoImage(file=f"assets/img1.png")
        self.img1_hover = PhotoImage(file="assets/img1_hover.png")
        self.b1 = Label(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")
        self.b1.bind("<Button-1>", func=lambda e: self.btn_clicked("random"))

        self.b1.place(
            x=889, y=203,
            width=157,
            height=58)
        self.changeOnHover(self.b1, self.img1, self.img1_hover)

        self.img2 = PhotoImage(file=f"assets/img2.png")
        self.img2_hover = PhotoImage(file="assets/img2_hover.png")
        self.b2 = Label(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b2.place(
            x=905, y=326,
            width=157,
            height=58)
        self.changeOnHover(self.b2, self.img2, self.img2_hover)
        self.b2.bind("<Button-1>", func=lambda e: self.btn_clicked("merge"))


        self.img3 = PhotoImage(file=f"assets/img3.png")
        self.img3_hover = PhotoImage(file="assets/img3_hover.png")
        self.b3 = Label(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b3.place(
            x=714, y=407,
            width=157,
            height=58)
        self.changeOnHover(self.b3, self.img3, self.img3_hover)
        self.b3.bind("<Button-1>", func=lambda e: self.btn_clicked("bubble"))

        self.img4 = PhotoImage(file=f"assets/img4.png")
        self.img4_hover = PhotoImage(file="assets/img4_hover.png")
        self.b4 = Label(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b4.place(
            x=905, y=407,
            width=157,
            height=58)
        self.changeOnHover(self.b4, self.img4, self.img4_hover)
        self.b4.bind("<Button-1>", func=lambda e: self.btn_clicked("counting"))

        self.img5 = PhotoImage(file=f"assets/img5.png")
        self.img5_hover = PhotoImage(file="assets/img5_hover.png")
        self.b5 = Label(
            image=self.img5,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b5.place(
            x=905, y=488,
            width=157,
            height=58)
        self.changeOnHover(self.b5, self.img5, self.img5_hover)
        self.b5.bind("<Button-1>", func=lambda e: self.btn_clicked("quick"))

        self.img6 = PhotoImage(file=f"assets/img6.png")
        self.img6_hover = PhotoImage(file="assets/img6_hover.png")
        self.b6 = Label(
            image=self.img6,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b6.place(
            x=812, y=591,
            width=156,
            height=58)
        self.changeOnHover(self.b6, self.img6, self.img6_hover)
        self.b6.bind("<Button-1>", func=lambda e: self.btn_clicked("selection"))

        self.img7 = PhotoImage(file=f"assets/img7.png")
        self.img7_hover = PhotoImage(file="assets/img7_hover.png")
        self.b7 = Label(
            image=self.img7,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b7.place(
            x=714, y=483,
            width=153,
            height=68)
        self.changeOnHover(self.b7, self.img7, self.img7_hover)
        self.b7.bind("<Button-1>", func=lambda e: self.btn_clicked("radix"))

        self.img8 = PhotoImage(file=f"assets/img8.png")
        self.img8_hover = PhotoImage(file="assets/img8_hover.png")
        self.b8 = Label(
            image=self.img8,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b8.place(
            x=580, y=440,
            width=92,
            height=37)
        self.changeOnHover(self.b8, self.img8, self.img8_hover)
        self.b8.bind("<Button-1>", func=lambda e: self.btn_clicked("plot"))

        self.img9_hover = PhotoImage(file=f"assets/img9_hover.png")
        self.img9 = PhotoImage(file=f"assets/img9.png")
        self.b9 = Label(
            image=self.img9,
            borderwidth=0,
            highlightthickness=0,
            relief="flat")

        self.b9.place(
            x=817, y=672,
            width=156,
            height=58)
        self.changeOnHover(self.b9, self.img9, self.img9_hover)
        self.b9.bind("<Button-1>", func= lambda e: self.btn_clicked("heap"))

        self.img10 = PhotoImage(file=f"assets/img10.png")
        self.img10_hover = PhotoImage(file=f"assets/img10_hover.png")
        self.b10 = Label(
            image=self.img10,
            borderwidth=0,
            bg="#a6cff5",
            highlightthickness=0,
            relief="flat")

        self.b10.place(
            x=550, y=265,
            width=122,
            height=47)
        self.b10.bind("<Button-1>", func= lambda e: self.btn_clicked("random_csv"))
        self.changeOnHover(self.b10, self.img10, self.img10_hover)


        self.img11 = PhotoImage(file=f"assets/img11.png")
        self.img11_hover = PhotoImage(file=f"assets/img11_hover.png")
        self.b11 = Label(
            image=self.img11,
            borderwidth=0,
            bg="#a6cff5",
            highlightthickness=0,
            relief="flat")

        self.b11.place(
            x=173, y=265,
            width=122,
            height=47)
        self.b11.bind("<Button-1>", func= lambda e: self.btn_clicked("datafile"))
        self.changeOnHover(self.b11, self.img11, self.img11_hover)


        self.extime = Label(self.canvas, text="", bg="#a6cff5", font=("Montserrat", 12, "bold"))
        self.extime.place(x=287, y=438)
        self.steps = Label(self.canvas, text="", bg="#a6cff5", font=("Montserrat", 12, "bold"))
        self.steps.place(x=297, y=470)

        self.unordered_list = []
        self.ordered_list = []
        self.plot_sort = {
            "merge": IntVar(),
            "heap": IntVar(),
            "selection": IntVar(),
            "insertion": IntVar(),
            "bubble": IntVar(),
            "quick": IntVar(),
            "counting": IntVar(),
            "radix": IntVar(),
            "O(n^2)": IntVar(),
            "O(n)": IntVar(),
            "O(nlog)": IntVar()
        }
        self.c0 = Checkbutton(self, text="merge sort",bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5",variable=self.plot_sort["merge"])
        self.c0.place(x=175, y=500)

        self.c1 = Checkbutton(self, text="insertion sort",bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["insertion"])
        self.c1.place(x=285, y=500)

        self.c2 = Checkbutton(self, text="heap sort",bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["heap"])
        self.c2.place(x=405, y=500)

        self.c3 = Checkbutton(self, text="bubble sort",bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["bubble"])
        self.c3.place(x=505, y=500)

        self.c4 = Checkbutton(self, text="quick sort", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["quick"])
        self.c4.place(x=175, y=530)

        self.c5 = Checkbutton(self, text="selection sort", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["selection"])
        self.c5.place(x=285, y=530)

        self.c6 = Checkbutton(self, text="radix sort", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["radix"])
        self.c6.place(x=405, y=530)

        self.c7 = Checkbutton(self, text="counting sort", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["counting"])
        self.c7.place(x=505, y=530)

        self.c8 = Checkbutton(self, text="O(n^2)", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["O(n^2)"])
        self.c8.place(x=175, y=560)

        self.c9 = Checkbutton(self, text="O(nlog)", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["O(nlog)"])
        self.c9.place(x=285, y=560)

        self.c10 = Checkbutton(self, text="O(n)", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.plot_sort["O(n)"])
        self.c10.place(x=405, y=560)
        self.negatives = tkinter.IntVar()

        self.c11 = Checkbutton(self, text="Include -ve numbers", bg="#A6CFF5", highlightthickness=0,
                              onvalue=1, offvalue=0, activebackground="#A6CFF5", variable=self.negatives)
        self.c11.place(x=727.0, y=171)



        self.leg = plt.legend()

    def btn_clicked(self, type):
        if type == "random":
            self.generate_random()
        elif type == "plot":
            self.plot_data()
        elif type == "datafile":
            self.get_data_from_csv()
        elif type == "random_csv":
            self.write_data_to_csv()
        else:
            self.sort(type)

    def get_data_from_csv(self):
        filetypes = (("csv files", "*.csv"),)
        filepath = fd.askopenfilename(
            filetype=filetypes,
            title="Open a file",
            initialdir="/"
        )
        if filepath == "":
            return
        with open(filepath, "r") as f:
            arr = [elem.replace("\n", "") for elem in f]
            self.write(arr)

    def write_data_to_csv(self):
        b = [elem for elem in (self.entry0.get("1.0", "end-1c")).split(',')]
        with open("Random.csv", "w") as f:
            for elem in b:
                f.write(elem + "\n")
        tkinter.messagebox.showinfo(title="Success", message="Random.csv generated successfully")

    def get_plot_data(self, type):
        ypoints = []
        for i in range(10, len(self.unordered_list), int(self.entry3.get())):
            b = [elem for elem in self.unordered_list[:i]]
            if type == "bubble":
                a = Algo.bubble_sort(b)
                ypoints.append(a[1])
            elif type == "quick":
                arr2 = b
                steps = Algo.quick_sort(0, len(arr2) - 1, arr2)
                ypoints.append(steps)
            elif type == "insertion":
                a = Algo.insertion_sort(b)
                ypoints.append(a[1])
            elif type == "merge":
                a = Algo.merge_sort(b)
                ypoints.append(a[1])
            elif type == "radix":
                if self.negatives.get() == 1:
                    a = Algo.radix_sort_neg(b)
                else:
                    a = Algo.radix_sort(b)
                ypoints.append(a[1])
            elif type == "counting":
                if self.negatives.get() == 1:
                    a = Algo.counting_sort_neg(b)
                else:
                    a = Algo.counting_sort(b)
                ypoints.append(a[1])
            elif type == "selection":
                a = Algo.selection_sort(b)
                ypoints.append(a[1])
            elif type == "heap":
                a = Algo.heap_sort(b)
                ypoints.append(a[1])
            elif type == "O(n^2)":
                ypoints.append(i*i)
            elif type == "O(n)":
                ypoints.append(i)
            elif type == "O(nlog)":
                ypoints.append(i * math.log2(i))

        return np.array(ypoints)

    def plot_data(self):
        self.leg.remove()
        plt.clf()
        plt.cla()
        if len(self.unordered_list) < 100:
            tkinter.messagebox.showerror(title="Insufficient Data", message="please generate at least 100 "
                                                                            "elements before plotting")
            return
        if self.entry3.get() == "" or int(self.entry3.get()) == 0:
            tkinter.messagebox.showerror(title="Invalid Input", message="Step needs to be more than 0")
            return

        xpoints = [i for i in range(10, len(self.unordered_list), int(self.entry3.get()))]
        for key, value in self.plot_sort.items():
            if value.get() == 1:
                ypoints = self.get_plot_data(key)
                plt.plot(xpoints, ypoints, label=f"{key}")
            self.leg = plt.legend()
            plt.xlabel("Array Size")
            plt.ylabel("# of Operations")
            plt.title("Selected Algorithms vs Array Size")
            plt.gcf().canvas.set_window_title("Sorting Algorithms Graph")
        plt.show()

    def generate_random(self):
        number = int(self.entry2.get())
        b = None
        if number > 0:
            if self.negatives.get() == 1:
                b = [random.randint(-1 * number, number) for _ in range(number)]
            else:
                b = [random.randint(1, number+1) for _ in range(number)]
            self.unordered_list = b
            arr = [str(elem) for elem in self.unordered_list]
            self.write(arr)
        else:
            tkinter.messagebox.showerror(title="Invalid Number", message=f"Cannot Generate {number} random numbers."
                                                                         f"\n please enter a +ve value")

    def write(self, arr):
        self.entry0.delete("1.0", END)
        srand = ",".join(arr)
        self.entry0.insert(END, srand)

    def sort(self, type):
        self.entry1.delete("1.0", END)
        self.unordered_list = [int(elem) for elem in (self.entry0.get("1.0", "end-1c")).split(',')]
        b = [elem for elem in self.unordered_list]
        if type == "bubble":
            self.ordered_list, steps = Algo.bubble_sort(b)
        if type == "quick":
            arr2 = b
            steps = Algo.quick_sort(0, len(arr2)-1, arr2)
            self.ordered_list = arr2
        if type == "insertion":
            self.ordered_list, steps = Algo.insertion_sort(b)
        if type == "merge":
            self.ordered_list, steps = Algo.merge_sort(b)
        if type == "radix":
            if self.negatives.get() == 1:
                self.ordered_list, steps = Algo.radix_sort_neg(b)
            else:
                self.ordered_list, steps = Algo.radix_sort(b)
        if type == "counting":
            if self.negatives.get() == 1:
                self.ordered_list, steps = Algo.counting_sort_neg(b)
            else:
                self.ordered_list, steps = Algo.counting_sort(b)

        if type == "selection":
            self.ordered_list, steps = Algo.selection_sort(b)
        if type == "heap":
            self.ordered_list, steps = Algo.heap_sort(b)
        arr = [str(elem) for elem in self.ordered_list]
        srand = ",".join(arr)
        self.entry1.insert(END, srand)
        self.extime.configure(text=f"{steps * 1e-9} s")
        self.steps.configure(text=f"{steps}")

    def changeOnHover(self, button, color, color_hover):
        button.bind("<Enter>", func=lambda e: button.configure(image=color_hover))
        button.bind("<Leave>", func=lambda e: button.configure(image=color))
