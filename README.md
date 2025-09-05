Velkommen til Labs-Responses!

Dette prosjektet er laget mest for utforskning og testing av Function Calling og respons-API-et til OpenAI. Prosjektet er satt opp slik at du kan snakke med chatbotten som en vanlig chatbot, men ved et visst ord vil den kalle på en funksjon som kun kjører når den blir aktivert. Function Calling er en veldig fleksibel og kraftig måte for OpenAI-modeller å samhandle med eksterne systemer på, samt få tilgang til data utenfor treningsdataene deres.

Funksjonalitet i dette prosjektet:

Bruke chatbotten som en vanlig chatbot

Kalle på en funksjon dersom aktiveringsordet brukes

Samtalehistorikk

Personvern

All samtale du har med chatbotten blir lagret i en conversationHistory-array så lenge programmet kjører. Dersom du starter en ny samtale eller restarter programmet, vil ingen meldinger eller informasjon bli lagret videre. Dette betyr at informasjonen du sender inn ikke blir tatt vare på etter endt økt. Chatbotten vil kunne huske samtalen underveis, men ikke i etterkant.

Når Function Calling brukes i dette programmet, hentes kun dagens dato ut via datetime-biblioteket i Python. Ingen data fra brukeren sendes eller lagres i dette endepunktet.

Med andre ord: ingen data eller informasjon fra brukeren er nødvendig eller blir lagret for å kjøre dette programmet.

Nedlasting av programmet

For å laste ned og teste ut dette programmet, kjør følgende kommando:

git clone https://github.com/SondreHaugom/Labs-Responses

