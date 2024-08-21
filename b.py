import requests
import re
import time

# URL của trang web bạn muốn gửi POST request
url = "https://tracuu.hanoi.edu.vn/"

count = 1
# male -> 137220  Chắc là hết r
number_start = 1
number_end = 108573

number = number_start

results = []

# Sử dụng session để tối ưu hóa request
with requests.Session() as session:
    while number <= 1:
        sbd = '01'+f'{number:06d}' 
        # Dữ liệu POST cần gửi
        payload = {
            'SOBAODANH': sbd,
            'ConfirmCode': '4khjo'
        }

        # Gửi POST request
        response = session.post(url, data=payload)
        result = response.text

        results.append(result)
        print("____________HỢP LỆ____________")

        # Kiểm tra kết quả phản hồi
        print(f"Đây là response thứ {count} của số {number}")
        count += 1
        number += 1

        # Viết kết quả vào file sau mỗi 1000 số kiểm tra
        if len(results) >= 1:
            with open('diemthi.txt', 'a', encoding='utf-8-sig') as file:
                file.write("\n".join(results) + "\n")
            results.clear()

    # Ghi lại bất kỳ kết quả nào còn lại
    # if results:
    #     with open('diemthi.txt', 'a', encoding='utf-8-sig') as file:
    #         file.write("\n".join(results) + "\n")
