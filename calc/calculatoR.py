# python calculator
print('Yapmak istediğiniz işlemi giriniz:')
print('1. Toplama')
print('2. Çıkarma')
print('3. Çarpma')
print('4. Bölme')

secim = input('Seçiminizi yapınız (1/2/3/4): ')


num1 = float(input('Birinci sayıyı giriniz: '))
num2 = float(input('İkinci sayıyı giriniz: '))


if secim == '1':
    sonuc = num1 + num2
    print(f'{num1} + {num2} = {sonuc}')
elif secim == '2':
    sonuc = num1 - num2
    print(f'{num1} - {num2} = {sonuc}')
elif secim == '3':
    sonuc = num1 * num2
    print(f'{num1} * {num2} = {sonuc}')
elif secim == '4':
    # Bölme işleminde sıfıra bölme kontrolü
    if num2 != 0:
        sonuc = num1 / num2
        print(f'{num1} / {num2} = {sonuc}')
    else:
        print('Bir sayıyı sıfıra bölemezsiniz!')
else:
    print('Geçersiz giriş! Lütfen 1, 2, 3 veya 4 seçeneklerinden birini giriniz.')
