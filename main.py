from stegano import lsb

secret = lsb.hide("./anonymous.png", "A"*500000)
secret.save("./anonymous-secret.png")
