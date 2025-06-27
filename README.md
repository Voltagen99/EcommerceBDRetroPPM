# BDRetro (La Bottega del Retrogaming) - E-commerce

Questo file README fornisce una panoramica del progetto La Bottega del Retrogaming (che per semplicità verrà anche chiamata BDRetro), un'applicazione web di e-commerce sviluppata con Django.

## Credenziali di Django Administration (/admin)

Per accedere al pannello di amministrazione di Django, naviga su `/admin` e utilizza le seguenti credenziali:

* **Username:** admin
* **Password:** supermanager

## Panoramica del Progetto

BDRetro è un negozio online specializzato nella vendita di prodotti legati al retrogaming. Gli utenti possono sfogliare un catalogo di prodotti, aggiungerli al carrello e completare acquisti. Il progetto è stato costruito utilizzando Django, Python, HTML, CSS e JavaScript.

## Funzionalità

### Registrazione e Login Utente

* **Registrazione**: I nuovi utenti possono creare un account fornendo un nome utente, un indirizzo email e una password.
* **Login**: Gli utenti registrati possono accedere al proprio account con nome utente e password, per effettuare ordini ed eventualmente fornire indirizzi di spedizione per i loro ordini.

### Utilizzo del sito

Una volta effettuato l'accesso (o come ospite), gli utenti possono:

* Visualizzare il catalogo dei prodotti nella pagina principale.
* Aggiungere e rimuovere prodotti dal carrello.
* Procedere al checkout per completare l'acquisto.
* Gli utenti non registrati possono comunque effettuare acquisti; un account verrà creato per loro durante il processo di checkout.

### Aggiunta nuovi prodotti (solo per gli amministratori)

L'amministratore del sito può aggiungere nuovi prodotti al catalogo attraverso il pannello di amministrazione di Django. È possibile specificare nome, prezzo, se il prodotto è digitale, e caricare un'immagine assegnata a quello specifico prodotto.

### Filtraggio prodotti

Nella pagina dello store, è possibile filtrare i prodotti in base a:

* **Ordinamento**: per ID (default, in ordine di inserimento nel database), nome (A-Z, Z-A) o prezzo (crescente, decrescente).
* **Tipo**: per prodotti digitali, fisici, o entrambi.

### Logout

Gli utenti autenticati possono disconnettersi dal proprio account tramite il pulsante di logout presente nella barra di navigazione.
