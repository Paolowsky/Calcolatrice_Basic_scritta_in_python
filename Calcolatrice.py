while True: #il ciclo while sarà sempre vero 
    print('''
    Benvenuto nella mia calcolatrice.
    Creata da Zio.P,
    Ecco un elenco delle verie funzioni disponibili:

    -Per effettuare un'addizione. seleziona 1;
    -Per effettuare una sottrazione, seleziona 2;
    -Per effettuare una moltiplicazione, seleziona 3;
    -Per effettuare una divisione, seleziona 4;
    -Per effettuare un calcolo esponenziale, seleziona 5;

    -Per uscire dal programma puoi digitare ESC;
    ''')
    scelta = input('inserisci il numero all\'azione desiderata ---> ') #diamo la possibilità all'utente di scegliere la funzione tramite input

    if scelta == '1': 
        print('\nHai scelto: Addizione\n')
        a = float (input('Inserisci il primo numero -> '))
        b = float (input('Inserisci il secondo numero -> '))
        print('IL risultato della somma è: ' + str(a + b))
    elif scelta == '2':
        print('\nHai scelto: Sottrazione\n')
        a = float (input('Inserisci il primo numero -> '))
        b = float (input('Inserisci il secondo numero -> '))
        print('IL risultato della sottrazione è: ' + str(a - b))
    elif scelta == '3':
        print('\nHai scelto: Moltiplicazione\n')
        a = float (input('Inserisci il primo numero -> '))
        b = float (input('Inserisci il secondo numero -> '))
        print('IL risultato della moltoplicazione è: ' + str(a * b))
    elif scelta == '4':
        print('\nHai scelto: Divisione\n')
        a = float (input('Inserisci il primo numero -> '))
        b = float (input('Inserisci il secondo numero -> '))
        print('IL risultato della divisione è: ' + str(a / b))
    elif scelta == '5':
        print('\nHai scelto: Calcolo esponenziale\n')
        a = float (input('Inserisci il primo numero -> '))
        b = float (input('Inserisci il secondo numero -> '))
        print('IL risultato del calcolo esponenziale è: ' + str(a ** b))
    elif scelta == "ESC" or scelta == "esc":
        print('''L'applicazione varrà ora chiusa.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break #interrompe il ciclo se l'utente digita esc
    loop = input("\nDesidera continuare ad usare l\'applacazione? S/N")
    if loop == 'S' or loop =='s': #cosi non cambia se  l'utente inserisce la lettere minuscola o maiuscola
        print('''Torno al menù principale.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue #salta il ciclo per riinziare il loop dall'inizio 
    else:
         print('''Addio.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
         break
# tutti gli \n servono per dare spazio/andare accapo 
