def applyPromoCode(promoCode, amount):
    if promoCode == "FLAT50":
        return amount * 50//100
    elif promoCode == "FLAT30":
        return amount * 30//100
    else:
        return amount * 10//100

total1 = 1000
discount = applyPromoCode("FLAT30", total1)
print("Please pay: \u20b9",total1-discount)

total2 =  5000
discount = applyPromoCode("FLAT30", total2)
print("Please pay: \u20b9",total2-discount)