import customtkinter
from PIL import Image

tela = customtkinter.CTk(fg_color="#CFD8DC")  # Cria a tela
tela.title("Tela")  # Define o título da tela
tela.geometry("1360x720")  # Define o tamanho da tela
tela.resizable(False, False)  # Impede que a tela seja 



frame_info = customtkinter.CTkFrame(tela, width=292, height=401, fg_color="#FFDA8F", corner_radius=100).place(x=10, y=275) 

frame_foto = customtkinter.CTkFrame(tela, width=250, height=250, fg_color="black", corner_radius=200, bg_color="#CFD8DC",border_width=1).place(x=20, y=10) 

frame_nome = customtkinter.CTkFrame(tela, width=300, height=100, fg_color="#8690AF", corner_radius=100).place(x=330, y=20)

frame_tipo1 = customtkinter.CTkFrame(tela, width=100, height=100, fg_color="white", corner_radius=100).place(x=800, y=20)

frame_tipo2 = customtkinter.CTkFrame(tela, width=100, height=100, fg_color="white", corner_radius=100).place(x=1000, y=20)

frame_video = customtkinter.CTkFrame(tela, width=900, height=500, fg_color="#FF9EB1", corner_radius=100).place(x=330, y=175)

frame_button_return = customtkinter.CTkFrame(tela, width=50, height=50, fg_color="white", corner_radius=100).place(x=1275, y=650)




tela.mainloop()  # Inicia a tela