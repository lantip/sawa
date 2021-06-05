

def replace_en_num(number: any) -> str:
    """
    Replace en number with jw number
    :param number: any
    :return: text: str
    """
    text = str(number)
    num_dict = {"0": "꧐", "1": "꧑", "2": "꧒", "3": "꧓", "4": "꧔", "5": "꧕", "6": "꧖", "7": "꧗", "8": "꧘", "9": "꧙"}
    for num in num_dict.keys():
        if num in text:
            text = text.replace(num, num_dict[num])
    return text
