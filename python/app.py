# Fungsi utama untuk menghitung jumlah maksimum double chunks
def max_double_chunks(n, peanut_bits):
    left = 0  # Pointer kiri (mulai iterasi dari awal)
    right = 0  # Pointer kanan (untuk eksplorasi ke depan)
    current_sum = 0  # Variabel untuk menyimpan jumlah bit kacang saat ini
    max_chunks = 0  # Variabel untuk menghitung jumlah double chunks
    total_sum = sum(peanut_bits)  # Jumlah total semua elemen dalam array
    target_sum = total_sum // 2  # Setengah dari total sum untuk mencari double chunk

    # Jika total jumlah kacang ganjil, tidak mungkin ada double chunks
    if total_sum % 2 != 0:
        return 0

    # Looping melalui setiap elemen dalam daftar
    for i in range(n):
        current_sum += peanut_bits[i]  # Tambahkan elemen pada indeks i ke current_sum
        
        # Jika menemukan double chunk (current_sum = target_sum)
        if current_sum == target_sum:
            max_chunks += 1  # Tambahkan satu double chunk
            current_sum = 0  # Reset current_sum untuk mencari double chunk berikutnya
            
    return max_chunks  # Kembalikan jumlah maksimum double chunks

# Bagian input dan output jika kode dijalankan sebagai script
if __name__ == "__main__":
    # Input jumlah chunks N dan array A
    n = int(input("Masukkan jumlah chunk (N): "))
    peanut_bits = list(map(int, input(f"Masukkan {n} bit kacang dalam array A (dipisah spasi): ").split()))
    
    # Validasi input panjang array
    if len(peanut_bits) != n:
        print(f"Error: Jumlah elemen harus sama dengan {n}. Anda memasukkan {len(peanut_bits)} elemen.")
    else:
        # Panggil fungsi utama untuk menghitung hasil
        result = max_double_chunks(n, peanut_bits)
        print("Jumlah maksimum double chunks:", result)