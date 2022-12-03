import cashier as cs

trans = cs.transaction()

print("\n\nTest Case 1: Add Item\n")
trans.add_item("Ayam Goreng", 2, 20000)
trans.add_item("Pasta Gigi", 3, 15000)
print(trans.list)

print("\n\nTest Case 2: Delete Item\n")
trans.delete_item("Pasta Gigi")
print(trans.list)

print("\n\nTest Case 3: Delete All Item\n")
trans.reset_transaction()
print(trans.list)

print("\n\nTest Case 4: Create New & Calculate Total Price\n")
trans.add_item("Ayam Goreng", 2, 20000)
trans.add_item("Pasta Gigi", 3, 15000)
trans.add_item("Mainan Mobil", 1, 200000)
trans.add_item("Mi Instan", 5, 3000)
trans.total_harga()