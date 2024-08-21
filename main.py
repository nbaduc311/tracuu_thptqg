import requests
import re
import time

# Pre-compile the regular expressions
student_id_regex = re.compile(r'value="(\d+)"')
name_regex = re.compile(r'Họ tên&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\s*</th>\s*<td>(.*?)</td>')
birth_date_regex = re.compile(r'Ngày sinh&nbsp;\s*</th>\s*<td>(.*?)</td>')
university_regex = re.compile(r'<td><b>Trường</b></td>\s*<td>(.*?)</td>')
university_code_regex = re.compile(r'<td><b>Mã trường</b></td>\s*<td>(.*?)</td>')
admission_code_regex = re.compile(r'<td><b>Mã tuyển sinh</b></td>\s*<td>(.*?)</td>')
priority_regex = re.compile(r'<td><b>Thứ tự nguyện vọng</b></td>\s*<td>(\d+)</td>')

def check_file(file_content):
    # Kiểm tra sự tồn tại của cụm từ trong toàn bộ nội dung
    if "Bạn không nằm trong danh sách đạt ở các trường được ủy quyền công bố" in file_content:
        return False
    return True

# Hàm xử lý và lấy thông tin từ file .txt
def extract_info_from_file(file_content):
    # Sử dụng regex để tìm kiếm các thông tin cần thiết
    student_id_match = student_id_regex.search(file_content)
    name_match = name_regex.search(file_content)
    birth_date_match = birth_date_regex.search(file_content)
    university_match = university_regex.search(file_content)
    university_code_match = university_code_regex.search(file_content)
    admission_code_match = admission_code_regex.search(file_content)
    priority_match = priority_regex.search(file_content)

    # Kiểm tra từng giá trị, nếu không tìm thấy thì trả về giá trị mặc định hoặc xử lý lỗi
    if not (student_id_match and name_match and birth_date_match and university_match and university_code_match and admission_code_match):
        return None  # Hoặc xử lý lỗi theo cách khác

    student_id = student_id_match.group(1)
    name = name_match.group(1)
    birth_date = birth_date_match.group(1)
    university = university_match.group(1)
    university_code = university_code_match.group(1)
    admission_code = admission_code_match.group(1)
    priority = priority_match.group(1) if priority_match else "0"

    # Kết hợp các thông tin thành chuỗi kết quả
    result = f"{student_id},{name},{birth_date},{university},{university_code},{admission_code},{priority}"
    return result


# URL của trang web bạn muốn gửi POST request
url = "http://kqmb.hust.edu.vn/"

number = 1

results = []

# Sử dụng session để tối ưu hóa request
with requests.Session() as session:
    while number < 100000:
        cccd = '001306'+f'{number:06d}' 
        # Dữ liệu POST cần gửi
        payload = {
            'cmt': cccd,
            '6_letters_code': '2AGT',
            'submit': 'Tra cứu'
        }

        # Gửi POST request
        response = session.post(url, data=payload)
        file_content = response.text

        if check_file(file_content):
            result = extract_info_from_file(file_content)
            results.append(result)
            print("____________HỢP LỆ____________")

        # Kiểm tra kết quả phản hồi
        print(f"Đây là response của căn cước công dân số 001306{number}")
        count += 1
        number += 1

        # Viết kết quả vào file sau mỗi 1000 số kiểm tra
        if len(results) >= 50:
            with open('hanoi_female_2k6.txt', 'a', encoding='utf-8-sig') as file:
                file.write("\n".join(results) + "\n")
            results.clear()

    # Ghi lại bất kỳ kết quả nào còn lại
    if results:
        with open('hanoi_female_2k6.txt', 'a', encoding='utf-8-sig') as file:
            file.write("\n".join(results) + "\n")
