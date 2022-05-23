# Pencarian Langkah Minimum dalam Permainan Ular Tangga dengan Algoritma Branch and Bound

## Deskripsi
Permainan ular tangga merupakan sebuah permainan papan yang dimainkan di atas papan kotak-kotak berukuran mxn, biasanya berbentuk persegi 10x10. Permainan ini menggunakan guliran dadu untuk menggerakkan bidak pemain. Tujuan dari permainan ini adalah menjadi pemain tercepat yang dapat menggerakkan bidaknya menuju kotak nomor maksimum atau biasanya 100.

Algoritma Branch and Bound merupakan algoritma yang digunakan untuk persoalan optimasi, baik minimasi maupun maksimasi. Permainan ular tangga merupakan persoalan minimasi, yaitu meminimalkan langkah untuk mencapai tujuan. Setiap kemungkinan guliran dadu menjadi dasar untuk pembangkitan ruang status dari algoritma ini. Dalam program ini, ongkos atau bound setiap simpul dihitung dengan cara menjumlahkan langkah dari simpul akar menuju simpul saat ini dan estimasi langkah menuju simpul tujuan.

## Kesimpulan
Algoritma Branch and Bound **GAGAL** mendapatkan solusi optimal dari permainan ular tangga. Hal ini karena ketidakpastian lokasi tangga dan ular sehingga teknik heuristik dalam penentuan ongkos tidak optimal. Penulis menyarankan penggunaan algoritma lain, seperti BFS untuk mencari solusi optimal.

## Cara Menjalankan Program
- Jalankan program dengan mengetik
```
python UlarTangga.py
```
- Masukkan nama file konfigurasi ular tangga yang berisi daftar ular dan tangga, contohnya `board/board1.txt`
- Rute yang ditempuh akan ditampilkan

## Penulis
Hafidz Nur Rahman Ghozali
13520117