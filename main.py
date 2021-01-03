from epic import Value, Builder, Error

# İki değer oluşturmak
v1 = Value(1, error=0.05, symbol="x")
v2 = Value(-2, error=0.04, symbol="y")

# Builder ve Error objelerinin oluşturulması
b = Builder()
e = Error()

# cos(x)^e(y), denkleminin oluştutulması
f = b.cos(v1) ** b.exp(v2)

# Sonuç ve hatanın hesaplanması
print(e.propagate(f, (v1, v2)))
