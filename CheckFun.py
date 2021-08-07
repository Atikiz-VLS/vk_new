import re

def ch_donate(text):
    re_text = re.findall(r"#donatstreet\s*1.\s*Что\s*хотите:\s*Донат\s*2.\s*Ник\s*в\s*игре:\s*[A-Z][a-z]{1,}[ _][A-Z][a-z]{1,}\s*3.\s*Сумма\s*доната:\s*\d+", text)

    a = """#donatstreet
    1. Что хотите: Донат
    2. Ник в игре:
    3.Сумма доната:"""
    print(re_text)
    print(text)
    if re_text:
        return True

def ch_admin(text):
    re_text = re.findall(r"#comadmin\s*1.\s*Ваш игровой ник:\s*[A-Z][a-z]{1,}[ _][A-Z][a-z]{1,}\s*2.\s*Ник администратора, который нарушил:\s*[A-Z][a-z]{1,}[ _][A-Z][a-z]{1,}\s*3.\s*Суть жалобы:\s*\w{1,}\s*4.\s*Доказательства:\s*",text)

    a = """
    #comadmin
    1. Ваш игровой ник: 
    2. Ник администратора, который нарушил: 
    3. Суть жалобы: 
    4. Доказательства:
    """

    if re_text:
        return True

def ch_player(text):
    re_text = re.findall(r"#complayer\s*1.\s*Ваш игровой ник:\s*[A-Z][a-z]{1,}[ _][A-Z][a-z]{1,}\s*2.\s*Ник нарушителя:\s*[A-Z][a-z]{1,}[ _][A-Z][a-z]{1,}\s*3.\s*Суть жалобы:\s*\w{1,}\s*4.\s*Доказательства:\s*",text)

    a = """
    #complayer
    1. Ваш игровой ник: 
    2. Ник нарушителя: 
    3. Суть жалобы: 
    4. Доказательства:
    """
    print(re_text)
    if re_text:
        return True