#import subprocess
import os
import psycopg2
#bağlantı zamanı kontrolü lazım ilk sefer bağlandığımda bazen database bağlanmamış olabiliyor.
connection = psycopg2.connect(
    dbname=os.getenv("DB_NAME", "mydb"),
    user=os.getenv("DB_USER", "myuser"),
    password=os.getenv("DB_PASSWORD", "mypass"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432")
)
#çalıştırmak için ilk önce docker-compose up --build
#eğer hata verirse geçmişten kalan bozuk konteynırlardan dolayı olur docker-compose down kullan eğer verileri silmek istersen --volumes ekle
#docker-compose run app

cursor = connection.cursor()

def Araçlar():
    cursor.execute("SELECT * FROM araçlar")

    dataset = cursor.fetchall()

    for data in dataset:
        print(data)

def menu():

    print("1. Araç ekle")
    print("2. Araç silme")
    print("3. Araç arama")
    print("4. Araçları listele")
    print("5. Programı kapat")

while True:
    
    menu()

    secim = input("Seçiminiz: ")

    if secim == "1":
    
        model = input("Araba modeli giriniz: ")
        plaka = input("Plaka giriniz: ")
        tarih = input("Tarih giriniz: ")
        fiyat = input("Fiyat bilgisi giriniz: ")

        cursor.execute(
        "INSERT INTO araçlar (model, plaka, tarih, fiyat) VALUES (%s, %s, %s, %s)",
        (model, plaka.upper(), tarih, fiyat)
    )
        print("Araç başarıyla kaydedildi.")

    elif secim == "2":

        arananPlaka = input("Silmek istediğiniz aracın Plakası: ").upper()

        cursor.execute("DELETE FROM araçlar WHERE plaka = %s", ((arananPlaka,)))

        print("İstenilen araç silindi")

    elif secim == "3":

        arananPlaka = input("Aradığınız plakayı giriniz: ").upper()

        cursor.execute("SELECT * FROM araçlar WHERE plaka = %s", (arananPlaka,)) # "=" işareti eklendi arananPllaka dan sonra "","" eklendi tuple olarak algılaması gerkiyor sql 

        for row in cursor.fetchall():
        
            print(f"Aranan araba: \n {row}")
        

    elif secim == "4":

        Araçlar();
    
    elif secim == "5":

        print("Programdan çıkılıyor...")
        
        break

    else:

        print("geçersiz seçim")

connection.commit()

#subprocess.run(["docker", "compose", "up", "-d"])
#subprocess.run(["docker", "exec", "-it", "arackayt-docker_db_1", "psql", "-U", "myuser", "-d", "mydb"]) #my_postgres kısmı değişebilir ona 
#göre yeni isim gerekebilir şu an arackayt-docker_db_1

cursor.close()
connection.close()
