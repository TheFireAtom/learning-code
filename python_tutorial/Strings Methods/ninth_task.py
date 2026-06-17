from transliterate import translit

text_cyrillic = input("Введите фразу на русском: ")
return_latin = translit(text_cyrillic, language_code="ru", reversed=True)
print(return_latin)