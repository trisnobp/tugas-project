Link aplikasi Heroku: https://lab1-assignment.herokuapp.com/katalog/

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
Jawaban:

[![Bagan-Framework-Django.jpg](https://i.postimg.cc/FzQMdBBb/Bagan-Framework-Django.jpg)](https://postimg.cc/WFXWxXjt)


2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawaban:
Penggunaan virtual environment ketika mengembangkan aplikasi Django bertujuan agar tidak terjadi konflik dependencies dari project yang sedang kita kembangkan dengan project yang lainnya. Meskipun begitu, mengembangkan projek Django tanpa virtual environment pada dasarnya bisa saja dilakukan, hanya saja lebih rentan untuk mengalami isu dalam pengembangannya (not the best practice).

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4?
Jawaban:
1) Poin 1
Pada file views.py yang berada di folder katalog, dilakukan import CatalogItem dari file models.py agar bisa mengambil data dan kemudian dibuat sebuah fungsi bernama show_katalog yang mengambil parameter request. 

Di dalam fungsi show_katalog tersebut, dibuat sebuah variabel bernama data_barang_catalog yang berisi seluruh data dari model dan kemudian dimasukkan ke dictionary context dengan key 'list_barang'. Saat dipanggil, fungsi akan me-return pemanggilan fungsi render yang mengambil parameter berupa request, nama file HTML, dan context. Pemanggilan fungsi render dilakukan agar data yang diambil dari model bisa dikembalikan ke dalam file HTML yang dituju.

2) Poin 2
Setelah itu, perlu dibuat sebuah routing agar page dari aplikasi kita bisa ditampilkan lewat browser melalui sebuah URL (Uniform Resource Locator). Untuk itu, perlu dilakukan modifikasi pada file urls.py di folder katalog dan di folder project_django. Pada urls.py di folder katalog, dilakukan import fungsi yang sudah didefinisikan di views.py dan dilakukan routing terhadap fungsi views tersebut. Setelah itu, aplikasi katalog perlu didaftarkan ke dalam urls.py di folder project_django, dengan memasukkannya ke variabel urlpatterns seperti berikut:

path('katalog/', include('katalog.urls'))

Potongan kode di atas berarti kita menambahkan rute untuk mengakses page katalog.

3) Poin 3
Proses pemetaan data ke dalam file HTML dilakukan dengan cara melakukan looping variabel list_barang yang sudah kita render sebelumnya ke HTML melalui fungsi show_katalog.
Untuk menampilkan data-datanya, kita menggunakan sintaks {{data}}.

4) Poin 4
Sebelum melakukan deployment, dilakukan git add, commit, dan push terlebih dahulu ke repositori github yang dituju. Setelah itu, kita perlu membuat aplikasi terlebih dahulu di Heroku, lalu simpan API Key Heroku dan nama aplikasi yang sudah kita buat. 

Setelah itu, kita perlu menambahkan repository secrets pada repository github berupa HEROKU_API_KEY dan HEROKU_APP_NAME yang berisi API key dan nama aplikasi yang tadi kita simpan untuk mengonfigurasi parameter yang dibutuhkan oleh workflow (pada file dpl.yml). Setelah workflow dijalankan, maka proses deployment akan tereksekusi dan aplikasi katalog yang sudah dibuat bisa dibuka melalui https://<nama-aplikasi-heroku>.herokuapp.com/katalog/


