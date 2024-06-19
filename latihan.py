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
        
    elif user == '2':
        quantity = int(input('Berapa: '))
        total_gurame_terbang += gurame_terbang * quantity
        print('-'*20)
        print(f'{quantity} gurame terbang {total_gurame_terbang:,}')
        print('-'*20)
        
    elif user == '3':
        quantity = int(input('Berapa: '))
        total_lalapan_mentah += lalapan_mentah * quantity
        print('-'*20)
        print(f'{quantity} lalapan mentah {total_lalapan_mentah:,}')
        print('-'*20)
    
    elif user == '4':
        quantity = int(input('Berapa: '))
        total_pete_goreng += pete_goreng * quantity
        print('-'*20)
        print(f'{quantity} pete goreng {total_pete_goreng:,}')
        print('-'*20)

    elif user == '5':
        quantity = int(input('Berapa: '))
        total_plecing_kangkung += plecing_kangkung * quantity
        print('-'*20)
        print(f'{quantity} plecing kangkung {total_plecing_kangkung:,}')
        print('-'*20)

    elif user == '6':
        quantity = int(input('Berapa: '))
        total_sambal_dadak += sambal_dadak * quantity
        print('-'*20)
        print(f'{quantity} sambal dadak {total_sambal_dadak:,}')
        print('-'*20)

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

elif ultah == 'n':
    print(f'SUBTOTAL : {total:,}')

else:
    print('terima kasih')


