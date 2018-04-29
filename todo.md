0.  Costruzione Database;

1.  Raccolta ID utenti in tutti i chunck recuperati, costruire un record con variabili ID_UTENTE, CONTEGGIO_ATTIVITÀ, CONTEGGIO_FOLLOWERS, CONTEGGIO_FOLLOWING per ogni utente recuperato;

2.  Ricavo statistiche sui tweets;

3.  Visualizzazione statistiche;

4.  Interrogazione di Twetter, controllo di quanti tra gli utenti seguiti dall'untente selezionato lo seguono, e, tra questi, quanti sono all'interno del nostro network (API.show_friendship());

	- Friendship requests:
   In order to build the network of the authors of tweets we need the friendship status of each possible couple. The number of possible link to check is quadratic: n(n-1)/2. 
   We have 180 requests for each 15 minutes time window. 
   In friendship_request.py there are some computation about it.



- n - 1  Analisi del network ottenuto;

- n - Applicazione dei pesi selezionati;


