istring = "C:\Python3\python.exe"

file_name = istring[11:]
extension_name = istring[18:]
catalog_name = istring[3:10]
full_path_name = istring[:11]

print(f"Имя файла: {file_name}")
print(f"Расширение: {extension_name}")
print(f"Имя каталога {catalog_name}")
print(f"Полный путь к файлу {full_path_name}")