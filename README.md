# Function Calling med OpenAI  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-under_development-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

Dette prosjektet er en chatbot som hovedsakelig fokuserer på **function calling**.  
Chatboten tilbyr tre ulike funksjonskall i tillegg til vanlig kommunikasjon.  
Den er koblet opp mot to forskjellige OpenAI-endepunkter: *completions* og *responses*.  

⚠️ Prosjektet er fortsatt under utvikling, så feil kan forekomme.  

---

## 📖 Innholdsfortegnelse
- [Om prosjektet](#-om-prosjektet)  
- [Om funksjonskall](#-om-funksjonskall)  
- [Mine funksjonskall](#-mine-funksjonskall)  
- [Prosjektstruktur](#-prosjektstruktur)  
- [Sikkerhet og personvern](#-sikkerhet-og-personvern)  
- [Installasjon og oppsett](#-installasjon-og-oppsett)  

---

## 📌 Om prosjektet  
Dette er et Python-prosjekt som implementerer en chatbot basert på OpenAI sin språkmodell og **function calling**.  

Prosjektet er ment som en utforskning av funksjonskall og *responses*-endepunktet til OpenAI.  
Det er koblet opp mot to forskjellige OpenAI-endepunkter for å undersøke hva som er nytt og forskjellig mellom dem.  

---

## ⚙️ Om funksjonskall  
Funksjonskall er et kraftig verktøy i OpenAI-modeller.  
Selv om språkmodeller er trent på store mengder data, kan man med funksjonskall hente inn oppdatert eller spesialisert informasjon som ikke finnes i treningsdataen.  

Dette gir større fleksibilitet og gjør det mulig å skreddersy chatboten til spesifikke behov.  

---

## 🧩 Mine funksjonskall  
Jeg har valgt tre ulike funksjonskall for å eksperimentere med mulighetene rundt function calling:  

1. **Datetime (Python-bibliotek)**  
   - En enkel start for å forstå hvordan funksjonskall fungerer i praksis.  

2. **Chuck Norris API**  
   - For å koble chatboten mot et eksternt API og teste hvordan den håndterer ekstern data.  

3. **Useless Facts API**  
   - Et nytt API for videre trening i å integrere eksterne kilder med funksjonskall.  

---

## 📂 Prosjektstruktur  
Prosjektstrukturen er bevisst holdt enkel, ettersom dette er et lite og utforskende prosjekt.  

---

## 🔒 Sikkerhet og personvern  
Dette prosjektet samler **ikke** inn personopplysninger for bruk av selve programmet.  

⚠️ **Viktig:**  
Chatboten bruker OpenAI sin språkmodell.  
**Ikke del sensitiv eller personlig informasjon** om deg selv eller andre når du tester prosjektet.  

---

## 🚀 Installasjon og oppsett  

### Forutsetninger
For å kjøre prosjektet trenger du følgende:  

- En **API-nøkkel fra OpenAI**  
- Et Python-miljø med OpenAI-biblioteket installert  
- `python-dotenv` for miljøvariabler  
- Følgende Python-biblioteker:  
  - `datetime` (innebygget i Python)  
  - `os` (innebygget i Python)  
  - `sys` (innebygget i Python)  
  - `json` (innebygget i Python)  
  - `requests`  

### Kloning av repo
Klon prosjektet lokalt med:  

```bash
git clone https://github.com/SondreHaugom/Labs-Responses
