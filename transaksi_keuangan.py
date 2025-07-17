def pilihan():
    print("Anda Ingin Melakukan Transaksi Apa?")
    print("1. Tarik Tunai")
    print("2. Transfer")
    print("3. Bayar Listrik")
    pilih = int(input(" Masukkan Pilihan: "))
    return pilih
def tarikTunai():
    print("Tarik Tunai")
    nominal = int(input("Masukkan Nominal: "))
    Jumlah_setelah_pajak=nominal-(nominal*0.1)
    print("Jumlah Setelah Pajak: ",Jumlah_setelah_pajak)
def transfer():
    print("1. Transfer Sesama Bank")
    print("2. Transfer Antar Bank")
    input_transfer = int(input("Masukkan Pilihan: "))
    if input_transfer == 1:
        nominal = int(input("Masukkan Nominal: "))
        print("Anda Berhasil Melakukan Transfer Sesama Bank Sebesar: ", nominal)
    elif input_transfer == 2:
        nominal = int(input("Masukkan Nominal: "))
        Jumlah_setelah_pajak=nominal-(nominal*0.06)
        print("Anda Berhasil Melakukan Transfer Antar Bank Sebesar: ", Jumlah_setelah_pajak)
def bayarListrik():
    print("Masukkan Nominal Pembayaran Listrik")
    nominal = int(input("Masukkan Nominal: "))
    if nominal==10000:
        print("Anda Berhasil Melakukan Pembayaran Listrik, dan mendapatkan token sebesar 213 Kwh")
    elif nominal==20000:
        print("Anda Berhasil Melakukan Pembayaran Listrik, dan mendapatkan token sebesar 250 Kwh")
    elif nominal==30000:
        print("Anda Berhasil Melakukan Pembayaran Listrik, dan mendapatkan token sebesar 300 Kwh")
    else:
        print("Nominal yang Anda Masukkan Tidak Tersedia")
while True:
    pilih = pilihan()
    if pilih == 1:
        tarikTunai()
        break
    elif pilih == 2:
        transfer()
        break
    elif pilih == 3:
        bayarListrik()
        break
    else:
        print("Pilihan Tidak Tersedia")
        break