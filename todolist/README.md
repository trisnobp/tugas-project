Nama        : Trisno Bayu Pamungkas

NPM         : 2106702200

Kelas       : PBP-F

Asdos       : BYN



1) Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

CSRF atau Cross-Site Request Forgery merupakan serangan yang membuat client tanpa sadar mengirimkan tanpa sadar mengirimkan request ke suatu website melalui website yang sedang diakses. Yang berarti, terdapat serangkaian tindakan terjadi yang dilakukan aplikasi dan tidak dikehendaki oleh client, dan mengancam keamanan informasi client. Misalnya, melalui CSRF yang dilakukan melalui url, jika client meng-kliknya, maka penyerang bisa melakukan perintah apapun yang dia mau, bisa saja seperti mengganti password client dan sebagainya. Oleh karena itu, untuk mencegah kerusakan dan kerugian oleh serangan ini, dibuat sebuah token bernama csrf_token, yang gunanya untuk melakukan validasi request pada server-side, di mana penyerang tidak akan mungking melakukan permintaan HTTP yang valid dan cocok untuk diberikan ke korban.


2) Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Penggunaan generator pada pembuatan elemen <form> membuat kita tidak perlu menuliskan sintaks-sintaks html untuk sebuah form secara manual. Akan tetapi, jika kita ingin membuat elemen <form> secara manual, 



3) Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.