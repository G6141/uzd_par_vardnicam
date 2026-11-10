# Uzdevumā izmantot mainīgo - skirosana
# Datu kolonnu atšifrējumi:

# „0 : Papīrs” – ir nododams papīrs.
# „1 : Plastmasa” – ir nododama plastmasa.
# „2 : Stikls” – ir nododams stikls.
# „3 : Metāls” – ir nododams metāls.
# „4 : Bioloģiski noārdāmie atkritumi” – ir nododami bioloģiski noārdāmie atkritumi.
# „5 : Tekstilmateriāli” – ir nododami tekstilmateriāli.
# „6 : Elektriskās un elektroniskās iekārtas” – ir nododamas elektriskās un elektroniskās iekārtas.
# „7 : Apgaismes iekārtas un spuldzes” – ir nododamas apgaismes iekārtas un spuldzes.
# „8 : Baterijas un akumulatori” – ir nododamas baterijas un akumulatori.
# „9 : Sadzīvē radušies bīstamie atkritumi” – ir nododami sadzīvē radušies bīstamie atkritumi.
# „10 : Nolietotās riepas” – ir nododamas nolietotās riepas.
# Burts „x” norāda, ka konkrētajā punktā ir iespējas nodot attiecīgos atkritumus.

# Uzdevums
# Ja kādā no uzdevumiem datu nav, izvadīt paziņojumu: "ieraksta ar šādiem datiem nav"

# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot baterijas un akumulatorus.
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot nolietotās riepas.
# Izvadīt šos datus (pirmos 10 ierakstus) un šo vietu skaitu:
    - atkritumu nodošanas punkta adresi un novada nosaukumu, kurā var nodot metālu.

# Izvadīt novadu, kurā atrodas visvairāk atkritumu skirosanas punktu
      """
      Rēzeknes novada: 12
      1. Adrese 1
      2. Adrese 2
      """
# Izvadīt visu novadu skaitu, kuros atrodas vismaz viena katra veida šķirošanas iespēja
      """
      Visu veidu atkritumus var škirot xx novados
      """
      PIEMĒRAM:
      """
      {
          "_id": 2176,
          "pilsetanovads": "Preiļu novads",
          "adrese": "Brīvības iela 8, Prīkuļi, Saunas pag.",
          "map": "56.359293, 26.596843",
          "0 : Papīrs": "x",
          "1 : Plastmasa": "x",
          "2 : Stikls": "x",
          "3 : Metāls": "x",
          "4 : Bioloģiski noārdāmie atkritumi": "",
          "5 : Tekstilmateriāli": "",
          "6 : Elektriskās un elektroniskās iekārtas": "",
          "7 : Apgaismes iekārtas un spuldzes": "",
          "8 : Baterijas un akumulatori": "",
          "9 : Sadzīvē radušies bīstamie atkritumi": "",
          "10 : Nolietotās riepas": ""
      },
      {
          "_id": 2177,
          "pilsetanovads": "Priekules novads",
          "adrese": "Priekules daudzfunkcionālā sporta halle, Aizputes iela 1A, Priekule, Priekules nov.",
          "map": "56.438793, 21.579451",
          "0 : Papīrs": "x",
          "1 : Plastmasa": "",
          "2 : Stikls": "x",
          "3 : Metāls": "",
          "4 : Bioloģiski noārdāmie atkritumi": "",
          "5 : Tekstilmateriāli": "",
          "6 : Elektriskās un elektroniskās iekārtas": "",
          "7 : Apgaismes iekārtas un spuldzes": "",
          "8 : Baterijas un akumulatori": "x",
          "9 : Sadzīvē radušies bīstamie atkritumi": "x",
          "10 : Nolietotās riepas": ""
      },
      Nozīmē, ka var šķirot vismaz 6 veidu atkritumus
      """
