
# export records webpublicatie = 'Europeana' uit adlib naar csv
# zet csv om naar dataframe

import pandas as pd
# pip install pandas in terminal

df = pd.read_csv(r"C:\Users\teugelso\PycharmProjects\pythonProject\TraintheTrainer_03\ttt3.csv", delimiter=';')
print(df)

# read kolomnamen
#print(df.columns)

# read 1 kolom
#print(df['objectnaam'][0:5])

# read meerdere kolommen
#print(df[['objectnaam', 'vervaardiger']])

# read 1 of meer rij(en)
#print(df.iloc[1:4])

# read een specifieke locatie
#print(df.iloc[1,1])

# om dataframe te bekijken, laat bovenstaande lopen in python console ipv terminal en klik op 'view as dataframe'

#######################################################################################################################

# transformaties van de dataframe

# 1. wijzigen kolomnaam

df = df.rename(columns={"instelling.naam": "instellingsnaam", "vervaardiging.plaats": "plaats vervaardiging"})
print(df)

#######################################################################################################################

# 2. delete kolom

df2 = df.drop(["objectnummer", 'instellingsnaam'], 1)
print(df2)

#######################################################################################################################

# 3. toevoegen kolom

df['Test'] = df['objectnummer'] + df['instellingsnaam']
print(df)

#######################################################################################################################

# 4. verplaats kolom

#df = df[['instellingsnaam', 'objectnummer', 'Test', 'object_categorie', 'objectnaam', 'titel', 'beschrijving',
         'vervaardiger', 'vervaardiger.rol', 'plaats vervaardiging', 'vervaardiging.datum.begin.prec',
         'vervaardiging.datum.begin', 'vervaardiging.datum.eind.prec', 'vervaardiging.datum.eind',
         'associatie.onderwerp', 'associatie.persoon', 'associatie.periode', 'inhoud.onderwerp', 'inhoud.persoon.naam']]

cols = list(df.columns.values)
#print(cols)
#df = df[cols[0:1] + [cols[-1]] + cols[2:19]]
print(df)

#######################################################################################################################

# 5. alfabetisch/numeriek sorteren

df = df.sort_values('objectnaam', #ascending=False)
print(df)

#df5 = df.sort_values(['vervaardiger', 'objectnaam'], ascending=[1,0])
#print(df5)

#df6 = df.sort_values('objectnummer')
#print(df6)

#######################################################################################################################

# 6. filteren

df3 = df.loc[df['plaats vervaardiging'] == 'Gent']
print(df3)

#######################################################################################################################

# 7. filteren op meerdere condities

df4 = df.loc[(df['plaats vervaardiging'] == 'Gent') & (df['vervaardiger.rol'] == 'ontwerper')]
print(df4)

#######################################################################################################################

# 8. csv opslaan

df4.to_csv('Gentseontwerpers.csv')

#######################################################################################################################

# 9. waarden tellen

# 9.1 aantal records
aantal_records = df["objectnummer"].count()
print(aantal_records)

#######################################################################################################################

# 9.2 tellen van het aantal records met een beschrijving
beschrijving = df["beschrijving"].count()
print(beschrijving)

#######################################################################################################################

# 9.3 aantal records vervaardigd in Gent
# filteren op waarde die je wil tellen
filterplaatsGent = df.loc[df['plaats vervaardiging'] == 'Gent']

# tellen aantal keer waarden voorkomt in kolom
records_vervaardigdinGent = filterplaatsGent['plaats vervaardiging'].count()
print(records_vervaardigdinGent)

#######################################################################################################################

# visualiseren met matplotlib

from matplotlib import pyplot as plt
# pip install matplotlib

# 1. aantal records vervaardigd in Gent
vervaardigingGent = [aantal_records-records_vervaardigdinGent, records_vervaardigdinGent]
plt.pie(vervaardigingGent)
plt.show()

#######################################################################################################################

# 2. voorbeeld van barchart met ontbrekende velden

vervaardiger = df["vervaardiger"].count()
vervaardiger_rol = df["vervaardiger.rol"].count()
vervaardiging_plaats = df["plaats vervaardiging"].count()
vervaardiging_datumbegin = df["vervaardiging.datum.begin"].count()
vervaardiging_datumeind = df["vervaardiging.datum.eind"].count()
associatie_onderwerp = df["associatie.onderwerp"].count()

velden = ["vervaardiger", "rol vervaardiger", "plaats vervaardiging", "datum vervaardiging begin",
          "datum vervaardiging eind", "associatie onderwerp"]
aanwezig = [vervaardiger, vervaardiger_rol, vervaardiging_plaats, vervaardiging_datumbegin, vervaardiging_datumeind,
            associatie_onderwerp]
afwezig = [aantal_records-vervaardiger, aantal_records-vervaardiger_rol, aantal_records-vervaardiging_plaats,
           aantal_records-vervaardiging_datumbegin, aantal_records-vervaardiging_datumeind,
           aantal_records-associatie_onderwerp]

plt.bar(velden, aanwezig)
plt.bar(velden, afwezig, bottom=aanwezig)
plt.show()

#######################################################################################################################

# brainstorm project cogent datavisualisatie
#    - gemeenschappelijke grafieken (inclusief thesaurus & personen/instellingen)
#    - grafieken per instelling
