Nama    : Trisno Bayu Pamungkas

NPM     : 2106702200

Kelas   : PBP-F

Asdos   : BYN



#Tugas 6

1) Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.


- Synchronous programming

Konsep pemrograman di mana proses berjalannya program terjadi secara sequential. Setiap task akan dieksekusi sesuai urutan dibuatnya task tersebut.

- Asynchronous programming

Konsep pemrograman asinkronus memungkinkan proses jalannya program berlangsung secara bersamaan tanpa menunggu proses antrian task, yang berarti urutan task yang dieksekusi tidak harus sesuai dengan urutan dibuatnya task tersebut. Salah satu penerapan pemrograman asinkronus adalah menggunakan AJAX (Asynchronous Javascript and XML)

2) Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.


Event-Driven Programming merupakan salah satu penerapan yang dilakukan menggunakan AJAX, di mana jalannya suatu program ditentukan oleh suatu event tertentu. Event yang terjadi bisa berupa dari tindakan user (misal klik mouse), message passing, dan sebagainya.

Salah satu penerapannya di dalam tugas ini adalah ketika user menambahkan data lewat modal. Saat tombol submit ditekan oleh user, maka akan dilakukan penambahan data secara asinkronus menggunakan AJAX ke database Django. Nantinya, data baru tersebut akan bisa diakses dan ditampilkan secara langsung tanpa perlu reload seluruh page

3) Jelaskan penerapan asynchronous programming pada AJAX.


Secara konsep, AJAX itu sendiri memanfaatkan transfer data asinkronus (HTTP request) antara web server dan browser. Dengan menggunakan AJAX, dapat terjadi komunikasi antara Javascript dengan web server menggunakan sebuah objek yang dinamakan XMLHttpRequest. Objek Javascript tersebut nantinya dapat melakukan pertukaran data tanpa kita harus me-load ulang seluruh page.


4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.


- Menambahkan tag script pada base.html untuk menggunakan AJAX pada html todolist, yaitu "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"


- Memodifikasi file todolist.html dengan menambahkan Modal yang berisikan form untuk mengambil data baru dari user. Nantinya, data tersebut diproses menggunakan javascript. 


- Menambahkan tag script pada bagian akhir HTML yang berisikan kode-kode Javascript untuk melakukan pengambilan data menggunakan AJAX GET dan menambahkan data ke dalam database django menggunakan AJAX POST. Secara langsung, nantinya HTML akan terupdate dengan adanya penambahan data baru pada table todolist.



