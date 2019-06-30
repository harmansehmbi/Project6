def applyPromoCode(promoCode, amount):
    if promoCode == "FLAT50":
        return amount * 50//100
    elif promoCode == "FLAT30":
        return amount * 30//100
    else:
        return amount * 10//100

total = 1000
discount = applyPromoCode("FLAT30", total)
print("Please pay: \u20b9",total-discount)

print("Please pay: \u20b9",total-applyPromoCode("FLAT30", total))

print("applyPromoCode is:",applyPromoCode)

# Reference Copy !!
fun = applyPromoCode

print("fun is:",fun)

print("Please pay: \u20b9",total-fun("FLAT50", total))

del applyPromoCode
print("Please pay: \u20b9",total-applyPromoCode("FLAT30", total))

# gives an error because applyPromoCode is deleted