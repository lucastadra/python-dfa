# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pyDFA import DFA;

# Defining TextEditor Class
class TextEditor:

  # Defining Constructor
  def __init__(self,root):
    # Assigning root
    self.root = root
    # Title of the window
    self.root.title("TEXT EDITOR")
    # Window Geometry
    self.root.geometry("1200x700+200+150")
    # Initializing filename
    self.filename = None
    # Declaring Title variable
    self.title = StringVar()
    # Declaring Status variable
    self.status = StringVar()

    # Creating Titlebar
    self.titlebar = Label(self.root,textvariable=self.title,font=("arial",15,"bold"),bd=2,relief=GROOVE)
    # Packing Titlebar to root window
    self.titlebar.pack(side=TOP,fill=BOTH)
    # Calling Settitle Function
    self.settitle()

    # Creating Statusbar
    self.statusbar = Label(self.root,textvariable=self.status,font=("arial",15,"bold"),bd=2,relief=GROOVE)
    # Packing status bar to root window
    self.statusbar.pack(side=BOTTOM,fill=BOTH)
    # Initializing Status
    self.status.set("Welcome To Text Editor")

    # Creating Menubar
    self.menubar = Menu(self.root,font=("arial",15,"bold"),activebackground="skyblue")
    # Configuring menubar on root window
    self.root.config(menu=self.menubar)

    # Creating File Menu
    self.filemenu = Menu(self.menubar,font=("arial",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding New file Command
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
    # Adding Open file Command
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
    # Adding Save File Command
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
    # Adding Save As file Command
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
    # Adding Check C Tokens Command
    self.filemenu.add_command(label="Check C Tokens",accelerator="Ctrl+T",command=self.checkCTokens)
    # Adding Seprator
    self.filemenu.add_separator()
    # Adding Exit window Command
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
    # Cascading filemenu to menubar
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,font=("arial",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding Cut text Command
    self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
    # Adding Copy text Command
    self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
    # Adding Paste text command
    self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
    # Adding Seprator
    self.editmenu.add_separator()
    # Adding Undo text Command
    self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
    # Cascading editmenu to menubar
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("arial",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding About Command
    self.helpmenu.add_command(label="About",command=self.infoabout)
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    # Creating Text Area
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("arial",15,"bold"),state="normal",relief=GROOVE)
    # Packing scrollbar to root window
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbar to text area
    scrol_y.config(command=self.txtarea.yview)
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)

    # Calling shortcuts funtion
    self.shortcuts()

  # Defining settitle function
  def settitle(self):
    # Checking if Filename is not None
    if self.filename:
      # Updating Title as filename
      self.title.set(self.filename)
    else:
      # Updating Title as Untitled
      self.title.set("Untitled")

  # Defining New file Function
  def newfile(self,*args):
    # Clearing the Text Area
    self.txtarea.delete("1.0",END)
    # Updating filename as None
    self.filename = None
    # Calling settitle funtion
    self.settitle()
    # updating status
    self.status.set("New File Created")

  # Defining Open File Funtion
  def openfile(self,*args):
    # Exception handling
    try:
      # Asking for file to open
      self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      # checking if filename not none
      if self.filename:
        # opening file in readmode
        infile = open(self.filename,"r")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing the file  
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save File Funtion
  def savefile(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Reading the data from text area
        data = self.txtarea.get("1.0",END)
        # opening File in write mode
        outfile = open(self.filename,"w")
        # Writing Data into file
        outfile.write(data)
        # Closing File
        outfile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Saved Successfully")
      else:
        self.saveasfile()
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save As File Funtion
  def saveasfile(self,*args):
    # Exception handling
    try:
      # Asking for file name and type to save
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      # Reading the data from text area
      data = self.txtarea.get("1.0",END)
      # opening File in write mode
      outfile = open(untitledfile,"w")
      # Writing Data into file
      outfile.write(data)
      # Closing File
      outfile.close()
      # Updating filename as Untitled
      self.filename = untitledfile
      # Calling Set title
      self.settitle()
      # Updating Status
      self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Exit Funtion
  def exit(self,*args):
    op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
    if op>0:
      self.root.destroy()
    else:
      return

  def checkCTokens(self,*args):
    # Exception handling
    try:
      # Asking for file name and type to save
      untitledfile = filedialog.asksaveasfilename(title = "Save as",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt")))
      # Reading the data from text area
      data = self.txtarea.get("1.0",END)
      # opening File in write mode
      outfile = open(untitledfile,"w")
      # Writing Data into file
      outfile.write(data)
      # Closing File
      outfile.close()
      # Updating filename as Untitled
      self.filename = untitledfile
      # Calling Set title
      self.settitle()
      # Updating Status
      self.status.set("Saved Successfully")
      # Reading File
      file = open(untitledfile, "r")
      #tempfile.write(data)

      # Leitura do arquivo
      content = file.read()
      # Trata espaçamentos, tabs e quebras de linha
      formattedContent = content.replace('\n', ' ').replace('\t', ' ').split(' ')

      # Keywords pré definidas
      keywords = ["char", "int", "void", "float", "double", "long", "short", "enum", "unsigned"]    

      # Listas
      strings = [n for n in formattedContent if n != '']

      # Identificadores
      identifiers = []

      # Palavras Reservadas
      reservedWords = []

      # Inteiros
      integers = []

      # Floats
      floats = []

      # Pré processadores
      preProcessors = []

      ### Verifica Inteiros ou Floats
      # Abertura do arquivo em leitura
      with open(untitledfile, "r") as file:
        # Para cada linha no arquivo
        for line in file:
          # Transforma a linha atual em uma lista de strings
            lineArr = line.lower().split()
            # Para cada string na linha atual, checa se é um inteiro ou float
            for string in lineArr:
              if (self.checkInt(string.replace(';', ''))):
                # Caso este não seja um valor de retorno (exemplo: return 0 ao final da execução de um programa)
                if lineArr[lineArr.index(string)-1] != 'return':
                  integers.append(int(string.replace(';', '')))
                  strings.remove(string)

              elif (self.checkFloat(string.replace(';', ''))):
                floats.append(float(string.replace(';', '')))
                strings.remove(string)

      ### Verifica Pré Processadores
      # Abertura do arquivo em leitura
      with open(untitledfile, "r") as file:
        # Para cada linha no arquivo
        for line in file:
          # Transforma a linha atual em uma lista de strings
            lineArr = line.lower().split()
            # Para cada string na linha atual
            for string in lineArr:
              # Se a string iniciar com #, é um pré processador
              if string.startswith('#'):
                # Adiciona à lista de pré processadores
                preProcessors.append(string)
                # Remove da lista de strings, pois não é uma string
                strings.remove(string)
      ### Verifica Identificadores
      # Abertura do arquivo em leitura
      with open(untitledfile, "r") as file:
        # Para cada linha no arquivo
        for linha in file:
          # Percorre cada key da lista de keywords
          for key in keywords:
            # Transforma a linha atual em uma lista de strings
            lineArr = linha.lower().split()
            # Verifica se alguma key da lista de keywords está presente na linha
            for string in lineArr:
              if key == string:
                # Caso o atual esteja na lista de keywords, mas o próximo não
                if (lineArr[lineArr.index(key)+1] not in keywords and lineArr[lineArr.index(key)-1] not in keywords):
                  # Adiciona à lista de identificadores removendo ; caso exista
                  tmp = lineArr[lineArr.index(key)+1].replace(';', '')
                  tmp = tmp.replace(',', '')
                  identifiers.append(tmp)
                  # Pega variaveis declaras na mesma linha (Ex: 'int a, b, c')
                  for element in lineArr:
                    tmp = lineArr[lineArr.index(element)].replace(';', '')
                    tmp = tmp.replace(',', '')
                    if tmp != '=' and tmp != ',' and tmp != '' and tmp not in identifiers:
                      tmp = lineArr[lineArr.index(element)].replace(';', '')
                      tmp = tmp.replace(',', '')
                      identifiers.append(tmp)
                    elif element == '=':
                      break
                      return

                  # strings.remove(key)
                  # TODO: VERIFICAR SE O PROXIMO ELEMENTO CONTÉM '=' e aí anotar o valor[indice do = + 1] em integer ou float
                # Caso seja um "unsigned int", por exemplo
                elif lineArr[lineArr.index(key)+1] in keywords:
                  # strings.remove(lineArr[lineArr.index(key)])
                  # strings.remove(lineArr[lineArr.index(key)+1])
                  identifiers.append(lineArr[lineArr.index(key)+2].replace(';', ''))
                  reservedWords.append((lineArr[lineArr.index(key)].replace(';', '') + ' ' + lineArr[lineArr.index(key)+1].replace(';', '')))

      for identifier in identifiers:
        if (identifier == '{'):
          identifiers.remove(identifiers[identifiers.index(identifier)])
        elif (identifier == '}'):
          identifiers.remove(identifiers[identifiers.index(identifier)])


      ### Verifica Funções como "printf" ou "scanf"
      # Abertura do arquivo em leitura
      with open(untitledfile, "r") as file:
        # Para cada linha no arquivo
        for line in file:
          # Transforma a linha atual em uma lista de strings
            lineArr = line.lower().split()
            # Para cada string na linha atual
            for string in lineArr:
              # A string pode ser uma função scanf ou printf
              if string == 'scanf' or string == 'printf':
                identifiers.append(string)
              # Caso haja problemas de escrita como printf() ao invés de printf (), por exemplo:
              elif str.__contains__(string, '('):
                temp = string.split('(')[0]
                if (temp == 'scanf' or temp == 'printf'):
                  # Adiciona à lista de identificadores
                  identifiers.append(temp)
                  # strings.remove(string)
                  # Remove da lista de strings, pois não é uma string


      # Verifica palavras reservadas através do AFD
      for string in strings:
        # Verifica se a string não é nula e é maior do que zero caracteres
        if (len(string) > 0 and string != '' and string != ' '):
          # A objeto da classe DFA recebe a string a ser tratada internamente
          dfa = DFA(string.lower())
          # Inicializa o tratamento chamando o estado inicial com estado = 0
          dfa.q0(string.lower(), 0)
          # O valor de retorno fica armazenado no campo valid. Caso este seja válido, retorna uma string, senão retorna 0
          if (dfa.valid != 0):
            # Se a palavra reservada não for repetida
            if (dfa.valid not in reservedWords):
              # Armazena na lista de palavras reservadas
              reservedWords.append(string.strip('\n'))
              # Remove da lista de strings, pois não é uma string
              strings.remove(string)

      newStrings = []
      for string in strings:
        if (string.replace(';', '') not in identifiers and not str.__contains__(string, "printf") and not str.__contains__(string, "scanf")):
          if (string not in keywords):
            if (string not in identifiers):
              if (string.replace(';', '') not in integers and string.replace(';', '') not in floats):
                newStrings.append(string)

      print ('\nInteiros: ', integers)
      print ('\nFloats: ', floats)
      print ('\nPalavras reservadas: ', reservedWords)
      print ('\nStrings: ', newStrings)
      print ('\nIdentificadores: ', identifiers)
      print ('\nPré Processadores: ', preProcessors)

    except Exception as e:
      messagebox.showerror("Exception",e)

  def checkInt(self, str):
    try:
      int(str)
      return True
    except ValueError:
      return False

  def checkFloat(self, str):
    try:
      float(str)
      return True
    except ValueError:
      return False



  # Defining Cut Funtion
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")

  # Defining Copy Funtion
  def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")

  # Defining Paste Funtion
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")

  # Defining Undo Funtion
  def undo(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # opening File in read mode
        infile = open(self.filename,"r")
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing File
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining About Funtion
  def infoabout(self):
    messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python.")

  # Defining shortcuts Funtion
  def shortcuts(self):
    # Binding Ctrl+n to newfile funtion
    self.txtarea.bind("<Control-n>",self.newfile)
    # Binding Ctrl+o to openfile funtion
    self.txtarea.bind("<Control-o>",self.openfile)
    # Binding Ctrl+s to savefile funtion
    self.txtarea.bind("<Control-s>",self.savefile)
    # Binding Ctrl+a to saveasfile funtion
    self.txtarea.bind("<Control-a>",self.saveasfile)
    # Binding Ctrl+e to exit funtion
    self.txtarea.bind("<Control-e>",self.exit)
    # Binding Ctrl+x to cut funtion
    self.txtarea.bind("<Control-x>",self.cut)
    # Binding Ctrl+c to copy funtion
    self.txtarea.bind("<Control-c>",self.copy)
    # Binding Ctrl+v to paste funtion
    self.txtarea.bind("<Control-v>",self.paste)
    # Binding Ctrl+u to undo funtion
    self.txtarea.bind("<Control-u>",self.undo)

    

# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()