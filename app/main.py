import subprocess
import os
import psycopg2

connection = psycopg2.connect(
    dbname=os.getenv("DB_NAME", "mydb"),
    user=os.getenv("DB_USER", "myuser"),
    password=os.getenv("DB_PASSWORD", "mypass"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432")
)


cursor = connection.cursor()

def Araçlar():
    cursor.execute("SELECT * FROM araçlar")

    dataset = cursor.fetchall()

    for data in dataset:
        print(data)

print("1. Araç ekle")
print("2. Araçları listele")
secim = input("Seçiminiz: ")

if secim == "1":
    
    model = input("Araba modeli giriniz: ")
    plaka = input("Plaka giriniz: ")
    tarih = input("Tarih giriniz: ")
    fiyat = input("Fiyat bilgisi giriniz: ")

    cursor.execute(
    "INSERT INTO araçlar (model, plaka, tarih, fiyat) VALUES (%s, %s, %s, %s)",
    (model, plaka, tarih, fiyat)
)
    print("Araç başarıyla kaydedildi.")
elif secim == "2":
    Araçlar();
    

connection.commit()

#subprocess.run(["docker", "compose", "up", "-d"])
#subprocess.run(["docker", "exec", "-it", "arackayt-docker_db_1", "psql", "-U", "myuser", "-d", "mydb"]) #my_postgres kısmı değişebilir ona 
#göre yeni isim gerekebilir şu an arackayt-docker_db_1


cursor.close()
connection.close()
