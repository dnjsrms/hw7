basket = {}
print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        print()
        print(f'>>>장바구니 보기: {basket}\n')
        print('[검색]')
        find = input('장바구니에서 확인하고자 하는 상품은? ')
        print(f'{find}은(는) {basket.get(find)}개 담겨 있습니다.')
        break
    else:
        num = int(input('수량은? '))
        basket[item]= num
        print(f'장바구니에 {item}가(이) {num}개가 담겼습니다.\n')

