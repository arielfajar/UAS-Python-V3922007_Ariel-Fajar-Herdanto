#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import csv

# menyimpan link web bukalapak  yang akan discrape ke variabel 
web_url = 'https://www.bukalapak.com/c/g-handphone/hp-smartphone-6004?page='


data = []  # List kosong untuk menyimpan data produk

# Melakukan perulangan untuk scraping pada halaman 2 hingga 6
for page in range(2, 7): 
    url = web_url + str(page)  # Membuat URL halaman yang akan discraping
    req = requests.get(url)  # Mengirim permintaan HTTP GET ke URL bukalapak
    soup = BeautifulSoup(req.text, 'html.parser')  # Membuat objek BeautifulSoup dari untuk memparse konten HTML
    product_items = soup.find_all('div', {'class': 'bl-product-card'})  # Mencari semua elemen dengan tag div dan class tersebut di variabel product_items
    
    # melakukan perulangan untuk mengambil masing2 item yng telah dicari di variabel product_items
    for item in product_items:
        # Mengambil nama, alamat, harga, dan rating produk dari elemen-elemen yang ditemukan
        name = item.find('a', {'class': 'bl-link'}).text.strip() # Mencari semua elemen dengan tag a dan class 'bl-link' di variabel name
        address = item.find('span', {'class': 'mr-4 bl-product-card__location bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1'}).text.strip() # Mencari semua elemen dengan tag span dan class tersebut di variabel address
        price = item.find('p', {'class': 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1'}).text.strip() # Mencari semua elemen dengan tag p dan class tersebut di variabel price
        rating = item.find('p', {'class': 'bl-text bl-text--body-14 bl-text--subdued'}).text.strip() # Mencari semua elemen dengan tag p dan class tersebut di variabel rating
        data.append([name, address, price, rating])  # Menyimpan data dalam list data

# Membuat file CSV untuk menyimpan data
csv_file = 'data_smartphone.csv'  

with open(csv_file, 'w', newline='', encoding='utf-8') as file: # Membuka file csv_file dengan mode write ('w') untuk menulis data
    writer = csv.writer(file) # Membuat objek writer dari modul CSV untuk menulis data ke dalam file.
    writer.writerow(['Name', 'Address', 'Price', 'Rating'])  # Menulis header kolom
    writer.writerows(data)  # Menambahkan data ke dalam file CSV


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

# membaca file CSV menjadi DataFrame
data = pd.read_csv('data_smartphone.csv')

# Bar chart
plt.figure(figsize=(10, 6)) # mengatur ukuran gambar 10x6 inci menggunakan modul Matplotlib.
data['Address'].value_counts().plot(kind='bar') # Menghitung jumlah kemunculan tiap nilai dalam kolom 'Address'
plt.xlabel('Address') # melabeli sumbu x dengan teks 'Address'.
plt.ylabel('Count') # melabeli sumbu y dengan teks 'Count'.
plt.title('Bar Chart Smartphone') # membust judul grafik dengan teks .
plt.savefig('bar_chart.jpg') # Menyimpan chart dalam format JPG dengan nama file 'bar_chart.jpg'.
plt.show() # menampilkan chart


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# Membaca file CSV
data = pd.read_csv("data_smartphone.csv")

# Menghitung jumlah kemunculan tiap nilai dalam kolom 'Address'
plt.hist(data['Address'])

# Menambahkan judul
plt.title("Histogram Smartphone Berdasarkan Alamat")

# Menyimpan Histogram dalam format JPG dengan nama file 'histogram.jpg'
plt.savefig('histogram.jpg', dpi=300, bbox_inches='tight')

# Menampilkan Histogram
plt.show()


# In[ ]:




