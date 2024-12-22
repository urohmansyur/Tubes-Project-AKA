import time
import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi pengurutan menggunakan algoritma Bubble Sort (Iteratif)
def bubble_sort(prices, items):
    n = len(prices)
    for i in range(n):
        for j in range(0, n - i - 1):
            if prices[j] > prices[j + 1]:
                prices[j], prices[j + 1] = prices[j + 1], prices[j]
                items[j], items[j + 1] = items[j + 1], items[j]
    return prices, items

# Fungsi pengurutan menggunakan algoritma rekursif
def recursive_sort(prices, items):
    if len(prices) <= 1:
        return prices, items
    else:
        mid = len(prices) // 2
        left_prices, left_items = recursive_sort(prices[:mid], items[:mid])
        right_prices, right_items = recursive_sort(prices[mid:], items[mid:])
        return merge(left_prices, left_items, right_prices, right_items)

def merge(left_prices, left_items, right_prices, right_items):
    merged_prices = []
    merged_items = []
    i = j = 0

    while i < len(left_prices) and j < len(right_prices):
        if left_prices[i] < right_prices[j]:
            merged_prices.append(left_prices[i])
            merged_items.append(left_items[i])
            i += 1
        else:
            merged_prices.append(right_prices[j])
            merged_items.append(right_items[j])
            j += 1

    merged_prices.extend(left_prices[i:])
    merged_items.extend(left_items[i:])
    merged_prices.extend(right_prices[j:])
    merged_items.extend(right_items[j:])

    return merged_prices, merged_items

# Fungsi simulasi untuk menghasilkan data harga acak
def generate_data(size):
    items = [f"Item-{i+1}" for i in range(size)]
    prices = [random.randint(1000, 100000) for _ in range(size)]
    return items, prices

# Grafik untuk menyimpan data waktu eksekusi
iteration_values = []
recursive_times = []
iterative_times = []

# Fungsi untuk memperbarui grafik waktu eksekusi
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(iteration_values, recursive_times, label="Recursive", marker="o", linestyle="-")
    plt.plot(iteration_values, iterative_times, label="Iterative", marker="o", linestyle="-")
    plt.title("Performance Comparison: Recursive vs Iterative")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["Number of Items", "Recursive Time (s)", "Iterative Time (s)"]
    for i in range(len(iteration_values)):
        table.add_row([iteration_values[i], recursive_times[i], iterative_times[i]])
    print(table)

# Program utama
print("Sistem Pemantauan Harga Bahan Pokok di Pasar Tradisional")
print("----------------------------------------------------------")

while True:
    try:
        # Input ukuran data dari pengguna
        size = int(input(f"Masukkan jumlah data ke-{len(iteration_values) + 1} (atau ketik -1 untuk keluar): "))
        if size == -1:
            print("Program selesai. Terima kasih!")
            break
        if size <= 0:
            print("Masukkan jumlah data yang valid!")
            continue

        # Generate data acak untuk ukuran size
        items, prices = generate_data(size)
        iteration_values.append(size)

        # Ukur waktu eksekusi algoritma pengurutan (Iteratif)
        start_time = time.time()
        bubble_sort(prices[:], items[:])
        iterative_times.append(time.time() - start_time)

        # Ukur waktu eksekusi algoritma pengurutan (Rekursif)
        start_time = time.time()
        recursive_sort(prices[:], items[:])
        recursive_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print("\nTabel Waktu Eksekusi:")
        print_execution_table()

        # Perbarui grafik waktu eksekusi
        print("\nMemperbarui grafik...")
        update_graph()

    except ValueError:
        print("Masukkan jumlah data yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
