import json
import os


def main():
    os.system('cls')
    while True:
        print_userinfo()
        print('\t<< 目錄 >>')
        print(' 0. 離開')
        print(' 1. 全部更新')
        print(' 2. 身分證字號')
        print(' 3. 出生年份')
        print(' 4. 出生月份')
        print(' 5. 出生日期')
        print('='*40)
        try:
            user_input = int(input('::請選擇你要更新的資料::\n\t>>'))
        except:
            print('!Error~ 只接受數字')
            continue

        if user_input == 0:
            break
        elif user_input == 1:
            update_idnumber()
            update_BDYear()
            update_BDMonth()
            update_BDDay()
        elif user_input == 2:
            update_idnumber()
        elif user_input == 3:
            update_BDYear()
        elif user_input == 4:
            update_BDMonth()
        elif user_input == 5:
            update_BDDay()
        else:
            print('!Error~ 超出範圍')


def update_idnumber():
    id_number = ''
    while True:
        user_input = input('::請輸入病患身分證字號::\n\t>>')
        # 檢驗輸入值之有效性, 長度、第一碼英文、後九碼數字
        if len(user_input) != 10:
            print('!Error~ 輸入長度錯誤')
            continue
        id_number = user_input[0].upper()
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V', 'W' , 'X', 'Y', 'Z']
        if not(id_number in letters):
            print('!Error~ 第一碼必須是英文')
            continue
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for element in user_input[1:]:
            if element in numbers:
                id_number += element
            else:
                print('!Error~ 非身分證格式')
                break
        if len(id_number) == 10:
            break
        else:
            continue

    with open('patient_info.txt', 'r', encoding='utf') as f:
        content = json.load(f)
    content['id_number'] = id_number
    with open('patient_info.txt', 'w', encoding='utf') as g:
        json.dump(content, g, ensure_ascii=False, indent=4)

    print('身份證字號已更新為', id_number)


def update_BDYear():
    while True:
        user_input = input('::請輸入病患出生年份::\n\t>>')
        # 檢驗輸入值之有效性
        try:
            BDYear = int(user_input)
            break
        except:
                print('!Error~ 只接受數字')

    with open('patient_info.txt', 'r', encoding='utf') as f:
        content = json.load(f)
    content['BDYear'] = BDYear
    with open('patient_info.txt', 'w', encoding='utf') as g:
        json.dump(content, g, ensure_ascii=False, indent=4)

    print('出生年份已更新為', BDYear)


def update_BDMonth():
    while True:
        user_input = input('::請輸入病患出生月份::\n\t>>')
        # 檢驗輸入值之有效性
        try:
            BDMonth = int(user_input)
            break
        except:
                print('!Error~ 只接受數字')

    with open('patient_info.txt', 'r', encoding='utf') as f:
        content = json.load(f)
    content['BDMonth'] = BDMonth
    with open('patient_info.txt', 'w', encoding='utf') as g:
        json.dump(content, g, ensure_ascii=False, indent=4)

    print('出生月份已更新為', BDMonth)

def update_BDDay():
    while True:
        user_input = input('::請輸入病患出生月份::\n\t>>')
        # 檢驗輸入值之有效性
        try:
            BDDay = int(user_input)
            break
        except:
                print('!Error~ 只接受數字')

    with open('patient_info.txt', 'r', encoding='utf') as f:
        content = json.load(f)
    content['BDDay'] = BDDay
    with open('patient_info.txt', 'w', encoding='utf') as g:
        json.dump(content, g, ensure_ascii=False, indent=4)

    print('出生月份已更新為', BDDay)


def print_userinfo():
    with open('patient_info.txt', 'r', encoding='utf') as f:
        content = json.load(f)
    print('='*20)
    try:
        print("身份證字號為:", content['id_number'])
        print("出生日期為:", content['BDYear'], '年', content['BDMonth'], '月', content['BDDay'], '日')
    except:
        print("資料尚未齊全")
    print('='*20)


if __name__ == "__main__":
    main()