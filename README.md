# 221204-Cashier
Project ini merupakan modul python yang berfungsi untuk melakukan proses CRUD pada sebuah list dengan menggunakan skenario proses transaksi saat berbelanja. 

# Latar Belakang
Membuat modul kasir sederhana yang dapat melakukan tugas:
- Penambahan Item belanja dengan 3 input: Nama, Jumlah, dan Harga
- Modifikasi item belanja pada ketiga inputnya.
- Mengecek apakah semua item transaksi yang diinput sudah sesuai
- Menghapus salah satu atau semua item transaksi
- Menghitung total belanja dan total belanja yang sudah mendapatkan diskon

# Alur kerja
1. Membuat Empty List
2. Menambahkan Item ke list tersebut
3. Mengubah Nama, Jumlah, dan Harga berdasarkan parameter nama item tersebut
4. Menghapus item dan atributnya berdasarkan parameter nama item tersebut
5. Menghapus semua item yang berada di list
6. Mengecek apakah item yang diinput sudah sesuai tipe datanya. 
7. Menghitung total harga masing-masing dan keseluruhan item. Termasuk total harga jika mendapatkan diskon.

# Function: Class Transaction
Semua function modul ini berada di dalam satu Class Transaction.

## 1. __init__
Berfungsi untuk mendefinisikan parameter awal yaitu empty List yang akan digunakan oleh function-function dibawahnya. 
Parameter self digunakan di semua method dibawah agar method tersebut dapat memanggil parameter list yang sudah didefinisikan di method __init__.

## 2. add_item
Berfungsi untuk menambahkan item kedalam list dengan parameter berjumlah 3, yaitu: Nama, Qty, dan Harga. 
### Parameter
- name (any): Nama Barang
- qty (any): jumlah barang
- price (any): harga barang

## 3. update_item_name
Berfungsi untuk memodifikasi item yang sudah ada di list dengan parameter berjumlah 2, yaitu: Nama Sebelumnya dan Nama Setelahnya. 
### Parameter
- name (any): Nama Barang
- updateName (any): Nama Barang yang akan menggantikan Nama sebelumnya

## 4. update_item_qty
Berfungsi untuk memodifikasi item yang sudah ada di list dengan parameter berjumlah 2, yaitu: Nama Sebelumnya dan Nama Setelahnya. 
### Parameter
- name (any): Nama Barang
- updateQty (any): Jumlah barang baru yang akan menggantikan Jumlah barang lama pada item nama yang diberikan

### 5. update_item_price
Berfungsi untuk memodifikasi item yang sudah ada di list dengan parameter berjumlah 2, yaitu: Nama Sebelumnya dan Nama Setelahnya. 
#### Parameter
- name (any): Nama Barang
- updateQty (any): Harga barang baru yang akan menggantikan Harga barang pada item nama yang diberikan

## 6. delete_item
Berfungsi untuk menghapus satu item yang sudah ada di list dengan parameter berjumlah 1, yaitu: Nama item yang ingin dihapus beserta atributnya. 
### Parameter
- name (any): Nama Barang

## 7. reset_transaction
Berfungsi untuk menghapus semua item yang sudah ada di list dan membuat list tersebut menjadi list empty. 
### Parameter
- None

## 9. check_order
Berfungsi untuk mengecek apakah tipe data pada semua item sudah sesuai.
Name: string, Qty: integer, Price: integer.
### Parameter
None

## 10. total_harga
Berfungsi untuk menghitung total harga masing-masing item dan berfungsi untuk menghitung total harga yang
harus dibayarkan setelah mendapatkan diskon.
- Diskon 5%: Jika barang di range harga 200.000-300.000
- Diskon 8%: Jika barang di range harga 300.000-500.000
- Diskon 5%: Jika barang di range harga lebih dari 500.000
### Parameter
- None

# Test Code
Ada 4 Test yang diberikan pada modul ini.
## Tes 1
Menambahkan Item

## Tes 2
Menghapus satu item

## Tes 3
Menghapus semua item

## Tes 4
Menambahkan 4 item baru dan menghitung total harga yang sudah diberikan diskon

# Kesimpulan
Dengan membuat project ini maka user akan memiliki pengalaman terhadap hal-hal berikut:
- Class, Method, & Inheritance
- For Loop & While Loop
- If Else
- Try Catch

Dan dari sisi project management mendapat pengalaman untuk:
- Penggunaan Git
- Penggunaan file Jupyter Notebook
- Pengggunaan file python
- Impor dan Pengetesan Modul

# Terima Kasih :)
