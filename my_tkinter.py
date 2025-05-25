import tkinter as tk
import random

# Əsas pəncərə
root = tk.Tk()
root.title("Login Səhifəsi - Matrix Effekti ilə")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="black")

# Canvas - matrix kodu üçün
canvas = tk.Canvas(root, width=400, height=300, bg="black", highlightthickness=0)
canvas.place(x=0, y=0)

# Matrix stilində 0 və 1-lər
colors = ["#00FF00", "#33FF33", "#66FF66", "#99FF99", "#CCFFCC"]  # yaşılın müxtəlif çaları

matrix_texts = []
for y in range(0, 300, 20):
    row = []
    for x in range(0, 400, 20):
        txt = canvas.create_text(x+10, y+10, text=random.choice(["0", "1"]),
                                 fill=random.choice(colors), font=("Courier", 14, "bold"))
        row.append(txt)
    matrix_texts.append(row)

def update_matrix():
    for row in matrix_texts:
        for txt in row:
            canvas.itemconfig(txt, text=random.choice(["0", "1"]),
                              fill=random.choice(colors))
    root.after(200, update_matrix)

update_matrix()

# Login form üçün qara fonlu çərçivə
frame = tk.Frame(root, bg="#111111", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Başlıq
label_title = tk.Label(frame, text="Xoş gəlmisiniz!", fg="white", bg="#111111", font=("Helvetica", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# İstifadəçi adı
label_user = tk.Label(frame, text="İstifadəçi adı:", fg="#00FF00", bg="#111111", font=("Arial", 12))
label_user.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_user = tk.Entry(frame, font=("Arial", 12))
entry_user.grid(row=1, column=1, padx=10, pady=5)

# Şifrə
label_pass = tk.Label(frame, text="Şifrə:", fg="#00FF00", bg="#111111", font=("Arial", 12))
label_pass.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_pass = tk.Entry(frame, show="*", font=("Arial", 12))
entry_pass.grid(row=2, column=1, padx=10, pady=5)

# Status mesajı
status_label = tk.Label(frame, text="", fg="red", bg="#111111", font=("Arial", 12))
status_label.grid(row=4, column=0, columnspan=2, pady=5)

# Giriş düyməsi funksiyası
def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        status_label.config(text="Giriş uğurla tamamlandı!", fg="#00FF00")
    else:
        status_label.config(text="İstifadəçi adı və ya şifrə səhvdir.", fg="red")

btn_login = tk.Button(frame, text="Giriş", width=15, bg="#00FF00", fg="black", font=("Arial", 12, "bold"), command=login)
btn_login.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
