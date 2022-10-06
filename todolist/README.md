Nama        : Trisno Bayu Pamungkas

NPM         : 2106702200

Kelas       : PBP-F

Asdos       : BYN


# Tugas 4

1) Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF atau Cross-Site Request Forgery merupakan serangan yang membuat client tanpa sadar mengirimkan tanpa sadar mengirimkan request ke suatu website melalui website yang sedang diakses. Yang berarti, terdapat serangkaian tindakan terjadi yang dilakukan aplikasi dan tidak dikehendaki oleh client, dan mengancam keamanan informasi client. Misalnya, melalui CSRF yang dilakukan melalui url, jika client meng-kliknya, maka penyerang bisa melakukan perintah apapun yang dia mau, bisa saja seperti mengganti password client dan sebagainya. Oleh karena itu, untuk mencegah kerusakan dan kerugian oleh serangan ini, dibuat sebuah token bernama csrf_token, yang gunanya untuk melakukan validasi request pada server-side, di mana penyerang tidak akan mungking melakukan permintaan HTTP yang valid dan cocok untuk diberikan ke korban.


2) Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Penggunaan generator pada pembuatan elemen <form> membuat kita tidak perlu menuliskan sintaks-sintaks html untuk sebuah form secara manual. Akan tetapi, jika kita ingin membuat elemen <form> secara manual, hal tersebut juga bisa dilakukan dengan menuliskan sendiri atribut-atribut dari forms pada file HTML, seperti label, input, dan sebagainya.

Sebagai contoh, kita bisa lihat pada file login.html:

# Contoh Kode
   
   [![carbon.png](https://i.postimg.cc/054hJTsC/carbon.png)](https://postimg.cc/nMv3ywMs)
  
Potongan kode HTML di atas adalah cara membuat form secara manual, yaitu mengisi form dengan table, input, dan lainnya.


3) Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Pertama-tama, saat user ingin menambah task baru, user akan diminta memasukkan data judul task dan deskripsi task pada HTML form yang di-generate melalui forms.py. Setelah user memasukkan data-data dan klik submit, maka serangkaian proses akan dijalankan pada fungsi di views.py yang mengh-handle pembuatan task. Proses yang akan terjadi adalah melakukan validasi terhadap fiels pada form, jika mengandung data yang valid, akan dibuat instance Task() dari model, lalu kita assign tiap atribut dengan data dari form. Setelah itu, kita panggil method save pada instance tersebut untuk menyimpannya ke database. 
  
Untuk memunculkan data pada template HTML, kita atur fungsi pada views.py yang akan menampilkan data pada halaman to-do-list. Di dalamnya, kita ambil data yang ada di database namun di-filter berdasarkan user yang sedang login. Dengan demikian, kita hanya mengakses data yang terikat dengan user tersebut. Kemudian kita petakan data-data tersebut pada file HTML yang akan ditunjukkan pada user.


4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat model Task
   
Pada file models.py kita buat class Task dengan atribut berupa user, title, date (terisi secara otomatis), dan description. Atribut user berguna untuk memetakan user yang login dengan data yang dimilikinya.
  
- Implementasi Login, Logout, dan Register
   
Untuk implementasi register, kita buat fungsi pada views.py untuk memproses dan menampilkan HTML forms pada user. Pada fungsi ini, akan dibuat sebuah form dengan menginisiasi object UserCreationForm dengan parameter request.POST untuk membuat form registrasi secara otomatis, lalu dilakukan validasi. Jika valid, maka data pada form akan di-save pada database dan kembali ke halaman login. 

   
Untuk login, kita buat form secara manual pada file login.html. Kemudian dibuat fungi views.py untuk memproses dan menampilkan file HTML pada user. Proses yang dilakukan apda fungsi login adalah mengauthentikasi username dan password yang dimasukkan user untuk mengecek apakah akun terdaftar. Jika valid, maka proses login akan berjalan, tetapi jika tidak, maka akan menampilkan suatu info message kepada user.

   
Untuk logout, pada fungsi views.py yang meng-handle logout, kita panggil fungsi logout dengan parameter request dan melakukan redirect ke halaman login.
  
- Membuat halaman utama to-do-list
   
Untuk membuat halaman utama to-do-list, kita buat halaman html untuk menampilkan to-do-list kepada user. Kemudian pada fungsi show_todolist pada views.py, kita ambil data yang ada pada database berdasarkan user yang sedang login, kemudian dilakukan serangkaian proses untuk memetakan data pada file HTML yang dibuat.

- Membuat halaman pembuatan task
   
Untuk membuat halaman pembuatan task, dibuat sebuah form dengan file forms.py. Form ini akan mengambil data berupa title dan description yang di-input oleh user. Nantinya, pada fungsi create_task pada views.py, data dari forms akan diambil melalui request.POST.get() dan di-assign pada atribute object Task yang dibuat, kemudian object Task tersebut disimpan ke database.
 
- Membuat routing
   
Untuk routing, kita hanya perlu menambahkan path pada file urls.py di folder todolist agar fungsi-fungsi yang dibuat dapat diakses melalui route yang kita definisikan.


# Tugas 5
1) Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Inline CSS: 

Menggunakan CSS langsung pada tag HTML tertentu, yaitu dengan menambahkan style pada tag. Inline CSS akan sangat berguna jika kita tidak menggunakan banyak properti style pada suatu tag, sehingga kita tidak perlu membuat file CSS. Akan tetapi, kekurangannya adalah kita jadi perlu menuliskan property style pada semua tag yang perlu menggunakan CSS, di mana hal tersebut tidak efisien, apalagi jika terdapat beberapa tag yang menggunakan property style yang sama.


Internal CSS:

Internal CSS berarti kita meletakkan tag style di dalam tag head pada HTML. Style CSS yang dipasang dengan metode ini akan di-download setiap halaman dipanggil. Keuntungannya adalah kita tidak perlu menguoload beberapa file karena HTML dan CSS bisa digunakan di file yang sama. Akan tetapi, penggunaan Internal CSS akan meningkatkan waktu akses website dan tidak efisien apabila kita akan menggunakan CSS yang sama pada beberapa file HTML,


External CSS:

External CSS berarti kita membuat suatu file CSS pada suatu folder secara terpisah yang berisi rule-rule styling. Untuk menggunakannya, kita hanya perlu me-load file tersebut ke dalam file html yang akan menggunakan CSS. Salah satu keuntungan dari menggunakan External CSS adalah kita bisa menggunakan file CSS yang sama di banyak file html dan struktur HTML bisa menjadi lebih rapih. Akan tetapi, kekurangan dari external CSS adalah halaman html tidak akan tampil dengan sampai file CSS selesai dipanggil.

2) Jelaskan tag HTML5 yang kamu ketahui.

5 tag HTML5 yang biasa digunakan:

- <a>: Untuk menaruh suatu link
- <body>: Mendefinisikan body dari dokumen HTML
- <button>: Untuk membuat suatu tombol
- <div>: Membuat suatu division atau section pada dokumen HTML
- <li>: Untuk membuat list item


3) Jelaskan tipe-tipe CSS selector yang kamu ketahui.

- element: Memilih semua elemen <tag> 
- # id: Memilih elemen pada CSS dengan id
- .class: Memilih semua properti yang didefinisikan pada file CSS dengan class (Misalnya, selector: .bg | <tag class="bg"> )


4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama-tama, dibuat file style.css di dalam folder static pada app todolist. Folder static juga diisi dengan gambar-gambar yang akan digunakan pada HTML. Selain menggunakan file style.css, saya juga menggunakan inline CSS untuk beberapa tag tertentu yang tidak membutuhkan banyak property.


Terdapat 4 file yang menggunakan CSS, yaitu login, register, create-task, dan todolist. Pada register dan create-task, saya hanya mengubah background page dan mengubah tata letak dari form-nya. Pada login page, saya menggunakan class "backg" yang didefinisikan pada file style.css untuk mengubah background-nya menjadi sebuah gambar. Kemudian, saya juga menggunakan .center, .center h2, dan .center form untuk mengubah background dan tata letak setiap elemen pada form login.


Pada halaman utama todolist, saya menggunakan 2 elemen utama, yaitu navbar dan cards dari Bootstrap. Pertama-tama, di dalam tag body, kita definisikan navbar beserta properti di dalamnya, yaitu heading yang berisi sapaan kepada user dan 2 tombol, yaitu tombol logout dan tombol untuk menambah task.


Kemudian, untuk setiap iterasi dari data user, dibuat sebuah card yang berisi judul task user, tanggal dibuatnya task, dan juga deskripsi dari task. Proses pembuatan card ini juga memanfaatkan class row, container, dan col-4, di mana nantinya setiap baris akan terdiri dari 3 task cards.

  
