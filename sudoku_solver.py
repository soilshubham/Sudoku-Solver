import tkinter as tk

primaryColor = "#1c1c1c"
redColor = "#ff4336"
orangeColor = "#ffa13d"
greenColor = "#3dff61"
textColor = "#a1a1a1"

# Finds the empty slots and returns true
def findZeros(arr, zero):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                zero[0] = row
                zero[1] = col
                return True
    return False

# Check if a number can be inserted into the given row and col in an array
def isValueSafe(arr, i, j, num):
    quad_i = i - i%3
    quad_j = j - j%3
    flag = 1
    for row in range(3):
        for col in range(3):
            if num == arr[quad_i+row][quad_j+col]: return False
    for c in range(9):
        if num == arr[(i+c)%9][j]: return False
        elif num == arr[i][(j+c)%9]: return False
    return True

# Checks if the input is valid or not
def isInputSafe(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j] <0 and arr[i][j] >9: return False
            if arr[i][j]!=0:
                quad_i = i - i%3
                quad_j = j - j%3
                count=0
                for row in range(3):
                    for col in range(3):
                        if arr[i][j] == arr[quad_i+row][quad_j+col] :
                            count += 1
                    if count>1: return False
                for c in range(9):
                    if arr[i][j] == arr[c][j] and c!=i: return False
                    if arr[i][j] == arr[i][c] and c!=j: return False
    return True

# Solves the sudoku
def solve(arr):
    zero =[0, 0]
    if not findZeros(arr, zero): return True
    row = zero[0]
    col = zero[1]
    for num in range(1, 10):
        if(isValueSafe(arr, row, col, num)):
            arr[row][col] = num
            if(solve(arr)):
                return True
            else:
                arr[row][col] = 0
                continue
        else:
            continue
    return False

# Function to display the solution into the slots
def displaySol(arr):
    for i in range(9):
            for j in range(9):
                t[i][j].delete(0, 'end')
                t[i][j].insert(0, arr[i][j])

# Controller function
def runSolver():
    arrToSolve=[]
    for i in range(9):
        temp = []
        for j in range(9):
            if t[i][j].get() == "": 
                temp.append(0)
                continue
            try:
                val = int(t[i][j].get())
            except:
                msg1.config(text="Invalid Character :/")
                msg1.config(fg=redColor)
                return False

            if val<=9 and val>=0:
                temp.append(val)
            else:
                msg1.config(text="""Input should be
between 1 to 9""")
                msg1.config(fg=redColor)
                return False
        arrToSolve.append(temp)

    if not isInputSafe(arrToSolve):
        msg1.config(text="No Solution :(")
        msg1.config(fg=orangeColor)

        return False
    if(solve((arrToSolve))):
        displaySol(arrToSolve)
        msg1.config(text="Solved <3")
        msg1.config(fg=greenColor)
    else:
        msg1.config(text="No Solution :(")
        msg1.config(fg=orangeColor)

# Resets the slots to blank
def reset():
    for i in range(9):
        for j in range(9):
            t[i][j].delete(0, 'end')
            t[i][j].insert(0, "")
    msg1.config(text="""Fill in your Sudoku
and hit Solve!""")
    msg1.config(fg=textColor)


if __name__ == "__main__":

    demoInput = [
        ["", "", "", "", "", "", 6, 8, ""],
        ["", "", "", "", 7, 3, "", "", 9],
        [3, "", 9, "", "", "", "", 4, 5],
        [4, 9, "", "", "", "", "", "", ""],
        [8, "", 3, "", 5, "", 9, "", 2],
        ["", "", "", "", "", "", "", 3, 6],
        [9, 6, "", "", "", "", 3, "", 8],
        [7, "", "", 6, 8, "", "", "", ""],
        [0, 2, 8, "", "", "", "", "", ""]
        ]
    
    app = tk.Tk()
    app.title('Sudoku Solver - soilshubham')
    app.geometry("1200x700")
    app.resizable(False, False)
    app.config(bg=primaryColor)
    app.iconbitmap("icon.ico")

    sudokuFrame = tk.Frame(app, bg='#969696')
    sudokuFrame.grid(row=0, column=0, padx="20", pady="20")

    btnFrame = tk.Frame(app, bg=primaryColor)
    btnFrame.place(x="830", y="500")
    btnFrame.grid_columnconfigure(0, weight=1)
    btnFrame.grid_columnconfigure(2, weight=1)

    msgFrame = tk.Frame(app, bg=primaryColor)
    msgFrame.place(x="890", y="300")

    title = tk.Label(app, text='Sudoku Solver', font='Arial 25 bold', bg=primaryColor, fg='#a1a1a1')
    title.place(x="815", y="50")
    subTitle = tk.Label(app, text='- by soilshubham', font='Arial 10', bg=primaryColor, fg='#a1a1a1')
    subTitle.place(x="990", y="120")

    msg1 = tk.Label(msgFrame, text="""Fill in your Sudoku
and hit Solve!""", font='Arial 11', bg=primaryColor, fg=textColor, justify=tk.CENTER)
    msg1.grid(row=0, column=1)
    
    btn_solve = tk.Button(btnFrame, text="Solve", command=runSolver, font='Arial 12', bg='#303030',fg='#a1a1a1', relief="raised")
    btn_solve.grid(row=0, column=0, ipadx="100", ipady="10")
    btn_reset = tk.Button(btnFrame, text="Reset", command=reset, font='Arial 10', bg='#303030',fg='#a1a1a1', relief="raised")
    btn_reset.grid(row=1, column=0, ipadx="105", ipady="8", pady="20")

    t=[]

    for i in range(9):
        k=[]
        for j in range(9):
            ci = i - i%3
            cj = j - j%3
            cT = 10*ci + cj
            if cT in [0, 6, 33, 60, 66]:boxColor = '#f0f0f0'
            else: boxColor = '#ffffff'
            k.append(tk.Entry(sudokuFrame, width=5, justify="center", font='Arial 13', bd=1, relief="flat", bg=boxColor))
            k[j].grid(row=i,column=j, ipadx=4, ipady=20, padx=2, pady=2)

        t.append(k)

    displaySol(demoInput)
    app.mainloop()
