# BDRetro (La Bottega del Retrogaming) - E-commerce

Questo file README fornisce una panoramica del progetto 
"La Bottega del Retrogaming" (che per semplicità verrà anche 
chiamata BDRetro), un'applicazione web di e-commerce sviluppata con Django.

## Credenziali di Django

Per accedere al sito, usare il bottone di Login in alto a destra.
Queste sono le credenziali predefinite per l'accesso come amministratore:

* **Username:** admin
* **Password:** supermanager

E' fornito anche un profilo di cliente predefinito, senza privilegi di 
amministratore:

* **Username:** customer
* **Password:** shopping99

## Panoramica del Progetto

BDRetro è un negozio online specializzato nella vendita di prodotti 
legati al retrogaming, sia fisici che digitali. 
Gli utenti possono sfogliare un catalogo di prodotti, 
aggiungerli al carrello e completare acquisti. 
Il progetto è stato costruito utilizzando Django, Python, 
HTML, CSS e Javascript.

## Funzionalità

### Registrazione e Login Utente

* **Registrazione**: I nuovi utenti possono creare un account fornendo un nome utente, un indirizzo email e una password.
* **Login**: Gli utenti registrati possono accedere al proprio account con nome utente e password, per effettuare ordini ed eventualmente fornire indirizzi di spedizione per i loro ordini.

### Utilizzo del sito: Clienti

Una volta effettuato l'accesso (o come ospite), gli utenti possono sfogliare
i prodotti disponibili nel negozio e aggiungerli al carrello.

Se lo desidera, l'utente può visualizzare i dettagli di un prodotto e leggerne
una breve descrizione.

Una volta fatto l'accesso al carrello, sono visibili il numero di prodotti
selezionati e il prezzo totale del carrello. Gli utenti possono modificare
la quantità di prodotti nel carrello, rimuovere prodotti (portandone la
quantità da 1 a 0), o procedere al checkout.

La pagina di checkout richiede agli utenti di fornire un indirizzo di spedizione
(non necessario per i prodotti digitali) e, se non sono già registrati, di inserire i dati
necessari per la creazione automatica dell'account. Una volta completato il checkout,
tutte le informazioni relative all'ordine vengono salvate nel database e l'utente viene riportato
alla pagina principale del sito, dove può continuare a sfogliare i prodotti.

E' possibile tornare allo store in qualsiasi momento
cliccando sul logo "La Bottega del Retrogaming" nella barra di navigazione.

### Utilizzo del sito: Amministratori

Gli amministratori del sito, oltre ad avere gli stessi permessi dei clienti,
hanno accesso alla Vista Amministratore del sito, che consente loro di gestire
gli ordini, i prodotti e gli indirizzi degli utenti SENZA dover accedere alla
pagina di amministrazione di Django.

Si possono modificare i parametri
degli elementi, cancellarli o crearne di nuovi; per invece modificare, aggiungere o eliminare utenti, 
è possibile utilizzare il pannello di amministrazione di Django aggiungendo
/admin al link del sito, dopo aver fatto il login come amministratore.

### Filtraggio prodotti

Nella pagina dello store, è possibile filtrare i prodotti in base a:

* **Ordinamento**: 
per ID (default, in ordine di inserimento nel database), nome (A-Z, Z-A) o prezzo (crescente, decrescente).
* **Tipo**: per prodotti digitali, fisici, o entrambi.

### Logout

Gli utenti autenticati possono disconnettersi dal proprio account 
tramite il pulsante di Logout presente nella barra di navigazione.
