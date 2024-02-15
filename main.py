# VARIABLE ADALAH TEMPAT MENYIMPAN DATA

# MENARU / NILAI

a = 10
x = 10
y = 20

# PEMANGGILAN PERTAMA

print("nilai a =",a)
print("nilai x =",x)
print("nilai y =",y)


# PENAMAAN

nilai_y = 300 #HARUS DENGAN MENGGUNAKAN UNDERSCORE
juta10 = 30000 # TIDAK BOLEH MENGGUNAKAN UNDERSCORE JIKA MEMILIKI VARIABLE ANGKA
nilaiZ = 1.8 # ini boleh


# PEMANGGILAN KEDUA 

a = 8
print("nilai a =",a)

# assigment indirect 

b = a 
print("nilai b =",b)



# TIPE DATA 

# TIPE DATA : ANGKA SATUAN 

data_integer = 1 
print("data :", data_integer)
print("- bertipe : ", type(data_integer))


data_float = 1.8
print("data :", data_float)
print("- bertipe : ", type(data_float))


data_string = "python"
print("data :", data_string)
print("- bertipe : ", type(data_string))

data_boolean = 0 # false or true
print("data :", data_boolean)
print("- bertipe : ", type(data_boolean))


# OPRATOR ASSIGMENT 

a = 5 

a += 1 # nilai a di tambah 1
print('nilai a di tambah 1 jadi:',a)

a -= 1 # nilai a di kurang 1 
print('nilai a di kurang 1 jadi:',a)

a *= 3 # nilai a di kali 3 
print('nilai a di kali 3 jadi:',a)


a /= 2 # nilai a di bagi 2
print('nilai a di bagi 2 jadi:',a)


a **= 3 # nilai a di pangkat 3
print('nilai a di pangkat 3 jadi:',a)


# oprasi logika atau boolean 


# not , or, and, xor

# Operator "not": Mengembalikan nilai False jika operandnya True, dan sebaliknya. 

print('====not====')
a = False
c = not a
print('data a =',a)
print('------not')
print('data c =',c)


print('====OR====')

# Operator "or": Menghasilkan nilai True jika setidaknya salah satu operandnya adalah True. Jika kedua operandnya False, hasilnya akan False.

a = False
b = True
c = a or b 
print(a,'or',b, c)


a = True
b = False
c = a or b 
print(a,'or',b, c)


a = True
b = True
c = a or b 
print(a,'or',b, c)


a = False
b = False
c = a or b 
print(a,'or',b, c)


print('=====XOR=====')

# jika beda maka true 

x = True
y = False
result = x ^ y
print(x,'XOR',y,result)


x = False
y = True
result = x ^ y
print(x,'XOR',y,result)


x = True
y = True
result = x ^ y
print(x,'XOR',y,result)


x = False
y = False
result = x ^ y
print(x,'XOR',y,result)

# jika ada false maka false

print('====AND=====')

a = False
b = True
c = a and b 
print(a,'and',b, c)


a = True
b = False
c = a and b 
print(a,'and',b, c)


a = True
b = True
c = a and b 
print(a,'and',b, c)


a = False
b = False
c = a and b 
print(a,'and',b, c)


# menggabungkan string 

nama_awal = 'fila'
nama_akhir = 'fadilla'
nama_lengkap = nama_awal + " " + nama_akhir
print(nama_lengkap)

# menghitung panjang string

panjang = len(nama_lengkap)
print('panjang dari nama lengkap ada = ' + str(panjang))

# mengecek komponen string 


f = 'f'
status = f in nama_lengkap
print(f + 'ada di'+nama_lengkap + '=' + str(status))
print(f,'ada di',nama_lengkap,str(status))

# pengulangan string 

print('hello'*5) 


# indexing 

no = '200903'
print('no',no[3])

# item paling kecil

print('paling kecil',min(nama_awal))

# item paling besar 

print('paling besar',max(nama_lengkap))

# oprator dalam bentuk method 

data = 'filafadilla'
jumlah = data.count(f)
print('jumlah huruf f pada',data,'=',str(jumlah))


data = "ini adalah string"
print(data)
print(type(data))


# cara membuat string

'''
1. dengan single quote '
2. dengan menggunakan double quote "

'''

data = 'dengan menggunakan single quote'
print(data)

data = "dengan menggunakan double quote"
print(data)


'''
 menggabungkan double dan single quote dalam percakapan
'''

print("'hello world'")
print('"hello world"')


# membuat tanda ' menjadi string
# menggunakan \

print('jangan lupa sholat jum\'at')

# backslash
print("C:\\user\\data")

#tab 
print('belajar\tpython')

# backspace
print('belajar\bpython')

# newline 
print('baris pertama.\nbaris kedua')
print


# string literal atau raw
# menggunakan raw string 

print(r'C:\new folder')

# multiline litteral string
print("""
    nama: ucup
    kelas: 3 sd
      """)

# multiline litteral string raw
print(r"""
      nama: ucup
      kelas: 5\tsd
      website: www.ucup.com
      """)


# komparasi 

# ==(sama dengan) , !=(tidak sama dengan) 
#  >(lebih dari) , <(kurang dari) ,
# >=(lebih dari sama dengan) 
#  <= (kurang dari sama dengan) 

print("====KURANG DARI=====")
a = 10
b = 20 
hasil = a < b 
print("hasil dari 10 < 20 adalah: ",hasil)

print("=====LEBIH DARI=====")
a = 10
b = 20 
hasil = a > b 
print("hasil dari 10 > 20 adalah: ",hasil)


print("=====LEBIH DARI SAMA DENGAN=====")
a = 10
b = 20 
hasil = a >= b 
print("hasil dari 10 >= 20 adalah: ",hasil)


print("=====KURANG DARI SAMA DENGAN=====")
a = 10
b = 20 
hasil = a <= b 
print("hasil dari 10 <= 20 adalah: ",hasil)


print("=====SAMA DENGAN=====")
a = 10
b = 20 
hasil = a == b 
print("hasil dari 10 == 20 adalah: ",hasil)


print("=====TIDAK SAMA DENGAN=====")
a = 10
b = 20 
hasil = a != b 
print("hasil dari 10 == 20 adalah: ",hasil)


print("=====OBJECT INDENTITY(is)=====")
x = 5 
y = 5
print("nilai x adalah:",x,"id:",id(x))
print("nilai y adalah:",y,"id:",id(y))
hasil = x is y 
print('hasil dari x is y adalah',hasil)



print("=====OBJECT INDENTITY(is not)=====")
x = 5 
y = 6 
print("nilai x adalah:",x,"id:",id(x))
print("nilai y adalah:",y,"id:",id(y))
hasil = x is not y 
print('hasil dari x is y adalah',hasil)



#INPUT DATA 

# DATA YANG DI MASUKAN SEMUA TIPE NYA AKAN TETAP STRING
nama = input (" masukan nama: ")
print("nama: ", nama , "tipe: ", type(nama))


# MENGCASTING DATA INPUT MENJADI INTEGER

nama = int(input(" masukan umur: "))
print("umur: ", nama, "tipe: ", type(nama))


# MENGCASTING DATA MENJADI FLOAT

nama = float(input(" masukan gaji: "))
print("gaji: ", nama, "tipe: ", type(nama))



# MENGCASTING DATA MENJADI BOOLEAN

nama = bool(input(" masukan hasil: "))
print("hasil: ", nama, "tipe: ", type(nama))


# MERUBAH SATU TIPE KE TIPE YANG LAIN

 # INTEGER


print("=====INTEGER=====")
data_int = 5
print("data = ", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # AKAN FALSE JIKA NILAI 0
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))


## FLOAT 
print("=====FLOAT=====")
data_float = 9.5
print("data = ", data_float, ",type =",type(data_float))

data_float = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # AKAN FALSE JIKA NILAI 0
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))


# BOOLEAN 

print("=====BOLEAN=====") 

data_bool = True
print("data = ", data_bool, ",type =",type(data_bool))

data_float = int(data_bool)
data_str = str(data_bool)
data_bool = float(data_bool) 
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_float, ",type =",type(data_float))


# OPRASI ARITMATIKA 

# TAMBAH + 
print("=====TAMBAH=====")
a = 5 
b = 5 
hasil = a + b 
print(a,'+',b,"hasilnya:",hasil)

# KURANG - 
print("=====KURANG=====")
a = 5 
b = 5 
hasil = a - b 
print(a,'-',b,"hasilnya:",hasil)


# KALI *  
print("=====KALI=====")
a = 5 
b = 5 
hasil = a * b 
print(a,'*',b,"hasilnya:",hasil)


# BAGI / 
print("=====BAGI=====")
a = 20
b = 5 
hasil = a / b 
print(a,'/',b,"hasilnya:",hasil)


# EXPONENSIAL **
print("=====EXPONENSIAL=====")
a = 5 
b = 5 
hasil = a ** b 
print(a,'**',b,"hasilnya:",hasil)


# MODULUS %
print("=====MODULUS=====")
a = 10
b = 5 
hasil = a % b 
print(a,'%',b,"hasilnya:",hasil)


# PRIORITAS OPRASI

a = 10
b = 5
c = 20
hasil = a + b * c / b ** b
print(a,'+',b,'*',c,'/',b,'**',b,"hasilnya",hasil)