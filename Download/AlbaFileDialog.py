import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as mbox
from functools import partial
from PIL import Image, ImageTk
import os

#pulisco il terminale
os.system("clear")

#creo la classe principale della mia finestra e creo la finestra principale
class Edipy(tk.Tk):
	def __init__(self):
		#richiamo il costruttore delal tk.Tk
		super().__init__()
		self.grandezza_finestra = "400x400"
		
		#variabili menu
		self.sfondo = "#1c2226"
		self.sfondo_scritta = "white"
		self.user_name = "Utente"
		self.message_benvenuto = f"Benvenuto su Edipy {self.user_name}"
		self.image_user = None
		self.h_img = 8
		self.w_img = 15
		
		#variabili impostazioni
		self.path_predefinita = "/home"
		self.width_tab = 30
		
		#variabili popup metodi prefatti
		self.variable_radio = tk.StringVar()
		self.save_code = ""
		
		self.geometry(self.grandezza_finestra)
		self.title("Alba - Edipy")
		self.resizable(0, 0)
		self.config(bg = self.sfondo)
		self.crea_widgets()
	
	def crea_widgets(self):
		self.crea_menu()
	
	def crea_menu(self, can_remove = False, fin = None):	
		#mi salvo il codice che l'utente ha digitato all'interno della Text() in tal caso
		#non esista ancora il widgets gestisco i vari errori
		try:
			self.save_code = str(self.blocco_lavoro.get("1.0", "end"))
		except AttributeError:
			self.save_code = ""
		except tk.TclError:
			pass
		
		#rimuovo la finestra precedente in tal modo da far visualizzare solo il menu quando necessario
		if can_remove == True:
			fin.destroy()
		
		#per sicurezza rimposto la grandezza della finestra principale in tal caso siamo andati nell'edipy
		#che al suo interno viene ingrandita la finestra 
		self.geometry(self.grandezza_finestra)
		
		#creo il frame e grazie alla place() riesco a centrare il frame
		wm = tk.Frame(self, bg = self.sfondo)
		wm.place(relx = 0.5, rely = 0.45, anchor = tk.CENTER)
		
		#creazione dei widgets
		title_win = tk.Label(wm, text = "MENU", font = ("Arial", 16, "bold"), bg = self.sfondo, fg = self.sfondo_scritta)
		title_win.grid(row = 0, column = 0)
		
		self.button_user_image = tk.Button(wm, image = self.image_user, height = self.h_img, width = self.w_img, text = "carica immagine...", command = self.aggiungi_foto)
		self.button_user_image.grid(row = 1, column = 0, pady = (10, 0))
		
		self.label_benvenuto = tk.Label(wm, bg = self.sfondo, text = self.message_benvenuto, fg = self.sfondo_scritta)
		self.label_benvenuto.grid(row = 2, column = 0, pady = (10, 0))
		
		button_settings = tk.Button(wm, text = "IMPOSTAZIONI", command = partial(self.crea_impostazioni, wm))
		button_settings.grid(row = 3, column = 0, pady = (10, 0))
		
		button_create = tk.Button(wm, text = "EDIPY", width = 14, command = partial(self.crea_progetto, wm))
		button_create.grid(row = 4, column = 0, pady = (10, 0))
		
		button_exit = tk.Button(wm, text = "ESCI", width = 14, command = self.destroy)
		button_exit.grid(row = 5, column = 0, pady = (10, 0))
		
		#riconfiguoro il nome dell'utente ogni volta che entra nel menu in tal caso
		#l'utente abbia cambiato il suo user name dalle impostazioni
		self.label_benvenuto.config(text = f"Benvenuto su Edipy {self.user_name}")

	def aggiungi_foto(self):
		"""
		Con il file dialog.askopenfilename() l'utente può selezionare l'immagine che 
		vuole, in più evito che l'utente possa iserire qualsiasi tipo di file limitando l'apertura
		dei file solo per il tipo di estensioni che io vado ad elencare all'interno della tupla grazie 
		all'opzione filetypes, e io riceverò la posizione dell'immagine, in cui uccessivamente grazie il
		metodo tk.PhotoImage() potrò andar a visualizzare l'immagine all'interno del mio programma
		"""
		
		try:
			path_img = filedialog.askopenfilename(initialdir = self.path_predefinita, filetypes=[('Image Files', ('*.png', '*.jpg', '*.jpeg'))])
			#self.image_user = tk.PhotoImage(file = path_img) --> così non puoi gestire la dimensione delle immagini
			#imposto grandezza button per la selezione delle immagini
			self.w_img = 125
			self.h_img = 125
			
			#uso il modulo PIL perchè ha la funzione adatta per ridimensionare l'immagine
			#e alla fine lo faccio diventare un oggetto di tipo PhotoImage così viene
			#riconosciuto dalla tkinter
			op_img = Image.open(path_img)
			resized_img = op_img.resize((self.w_img, self.h_img))
			self.image_user = ImageTk.PhotoImage(resized_img)
			
			self.button_user_image.config(image = self.image_user, activebackground = self.sfondo, bg = self.sfondo, width = 125, height = 125)
		
		except AttributeError:
			#imposto grandezza button per la selezione delle immagini e mostro errore se
			#l'utente ha solo schiacciato aggiugi immagine ma ha schiacciato la x
			self.w_img = 15
			self.h_img = 8
			mbox.showwarning("Attenzione!", "Nessuna immagine è stata caricata!")
		
	def crea_impostazioni(self, fin):
		#mi salvo il codice che l'utente ha digitato all'interno della Text() in tal caso
		#non esista ancora il widgets gestisco i vari errori
		try:
			self.save_code = str(self.blocco_lavoro.get("1.0", "end"))
		except AttributeError:
			self.save_code = ""
		except tk.TclError:
			pass
	
		#distruggo qualsiasi finestra precedente
		fin.destroy()
		
		#per sicurezza rimposto la grandezza della finestra principale in tal caso siamo andati nell'edipy
		#che al suo interno viene ingrandita la finestra 
		self.geometry(self.grandezza_finestra)
		
		#creo il frame e grazie alla place() riesco a centrare il frame
		wi = tk.Frame(self, bg = self.sfondo)
		wi.place(relx = 0.5, rely = 0.45, anchor = tk.CENTER)
		
		#creo i widgets necessari per la mia finestra
		title_win = tk.Label(wi, text = "IMPOSTAZIONI", font = ("Arial", 16, "bold"), bg = self.sfondo, fg = self.sfondo_scritta)
		title_win.grid(row = 0, column = 0, columnspan = 2)
		
		lbl_username = tk.Label(wi, text = "Nome utente: ", bg = self.sfondo, fg = self.sfondo_scritta)
		lbl_username.grid(row = 1, column = 0, pady = 15)
		
		self.input_name = tk.Entry(wi)
		self.input_name.grid(row = 1, column = 1, pady = 15, ipady = 8, ipadx = 5)
		
		lbl_width_tab = tk.Label(wi, text = "Larghezza tabulazioni: ", bg = self.sfondo, fg = self.sfondo_scritta)
		lbl_width_tab.grid(row = 2, column = 0, pady = 15)
		
		self.input_width_tab = tk.Entry(wi)
		self.input_width_tab.grid(row = 2, column = 1, pady = 15, ipady = 8, ipadx = 5)
		
		lbl_save_path = tk.Label(wi, text = "Percorso predefinito: ", bg = self.sfondo, fg = self.sfondo_scritta)
		lbl_save_path.grid(row = 3, column = 0, pady = 15)
		
		self.input_save_path = tk.Entry(wi)
		self.input_save_path.grid(row = 3, column = 1, pady = 15, ipady = 8, ipadx = 5)
		
		btn_home = tk.Button(wi, text = "SALVA", width = 20, command = self.salva_impostazioni)
		btn_home.grid(row = 4, column = 0, padx = (0, 10))
		
		btn_home = tk.Button(wi, text = "MENU", width = 20, command = partial(self.crea_menu, True, wi))
		btn_home.grid(row = 4, column = 1)
		
		btn_edipy = tk.Button(wi, text = "EDIPY", command = partial(self.crea_progetto, wi))
		btn_edipy.grid(row = 5, columnspan = 2, pady = (10, 0), sticky = "WE")
		
		#in tal caso l'utente abbia già effettuato delle modifiche 
		#le inserisco all'intero delle entry
		self.input_name.insert(0, self.user_name)
		self.input_width_tab.insert(0, self.width_tab)
		self.input_save_path.insert(0, self.path_predefinita)
	
	def salva_impostazioni(self):
		#flag controllo errori, valori entry
		no_error = True
		self.user_name = str(self.input_name.get())
		self.path_predefinita = str(self.input_save_path.get())
		
		try:
			self.width_tab = int(self.input_width_tab.get())
			no_error = True
		except ValueError:
			mbox.showerror("Errore - tabulazione", "Errore nell'inserimento del numero di tabulazione")
			no_error = False
			
		if self.user_name.isspace() or self.user_name.isnumeric() or self.user_name == ""  or self.path_predefinita.isspace() or self.path_predefinita.isnumeric() or self.path_predefinita == "":
			mbox.showerror("Errore - campi impostazioni", "Errore nell'inserimento dei campi")
			no_error = False
		
		if no_error == True:
			mbox.showinfo("impostazioni - salvate", f"Le tue impostazioni sono state salvate con successo\n\nNome utente: {self.user_name}\nPercorso predefinito: {self.path_predefinita}\nLarghezza tabulazioni: {self.width_tab}")
		
	def crea_progetto(self, fin):
		#distruggo la finestra precedente
		fin.destroy()
		
		#imposto la grandezza della finestra principale più grande, soltato per avere una visione
		#maggiore all'intero della mia finestra
		self.geometry("1000x750")
		
		#creo i frame e grazie alla place() riesco a centrare il frame padre
		wp = tk.Frame(self, bg = self.sfondo)
		wp.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

		wb = tk.Frame(wp, bg = self.sfondo)
		wb.grid(row = 0, column = 0, padx = (0, 30))

		wbl = tk.Frame(wp, bg = self.sfondo)
		wbl.grid(row = 0, column = 1)

		#creo i widgets necessari per la finestra
		button_settings = tk.Button(wb, text = "IMPOSTAZIONI", command = partial(self.crea_impostazioni, wp))
		button_settings.grid(row = 0, column = 0, pady = (20, 0), sticky = "NSWE")	

		btn_home = tk.Button(wb, text = "MENU", command = partial(self.crea_menu, True, wp))
		btn_home.grid(row = 1, column = 0, sticky = "NSWE", pady = (20, 0))

		btn_cls_set_get = tk.Button(wb, text = "Classe, set + get", command = partial(self.crea_classe_set_get, wp, True ))
		btn_cls_set_get.grid(row = 2, column = 0, pady = (20, 0), sticky = "NSWE")	
		
		btn_cls_set_get = tk.Button(wb, text = "set + get", command = partial(self.crea_classe_set_get, wp, False ))
		btn_cls_set_get.grid(row = 3, column = 0, pady = (20, 0), sticky = "NSWE")
		
		btn_pulisci = tk.Button(wb, text = "PULISCI", command = self.pulisci_blocco)
		btn_pulisci.grid(row = 4, column = 0, sticky = "WE", pady = (20, 0))
		
		btn_save = tk.Button(wb, text = "SALVA", command = self.salva_progetto)
		btn_save.grid(row = 6, column = 0, columnspan = 2, sticky = "WE", pady = (20, 0))
		
		btn_save = tk.Button(wb, text = "CARICA", command = self.carica_progetto)
		btn_save.grid(row = 5, column = 0, sticky = "WE", pady = (20, 0))
		
		self.blocco_lavoro = tk.Text(wbl, width = 102, height = 45, tabs = (self.width_tab), bg = "#283136", fg = "white", borderwidth = 0, insertbackground = 'white')
		self.blocco_lavoro.grid(row = 0, column = 1)
		
		self.blocco_lavoro.insert("1.0", self.save_code)
	
	def crea_classe_set_get(self, fin, class_flag = False):
		#creo un popup per far inserire all'utente il metodo che vuole e graze alla tk.Toplevel()
		#vado a creare una finestra sueriore alla finestra principale
		popup = tk.Toplevel(bg = self.sfondo)
		popup.geometry("350x300")
		popup.title("crea metodi")
		
		#creo il frame e grazie alla place() riesco a centrare il frames
		fp = tk.Frame(popup, bg = self.sfondo)
		fp.place(relx = 0.5, rely = 0.45, anchor = tk.CENTER)
		
		#piccolo controllo per vedere se l'utente ha schiacciato il bottone classe, set e get
		#oppure solo setter e getter + creazione widgets
		if class_flag == True:
			label_nm_cls = tk.Label(fp, text = "Inserisci nome classe: ", bg = self.sfondo, fg = self.sfondo_scritta)
			label_nm_cls.grid(row = 0, column = 0, pady = (10, 0))
			
			self.input_nm_cls = tk.Entry(fp)
			self.input_nm_cls.grid(row = 0, column = 1, ipady = 8, ipadx = 10, pady = (10, 0))
		
		self.radio_private = tk.Radiobutton(fp, text = "Privato: ", variable = self.variable_radio, value = "Privato", bg = self.sfondo, activebackground = self.sfondo, fg = self.sfondo_scritta, activeforeground = self.sfondo_scritta, selectcolor=self.sfondo)
		self.radio_private.grid(row = 1, column = 0, pady = (10, 0))
		
		self.radio_public = tk.Radiobutton(fp, text = "Pubblico: ", variable = self.variable_radio, value = "Pubblico", bg = self.sfondo, activebackground = self.sfondo, fg = self.sfondo_scritta, activeforeground = self.sfondo_scritta, selectcolor=self.sfondo)
		self.radio_public.grid(row = 1, column = 1, pady = (10, 0))
		
		label_primo_attributo = tk.Label(fp, text = "Nome primo attributo: ", bg = self.sfondo, fg = self.sfondo_scritta)
		label_primo_attributo.grid(row = 2, column = 0, pady = (10, 0))
		
		self.input_primo_attributo = tk.Entry(fp)
		self.input_primo_attributo.grid(row = 2, column = 1, ipady = 8, ipadx = 10, pady = (10, 0))
		
		label_secondo_attributo = tk.Label(fp, text = "Nome secondo attributo: ", bg = self.sfondo, fg = self.sfondo_scritta)
		label_secondo_attributo.grid(row = 3, column = 0, pady = (10, 0))
		
		self.input_secondo_attributo = tk.Entry(fp)
		self.input_secondo_attributo.grid(row = 3, column = 1, ipady = 8, ipadx = 10, pady = (10, 0))
		
		btn_aggiungi = tk.Button(fp, text = "AGGIUNGI", command = partial(self.popup_aggiungi, class_flag))
		btn_aggiungi.grid(row = 4, columnspan = 2, sticky = "NSWE", pady = (10, 0))
		
		#valoredi default per i radio button
		self.variable_radio.set("Privato")
	
	def popup_aggiungi(self, fc):
		#flag per il controllo errore delle entry per l'utente
		no_error = True
		atr1 = str(self.input_primo_attributo.get())
		atr2 = str(self.input_secondo_attributo.get())
		valore_radio = str(self.variable_radio.get())
		
		#controllo se ha schiacciato il bottone con classe, set e get... 
		#evitando di fare controlli inutili
		if fc == True:
			nm_cls = str(self.input_nm_cls.get())
			
			if nm_cls.isspace() or nm_cls.isnumeric() or nm_cls == "": 
				mbox.showerror("Errore - nome classe", "Il nome della classe ha una sintassi errata")
				no_error = False
		
		if atr1.isspace() or atr1.isnumeric() or atr1 == "" or atr2.isspace() or atr2.isnumeric() or atr2 == "":
			mbox.showerror("Errore - nome attributi", "I nomi degli attrubuti hanno una sintassi errata")
			no_error = False
		
		#se non è presente alcun errore controllo se ha selezionato un radio
		#per la classe privata oppure pubblica
		if no_error == True:
			if valore_radio == "Privato":
				nome_var1 = f"self.__V{atr1}"
				nome_var2 = f"self.__V{atr2}"
			else:
				nome_var1 = f"self.V{atr1}"
				nome_var2 = f"self.V{atr2}"
			
			#solito controllo per vedere se il codice che devo andare ad inserire dentro la
			#text ha schiacciato il bottone con classe + set e get o solo setter e getter
			if fc == True:
				codice = f"""class {nm_cls}():
	def __init__(self, {atr1}_ex, {atr2}_ex):
		self.set_{atr1}({atr1}_ex)
		self.set_{atr2}({atr2}_ex)
		
	def set_{atr1}(self, {atr1}):
		{nome_var1} = {atr1}
	
	def get_{atr1}(self):
		return {nome_var1}
	
	def set_{atr2}(self, {atr2}):
		{nome_var2} = {atr2}
	
	def get_{atr2}(self):
		return {nome_var2}
						"""
			else:
				codice = f"""	def set_{atr1}(self, {atr1}):
		{nome_var1} = {atr1}

	def get_{atr1}(self):
		return {nome_var1}

	def set_{atr2}(self, {atr2}):
		{nome_var2} = {atr2}

	def get_{atr2}(self):
		return {nome_var2}
						"""
			#ricavo l'indice in cui lampeggia il cursore del mouse e lo inserisco
			#all'intero della text in quella posizione
			indice = self.blocco_lavoro.index(tk.INSERT).split(".")[0]
			self.blocco_lavoro.insert(f"{indice}.0", codice)
	
	def pulisci_blocco(self):
		#pulisco la text
		self.blocco_lavoro.delete("1.0", "end")
	
	def salva_progetto(self):
		"""
		grazie al filedialog.asksaveasfilename() chiedo all'utente in che directory vuole salvare il progetto
		e grazie al metodo initialdir gli inserisci la path principale in cui l'utente vuole andare a salvare
		i suoi futuri progetti, di default ha /home ed e modificabile nelle impostazioni. Proseguendo
		grazie alla filetypes vado a definire all'interno di una tupla che tipo di file vuole salavare, in questo 
		caso .py
		"""
		code = self.blocco_lavoro.get("1.0", "end")
		path_file = filedialog.asksaveasfilename(initialdir = self.path_predefinita, filetypes = [('python file', ('*.py'))])
		
		#qui semplicemente controllo se la path_file restituise True. Faccio una try per aprire il file
		#in modlità scrittura, inserisco il codice e chiudo il file, in caso contrario visualizzo
		#un errore
		if path_file:
			try:
				file_py = open(path_file,'w')
				file_py.write(code)
				file_py.close()
			except IOError:
				mbox.showwarning("Errore", "È stato rilevato un errore nel salvare il file")
	
	def carica_progetto(self):
		"""
		grazie al filedialog.askopenfilename() chiedo all'utente in che directory vuole aprire il progetto
		e grazie al metodo initialdir gli inserisci la path principale in cui l'utente vuole andare a visualizzare
		i suoi futuri progetti, di default ha /home ed e modificabile nelle impostazioni. Proseguendo
		grazie alla filetypes vado a definire all'interno di una tupla che tipo di file vuole salavare, in questo 
		caso .py
		"""
		path_file = filedialog.askopenfilename(initialdir = self.path_predefinita, filetypes=[('Python File', ('*.py'))])
		
		#qui semplicemente controllo se la path_file restituise True. Faccio una try per aprire il file
		#in modlità letturo, prendo il codice e chiudo il file, in caso contrario visualizzo
		#un errore, impossibile aprire file.
		if path_file:
			try:
				file_py = open(path_file,'r')
				res = file_py.read()
				file_py.close()
				
				self.blocco_lavoro.delete("1.0", "end")
				self.blocco_lavoro.insert(f"1.0", res)
				
			except IOError:
				mbox.showwarning("Errore", "È stato rilevato un errore nel caricare il file")
			
#funzione principale per richiamare la mia classe	
def main():
	ep = Edipy()
	ep.mainloop()

main()
	
