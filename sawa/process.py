import sys
from sawa.enum.effected import Effected
from sawa.enum.token_error import TokenError
import sawa.util as util


class Process:

    def __init__(self, file, num_dict: dict, keyword_dict: dict, function_dict: dict):
        self.file = file
        self.num_dict = num_dict
        self.keyword_dict = keyword_dict
        self.function_dict = function_dict
        self.line = ''
        self.buffer = ''
        self.token = ''
        self.las_symbol = ''
        self.next_symbol = ''
        self.current_symbol = ''
        self.effected = Effected.AS_NONE
        self.line_no = 0
        self.char_no = 0

        self.operators = '=!<>+-%/*^'
        self.symbols = '#\"\':;.,@'
        self.brackets = '()[]{}'
        self.all_symbols = self.operators + self.symbols + self.brackets

    def report_error(self, error: TokenError) -> None:
        error_str = error.value + " " + " ꦤꦁꦧꦫꦶꦱ꧀ꦤꦺꦴꦩꦼꦂ " \
                    + util.replace_en_num(self.line_no) + ":" + util.replace_en_num(self.char_no)
        error_str = self.line + '\n' + error_str
        sys.exit(error_str)

    def change_number(self) -> None:
        if self.token is None or self.token == '':
            return
        new_token = ''
        for c in self.token:
            if c in self.num_dict.keys():
                new_token += self.num_dict[c]
            else:
                self.report_error(TokenError.INVALID_TOKEN)
        self.token = new_token

    def change_keyword(self) -> bool:
        if self.token is None or self.token == '':
            return False

        # If the token is a javanese number it will replace english number
        if self.token[0] in self.num_dict.keys():
            self.change_number()
            return True
            # return ''.join([num_dict[c] for c in token]), True

        # If the token matches any python keywords it replaces that keywords
        if self.token in self.keyword_dict.keys():
            self.token = self.keyword_dict[self.token]
            if self.token == 'from' or self.token == 'import':
                pass
            elif self.token == 'if' or self.token == 'elif' or self.token == 'else' or self.token == 'while' or self.token == 'for':
                pass
            elif self.token == 'def' or self.token == 'lamda':
                pass
            elif self.token == 'class':
                pass
            return True

        # If nothing matches it returns token as it
        return False

    def change_function(self) -> bool:
        if self.token is None or self.token == '':
            return False

        # If the token matches any python in built it replaces that function name
        if self.token in self.function_dict.keys():
            self.token = self.function_dict[self.token]
            return True

        # If nothing matches it returns false
        return False

    def get_next_symbol(self) -> bool:
        self.next_symbol = ''
        for character in self.line[self.char_no:]:
            if character == " " or character == "\n" or character in self.all_symbols:
                if character != " " and character != "\n":
                    self.next_symbol = character
                    return True
            else:
                return False

        return False

    def process_line(self):

        py_line = ''  # new line to store all characters and processed buffer or buffer

        self.buffer = ''  # Store buffer
        self.char_no = 0  # store the characters position
        # self.effected = Effected.AS_NONE

        for character in self.line:
            self.char_no += 1
            if character == " " or character == "\n" or character in self.all_symbols:
                special_character = character  # Since it is special char

                if character != " " and character != "\n":
                    self.current_symbol = special_character

                if special_character == '\'' and self.effected is Effected.AS_NONE:
                    self.effected = Effected.AS_SINGLE_QUOTE_STRING
                elif special_character == '\'' and self.effected is Effected.AS_SINGLE_QUOTE_STRING:
                    self.effected = Effected.AS_NONE
                elif special_character == '\"' and self.effected is Effected.AS_NONE:
                    self.effected = Effected.AS_DOUBLE_QUOTE_STRING
                elif special_character == '\"' and self.effected is Effected.AS_DOUBLE_QUOTE_STRING:
                    self.effected = Effected.AS_NONE
                elif special_character == '#' and self.effected is Effected.AS_NONE:
                    self.effected = Effected.AS_COMMENT
                elif special_character == '\n' and self.effected is Effected.AS_COMMENT:
                    self.effected = Effected.AS_NONE
                elif special_character == '\n' and self.effected is Effected.AS_DOUBLE_QUOTE_STRING:
                    self.report_error(TokenError.INCOMPLETE_STRING)
                elif special_character == '\n' and self.effected is Effected.AS_SINGLE_QUOTE_STRING:
                    self.report_error(TokenError.INCOMPLETE_STRING)

                if self.buffer != '':
                    self.token = self.buffer
                    # Process for predefined keywords
                    token_processed = self.change_keyword()  # Processed for keyword
                    if not token_processed and self.las_symbol != '.':
                        # If not processed as keywords and the last symbol is not . i.e not a property
                        if self.current_symbol != '' and self.current_symbol == '(':
                            # If current symbol is start bracket then it is function
                            token_processed = self.change_function()
                        else:
                            self.get_next_symbol()
                            if self.next_symbol != '' and self.next_symbol == '(':
                                token_processed = self.change_function()
                    py_line += self.token
                    self.buffer = ''
                    self.token = ''
                py_line += special_character
                self.current_symbol = ''
                if character != " " and character != "\n":
                    self.las_symbol = special_character
            else:
                if self.effected is Effected.AS_NONE:
                    self.buffer += character
                else:
                    py_line += character

        return py_line

    def process(self):

        py_content = ""  # store all the processed line or py_line
        # line_no = 0  # store the characters position
        for line in self.file:
            self.line_no += 1

            # Replace unicode and other javanese character to english.
            line = line.replace("\u202b", "")
            line = line.replace("\u202c", "")
            line = line.replace("꧈", ",")
            line = line.replace("꧉", ".")
            line = line.replace("꧇", "")
            line = line.replace("٪", "%")

            self.line = line

            # Finally appending line to the content of the file
            py_content += self.process_line()

        return py_content
