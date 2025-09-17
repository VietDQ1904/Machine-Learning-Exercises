
PI = 3.141592653589793

# Tinh chu vi hinh tron
def getPerimeter(r):
    return 2 * PI * r

# Tinh dien tich hinh tron
def getArea(r):
    return PI * r * r

r = float(input("Nhap ban kinh hinh tron: "))
print(f"Chu vi hinh tron la: {getPerimeter(r)}")
print(f"Dien tich hinh tron la: {getArea(r)}")
