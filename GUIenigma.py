import tkinter as tk
from tkinter import ttk

def click_button1():
    refer=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    rotor1=['U', 'J', 'X', 'A', 'T', 'D', 'B', 'P', 'Q', 'C', 'S', 'I', 'Y', 'E', 'N', 'H', 'R', 'M', 'Z', 'F', 'W', 'G', 'L', 'V', 'K', 'O']
    rotor2=['P', 'A', 'Q', 'O', 'Y', 'N', 'R', 'B', 'M', 'S', 'D', 'L', 'C', 'K', 'T', 'E', 'J', 'U', 'Z', 'X', 'F', 'G', 'V', 'H', 'I', 'W']
    rotor3=['M', 'O', 'U', 'E', 'W', 'L', 'N', 'Q', 'A', 'B', 'P', 'C', 'K', 'Y', 'J', 'Z', 'R', 'D', 'I', 'X', 'S', 'H', 'V', 'F', 'T', 'G']
    rotor4=['H', 'M', 'O', 'G', 'Q', 'S', 'I', 'W', 'Y', 'Z', 'F', 'V', 'E', 'X', 'J', 'U', 'D', 'T', 'R', 'C', 'K', 'P', 'N', 'B', 'L', 'A']
    rotor5=['F', 'Y', 'N', 'J', 'X', 'C', 'Z', 'I', 'W', 'D', 'B', 'T', 'H', 'U', 'K', 'V', 'A', 'R', 'G', 'S', 'L', 'Q', 'P', 'O', 'M', 'E']
    ref1=['I', 'Z', 'P', 'A', 'U', 'F', 'L', 'C', 'X', 'S', 'V', 'E', 'M']
    ref2=['Q', 'G', 'O', 'H', 'Y', 'N', 'B', 'T', 'K', 'W', 'D', 'J', 'R']
    count1=0
    count2=0
    rotors=[rotor1,rotor2,rotor3,rotor4,rotor5]

    pairs=[]
    pairs.append(pair1.get())
    pairs.append(pair2.get())
    pairs.append(pair3.get())
    pairs.append(pair4.get())
    pairs.append(pair5.get())
    pairs.append(pair6.get())
    pairs.append(pair7.get())
    pairs.append(pair8.get())
    pairs.append(pair9.get())
    pairs.append(pair10.get())
    print(alpha)
    for pair in pairs:
        exc=pair.upper()
        print(exc)
        exclist=[str(i) for i in (exc)]
        print(exclist)
        for i in range(26):
            if alpha[i]==exclist[0]:
                for j in range(26):
                    if alpha[j]==exclist[1]:
                        temp=alpha[i]
                        alpha[i]=alpha[j]
                        alpha[j]=temp
                        break
                break
    print(alpha)
    temp=int(combo1.get())
    temp=temp-1
    for i in range(5):
        if temp==i:
            r1=rotors[i]
            break
    temp=int(combo2.get())
    temp=temp-1
    for i in range(5):
        if temp==i:
            r2=rotors[i]
            break
    temp=int(combo3.get())
    temp=temp-1
    for i in range(5):
        if temp==i:
            r3=rotors[i]
            break

    c1=int(set1.get())
    c1=c1-1
    for i in range(c1):
        temp=r1[0]
        for i in range(25):
            r1[i]=r1[i+1]
        r1[25]=temp
    c2=int(set2.get())
    c2=c2-1
    for i in range(c2):
        temp=r2[0]
        for i in range(25):
            r2[i]=r2[i+1]
        r2[25]=temp
    c3=int(set3.get())
    c3=c3-1
    for i in range(c3):
        temp=r3[0]
        for i in range(25):
            r3[i]=r3[i+1]
        r3[25]=temp

    text=message.get()
    text=text.upper()
    text=[str(i) for i in (text)]

    for j in range(len(text)):
        for i in range(26):
            if text[j]==alpha[i]:
                text[j]=refer[i]
                break

    for j in range(len(text)):
        letter=text[j]
        
        count1=count1+1
        temp=r1[0]
        for i in range(25):
            r1[i]=r1[i+1]
        r1[25]=temp
        if count1%26==0:
            count2=count2+1
            temp=r2[0]
            for i in range(25):
                r2[i]=r2[i+1]
            r2[25]=temp
            if count2%26==0:
                temp=r3[0]
                for i in range(25):
                    r3[i]=r3[i+1]
                r3[25]=temp
                
        for i in range(26):
            if letter==refer[i]:
                letter=r1[i]
                break
        for i in range(26):
            if letter==refer[i]:
                letter=r2[i]
                break
        for i in range(26):
            if letter==refer[i]:
                letter=r3[i]
                break
        
        if letter in ref1:
            for i in range(13):
                if letter==ref1[i]:
                    letter=ref2[i]
                    break
        else:
            for i in range(13):
                if letter==ref2[i]:
                    letter=ref1[i]
                    break

        for i in range(26):
            if letter==r3[i]:
                letter=refer[i]
                break
        for i in range(26):
            if letter==r2[i]:
                letter=refer[i]
                break
        for i in range(26):
            if letter==r1[i]:
                letter=refer[i]
                break
        text[j]=letter

    for j in range(len(text)):
        for i in range(26):
            if text[j]==refer[i]:
                text[j]=alpha[i]
                break

    str1=""
    for i in text:
        str1=str1+i
        
    code.set(str1)
        
def click_button2():
    message.set("")
    code.set("")

root=tk.Tk()
root.title("Enigma Machine")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))

frame=tk.Frame(root, padx=10, pady=10)

frame.pack(fill=tk.BOTH, expand=True)
tk.Label(frame, text="Choose the rotors").grid(column=0, row=0)
rotorCombo=tk.Frame(frame)
rotorCombo.grid(column=0, row=1, columnspan=3, rowspan=2)
tk.Label(rotorCombo, text="Rotor 1").grid(column=0, row=0)
tk.Label(rotorCombo, text="Rotor 2").grid(column=1, row=0)
tk.Label(rotorCombo, text="Rotor 3").grid(column=2, row=0)
combo1=tk.StringVar()
ttk.Combobox(rotorCombo, textvariable=combo1, values=(1,2,3,4,5), width=2).grid(column=0, row=1)
combo2=tk.StringVar()
ttk.Combobox(rotorCombo, textvariable=combo2, values=(1,2,3,4,5), width=2).grid(column=1, row=1)
combo3=tk.StringVar()
ttk.Combobox(rotorCombo, textvariable=combo3, values=(1,2,3,4,5), width=2).grid(column=2, row=1)

tk.Label(frame, text="").grid(column=0, row=3)
tk.Label(frame, text="Set the positions of the rotors").grid(column=0, row=4)
rotorSet=tk.Frame(frame)
rotorSet.grid(column=0, row=5, columnspan=3, rowspan=2)
tk.Label(rotorSet, text="Rotor 1").grid(column=0, row=0)
tk.Label(rotorSet, text="Rotor 2").grid(column=1, row=0)
tk.Label(rotorSet, text="Rotor 3").grid(column=2, row=0)
set1=tk.StringVar()
ttk.Combobox(rotorSet, textvariable=set1, values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26), width=2).grid(column=0, row=1)
set2=tk.StringVar()
ttk.Combobox(rotorSet, textvariable=set2, values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26), width=2).grid(column=1, row=1)
set3=tk.StringVar()
ttk.Combobox(rotorSet, textvariable=set3, values=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26), width=2).grid(column=2, row=1)

tk.Label(frame, text="").grid(column=0, row=7)
tk.Label(frame, text="Enter the alphabet pairs to be swapped").grid(column=0, row=8)
switches=tk.Frame(frame)
switches.grid(column=0, row=9, columnspan=5, rowspan=2)
pair1=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair1).grid(column=0, row=0)
pair2=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair2).grid(column=1, row=0)
pair3=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair3).grid(column=2, row=0)
pair4=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair4).grid(column=3, row=0)
pair5=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair5).grid(column=4, row=0)
pair6=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair6).grid(column=0, row=1)
pair7=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair7).grid(column=1, row=1)
pair8=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair8).grid(column=2, row=1)
pair9=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair9).grid(column=3, row=1)
pair10=tk.StringVar()
tk.Entry(switches, width=4, textvariable=pair10).grid(column=4, row=1)

tk.Label(frame, text="").grid(column=0, row=11)
buttonFrame=tk.Frame(frame)
buttonFrame.grid(column=0, row=12, columnspan=2)
button1=tk.Button(buttonFrame, text="OK", command=click_button1).grid(column=0, row=0)
button2=tk.Button(buttonFrame, text="Clear", command=click_button2).grid(column=1, row=0)

tk.Label(frame, text="").grid(column=0, row=13)
tk.Label(frame, text="Enter the message").grid(column=0, row=14)
message=tk.StringVar()
tk.Entry(frame, width=50, textvariable=message).grid(column=0, row=15)
tk.Label(frame, text="").grid(column=0, row=16)
tk.Label(frame, text="Encrypted message is").grid(column=0, row=17)
code=tk.StringVar()
tk.Entry(frame, width=50, textvariable=code, state="readonly").grid(column=0, row=18)
root.mainloop()
