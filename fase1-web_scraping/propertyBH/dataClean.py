import re

class clean:
    
    def price(price):
        regex = r"[^R$]*$"
        price = re.findall(regex, price)
        price = price[0].replace(".", "")
        price = re.findall(r'\d+', price)
        return float(price[0])
    
    def suite(suite):
        if suite == "sem suíte":
            return 0
        else:
            suite = re.findall(r'\d+', suite)
            return int(suite[0])
    
    def neighborhoods(neighborhood):
        neighborhood = neighborhood.split(': ')
        return neighborhood[1]
    
    def general(general):
        general = re.findall(r'\d+', general)
        return int(general[0])