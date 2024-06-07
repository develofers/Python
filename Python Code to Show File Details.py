import os

file_path = 'example.txt'

file_size = os.path.getsize(file_path)
file_type = os.path.splitext(file_path)[1]
with open(file_path, 'r') as file:
file_text = file.read()
file_text_length = len(file_text)
file_modified_time = os.path.getmtime(file_path)
file_info = os.stat(file_path)
file_user = file_info.st_uid
with open(file_path, 'r') as file:
lines = file.readlines()
file_line_number = len(lines)
file_char_number = sum(len(line.strip()) for line in lines)

print(f"File Size: {file_size} bytes")
print(f"File Type: {file_type}")
print(f"File Text Length: {file_text_length} characters")
print(f"File Date Modified: {file_modified_time}")
print(f"File Info User: {file_user}")
print(f"File Line Number: {file_line_number}")
print(f"File Character Number (excluding spaces and dots): {file_char_number}")
