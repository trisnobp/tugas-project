Nama    : Trisno Bayu Pamungkas
NPM     : 2106702200
Kelas   : F
Asdos   : BYN

Link Heroku: lab1-assignment.herokuapp.com/mywatchlist/


Screenshot POSTMAN:

[![Screenshot-2022-09-22-075700.jpg](https://i.postimg.cc/c1hT5qJY/Screenshot-2022-09-22-075700.jpg)](https://postimg.cc/rzdSKPxF)

[![Screenshot-2022-09-22-075739.jpg](https://i.postimg.cc/kMLNHnm2/Screenshot-2022-09-22-075739.jpg)](https://postimg.cc/LhBZYFhS)

[![Screenshot-2022-09-22-075809.jpg](https://i.postimg.cc/4dDKWx9Z/Screenshot-2022-09-22-075809.jpg)](https://postimg.cc/vgvHBMhS)

1) Jelaskan perbedaan antara JSON, XML, dan HTML!

JSON: 

JSON digunakan untuk menyimpan data secara efisien, membaca, dan juga menukar informasi dari web server sehingga dapat dibaca pengguna. Data pada format JSON merupakan pasangan key-value dan dipisahkan oleh koma.


XML:

XML juga bisa digunakan untuk menyimpan data. Akan tetapi, format data pada XML jauh lebih terstruktur dibandingkan JSON, yang membuat data-nya mudah dibaca oleh manusia/mesin. Meskipun begitu, format XML kurang efisien dibandingkan JSON.


HTML:

HTML digunakan untuk menampilkan data dalam format teks yang bisa dimunculkan sebagai halaman web melalui web browser.


2) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dibutuhkan dalam pengimplementasian sebuah platform untuk mengirimkan data dari server sesuai dengan request dari client. Misal jika client meminta untuk ditampilkan halaman dalam format HTML, maka server akan mengembalikan file HTML untuk ditampilkan kepada client.


3) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Penjelasan tiap checklist:

1. Membuat aplikasi bernama mywatchlist pada direktori tugas lab dengan menuliskan python manage.py startapp mywatchlist.


2. Menambahkan aplikasi mywatchlist ke file settings.py pada project_django, lalu menambahkan path mywatchlist di urls.py pada project_django dan mengatur routing di urls.py pada mywatchlist agar aplikasi bisa diakses melalui http://localhost:8000/mywatchlist.


3. Membuat class MyWatchList di file models.py dengan atribut berupa watched, title, rating, release_date, dan review yang akan menjadi model data yang akan kita masukkan. Kemudian, untuk menambahkan data, dibuat folder fixtures dan file initial_mywatchlist_data.json yang berisi data-data film. Data-data tersebut nantinya akan diakses oleh objek MyWatchList.


4. Untuk menyajikan data dalam bentuk html, xml, dan json, diperlukan pengaturan pada file views.py pada mywatchlist. Pada file views.py, dibuat 3 fungsi untuk menampilkan data dalam bentuk html, xml, dan json. Untuk menampilkan data dalam bentuk HTML, kita memanfaatkan fungsi render untuk memetakan data ke file html. Untuk menampilkan data dalam bentuk XML dan JSON, kita memanfaatkan fungsi HttpResponse dan method serialize yang akan mengambil data dan menampilkannya dalam format XML/JSON.


5. Untuk menampilkan data menggunakan localhost, kita perlu menambahkan routing pada urls.py di mywatchlist untuk mengakses data dalam bentuk HTML, XML, dan JSON, yaitu:


path('html/', show_watchlist_html, name='show_watchlist_html'), // Untuk HTML

path('xml/', show_watchlist_xml, name='show_watchlist_xml'), // Untuk XML

path('json/', show_watchlist_json, name='show_watchlist_json') // Untuk JSON


6. Untuk deployment, add, commit, dan push terlebih dahulu aplikasi yang sudah dibuat ke repositori github. Setelah itu, .github/workflows akan secara otomatis berjalan untuk melakukan proses deployment ke Heroku.