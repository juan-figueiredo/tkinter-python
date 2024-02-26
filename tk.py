from tkinter import Tk, Label, Button, StringVar, Entry

window = Tk()

rotule = Label(window, text="Nome: ", font=("Arial", 14), foreground="black")
rotule.pack()

message = Label(window, font=('Arial', 14))
message.pack()


user_email = StringVar()
user_password = StringVar()

email_input = Entry(window, textvariable=user_email, bg="white", width = 35)
email_input.pack()

rotulee = Label(window, text="Senha: ", font=("Arial", 14), foreground="black")
rotulee.pack()
"\n"

password_input = Entry(window, textvariable=user_password, bg="white", show="*", width = 35)
password_input.pack()


def show_message():
    message.config(text=f'Seja bem-vindo(a) {user_email.get()}')

button = Button(window, text="Clique para Logar",command=show_message, borderwidth=1, bg="lightblue")
button.pack()

window.mainloop()
