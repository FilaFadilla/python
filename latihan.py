print('='*10, 'LATIHAN WHILE', '='*10)

ayam_betutu = 139000
gurame_terbang = 139000
lalapan_mentah = 15000
pete_goreng = 19000
plecing_kangkung = 35000
sambal_dadak = 15000

print(f"1. ayam betutu         {ayam_betutu}")
print(f'2. gurame terbang      {gurame_terbang}')
print(f'3. lalapan mentah      {lalapan_mentah}')
print(f'4. pete goreng         {pete_goreng}')
print(f'5. plecing kangkung    {plecing_kangkung}')
print(f'6. sambal dadak        {sambal_dadak}')

total_ayam_betutu = 0
total_gurame_terbang = 0
total_lalapan_mentah = 0
total_pete_goreng = 0
total_plecing_kangkung = 0
total_sambal_dadak = 0


qty_ayam_betutu = 0
qty_gurame_terbang = 0
qty_lalapan_mentah = 0
qty_pete_goreng = 0
qty_plecing_kangkung = 0
qty_sambal_dadak = 0

print('-'*20)
print('your menu')
print('-'*20)

while True:
    user = input('pilih menu [S jika selesai]: ')
    
    if user == '1':
        quantity = int(input('Berapa: '))
        total_ayam_betutu += ayam_betutu * quantity
        print('-'*20)
        print(f'{quantity} ayam betutu {total_ayam_betutu:,}')
        print('-'*20)
        qty_ayam_betutu += quantity

        
    elif user == '2':
        quantity = int(input('Berapa: '))
        total_gurame_terbang += gurame_terbang * quantity
        print('-'*20)
        print(f'{quantity} gurame terbang {total_gurame_terbang:,}')
        print('-'*20)
        qty_gurame_terbang += quantity
        
        
    elif user == '3':
        quantity = int(input('Berapa: '))
        total_lalapan_mentah += lalapan_mentah * quantity
        print('-'*20)
        print(f'{quantity} lalapan mentah {total_lalapan_mentah:,}')
        print('-'*20)
        qty_lalapan_mentah += quantity
        
    
    elif user == '4':
        quantity = int(input('Berapa: '))
        total_pete_goreng += pete_goreng * quantity
        print('-'*20)
        print(f'{quantity} pete goreng {total_pete_goreng:,}')
        print('-'*20)
        qty_pete_goreng += quantity

    elif user == '5':
        quantity = int(input('Berapa: '))
        total_plecing_kangkung += plecing_kangkung * quantity
        print('-'*20)
        print(f'{quantity} plecing kangkung {total_plecing_kangkung:,}')
        print('-'*20)
        qty_plecing_kangkung += quantity

    elif user == '6':
        quantity = int(input('Berapa: '))
        total_sambal_dadak += sambal_dadak * quantity
        print('-'*20)
        print(f'{quantity} sambal dadak {total_sambal_dadak:,}')
        print('-'*20)
        qty_sambal_dadak += quantity

    elif user.lower() == 's':
        print('Selesai')
        break


    else:
        print('Menu tidak valid, silakan pilih kembali.')

total = total_ayam_betutu + total_gurame_terbang + total_lalapan_mentah + total_pete_goreng + total_plecing_kangkung + total_sambal_dadak

print('-'*20)
print(f'TOTAL BELANJA : {total:,}')
print('-'*20)


diskon = total * 0.3

ultah = input('anda akan mendapatkan voucher 30%\njika anda atau rekan anda berulang tahun\napakah ada yang berulang tahun?[y/n]:')


if ultah == 'y':
    print('-'*20)
    print(f'SUBTOTAL {diskon:,}')
    print('-'*20)

elif ultah == 'n':
    print('-'*20)
    print(f'SUBTOTAL : {total:,}')
    print('-'*20)

else:
    print('terima kasih')

bill = input('ingin cetak bill?[y/n]: ')

if bill.lower() == 'y':
    print('='*10, 'BILL PEMBAYARAN', '='*10)
    if total_ayam_betutu > 0:
        print(f'{qty_ayam_betutu} ayam betutu       : {total_ayam_betutu:,}')
    if total_gurame_terbang > 0:
        print(f'{qty_gurame_terbang} gurame terbang    : {total_gurame_terbang:,}')
    if total_lalapan_mentah > 0:
        print(f'{qty_lalapan_mentah} lalapan mentah    : {total_lalapan_mentah:,}')
    if total_pete_goreng > 0:
        print(f'{qty_pete_goreng} pete goreng       : {total_pete_goreng:,}')
    if total_plecing_kangkung > 0:
        print(f'{qty_plecing_kangkung} plecing kangkung  : {total_plecing_kangkung:,}')
    if total_sambal_dadak > 0:
        print(f'{qty_sambal_dadak} sambal dadak      : {total_sambal_dadak:,}')
    print('-'*20)
    print(f'TOTAL             : {total:,}')
    if ultah.lower() == 'y':
        print(f'DISKON 30%        : {diskon:,}')
        print('-'*20)
        print(f'SUBTOTAL          : {total:,}')
    print('='*10, 'TERIMA KASIH', '='*10)
else:
    print('Terima kasih telah memesan.')
