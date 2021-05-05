import tkinter as tk

def findZeros(arr, zero):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                zero[0] = row
                zero[1] = col
                return True
    return False

def isSafe(arr, i, j, num):
    quad_i = i - i%3
    quad_j = j - j%3
    flag = 1
    for row in range(3):
        for col in range(3):
            if num == arr[quad_i+row][quad_j+col]:
                return False
    for c in range(9):
        if num == arr[(i+c)%9][j]:
            return False
        elif num == arr[i][(j+c)%9]:
            return False
            
    return True

def isQSafe(arr):
    for i in range(9):
        for j in range(9):
            if arr[i][j]!=0:
                for c in range(9):
                    if arr[i][j] == arr[c][j] and c!=i:
                        return False
                    if arr[i][j] == arr[i][c] and c!=j:
                        return False
                quad_i = i - i%3
                quad_j = j - j%3
                count=0
                for row in range(3):
                    for col in range(3):
                        if arr[i][j] == arr[quad_i+row][quad_j+col] :
                            count += 1
                    if count>1: return False
    return True

def solve(arr):
    zero =[0, 0]
    if(not findZeros(arr, zero)):
        return True
    row = zero[0]
    col = zero[1]
    for num in range(1, 10):
        if(isSafe(arr, row, col, num)):
            arr[row][col] = num
            if(solve(arr)):
                return True
            else:
                arr[row][col] = 0
                continue
        else:
            continue
    return False

def printSol(arr):
    for i in range(9):
            for j in range(9):
                t[i][j].delete(0, 'end')
                t[i][j].insert(0, arr[i][j])

def showSol():
    arrToSolve=[]
    for i in range(9):
        temp = []
        for j in range(9):
            try:
                val = int(t[i][j].get())
            except:
                reset()
                msg1.config(text="Wrong Input :/")
                return False
            temp.append(val)
        arrToSolve.append(temp)

    if not isQSafe(arrToSolve):
        printSol(a3)
        msg1.config(text="No Solution :(")
        return False


    if(solve((arrToSolve))):
        printSol(arrToSolve)
        msg1.config(text="Solved :D")
    else:
        printSol(a3)
        msg1.config(text="No Solution :(")

def reset():
    for i in range(9):
        for j in range(9):
            t[i][j].delete(0, 'end')
            t[i][j].insert(0, 0)
    msg1.config(text="""Fill in your Sudoku
and hit Solve!""")


if __name__ == "__main__":
    a1 = [
        [1, 7, 2, 5, 4,	9, 6, 8, 3],
        [6, 4, 5, 8, 7,	3, 2, 1, 9],
        [3, 8, 9, 2, 6, 1, 7, 4, 5],
        [4, 9, 6, 3, 2, 7, 8, 5, 1],
        [8, 1, 3, 4, 5, 6, 9, 7, 2],
        [2, 5, 7, 1, 9, 8, 4, 3, 6],
        [9, 6, 4, 7, 1, 5, 3, 2, 8],
        [7, 3, 1, 6, 8, 2, 5, 9, 4],
        [5, 2, 8, 9, 3, 4, 1, 6, 7]
        ]
    a2 = [
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]
        ]
    a3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
    
    app = tk.Tk()
    app.title('Sudoku Solver - soilshubham')
    app.geometry("1200x700")
    app.resizable(False, False)
    app.config(bg='#1c1c1c')
    app.iconbitmap("./icon/icon.ico")

    sudokuFrame = tk.Frame(app, bg='#969696')
    sudokuFrame.grid(row=0, column=0, padx="20", pady="20")

    btnFrame = tk.Frame(app, bg='#1c1c1c')
    btnFrame.place(x="830", y="500")

    msgFrame = tk.Frame(app, bg='#1c1c1c')
    msgFrame.place(x="890", y="300")

    title = tk.Label(app, text='Sudoku Solver', font='Arial 25 bold', bg='#1c1c1c', fg='#a1a1a1')
    title.place(x="815", y="50")
    subTitle = tk.Label(app, text='- by soilshubham', font='Arial 10', bg='#1c1c1c', fg='#a1a1a1')
    subTitle.place(x="990", y="120")

    msg1 = tk.Label(msgFrame, text="""Fill in your Sudoku
and hit Solve!""", font='Arial 11', bg='#1c1c1c', fg='#a1a1a1', justify=tk.CENTER)
    msg1.pack()
    

    btn_solve = tk.Button(btnFrame, text="Solve", command=showSol, font='Arial 12', bg='#303030',fg='#a1a1a1', relief="raised")
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

    printSol(a2)
    app.mainloop()
