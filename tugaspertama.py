nama = input('MASUKAN NAMA :')
umur = int(input('MASUKAN UMUR :'))
tinggi = int(input('MASUKAN TINGGI BADAN :'))
beratbadan = int(input('MASUKAN BERAT BADAN ANDA :'))
nilai_ujian = float(input('MASUKAN NILAI UJIAN ANDA :'))

if (umur <=23) and (tinggi >168) and (nilai_ujian >85) and (umur >=16):
    hasil = ('SELAMAT ANDA LOLOS ADMINISTRASI TARUNA TNI')
else:
    hasil = ('MAAF ANDA BELUM LOLOS ADMINISTRASI TARUNA TNI')

print('='*50)
print('NAMA :             ', (nama))
print('HASIL AKHIR ANDA : ', (hasil))

