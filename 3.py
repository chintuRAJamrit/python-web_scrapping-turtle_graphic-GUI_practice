#Define a dictionary called agencies that stores a mapping of acronyms CBI, FBI, NIA, SSB,WPA (the keys) to Indian government agencies ‘Centrak Bureau of Investigation’,
#‘ForeignDirect Investment’, ‘National Investion Agency’, ‘Service Selection Board’, and ‘Works ProgressAdministration’(the values) created by Prime Minister during the New Deal. Then:
#• Add the map of acronym BSE ‘Bombay Stock Exchange’.
#• Change the value of the key SSB to ‘Social Security Administration’.
#• Remove the (key value) pairs with keys CBI and WPA.

agencies = {"CBI":"Centrak Bureau of Investigation","FBI":"Foreign Direct Investment","NIA":"National Investion Agency", "SSB":"Service Selection Board" , "WPA": "Works ProgressAdministration"}

print(type(agencies))
agencies["BSE"] = "Bombay Stock Exchange"
agencies.update({"SSB":"Social Security Administration"})
agencies.pop("WPA")
del agencies["CBI"]
print(agencies)


