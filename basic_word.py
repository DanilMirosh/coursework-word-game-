class BasicWord:
    """Этот класс работает со словом."""

    def __init__(self, original_word, set_subword):
        self.original_word = original_word
        self.set_subword = set_subword

    def check_word(self, input_word):
        """Проверяет введенные слова в списке допустимых подслов"""
        if input_word in self.set_subword:
            return True
        return False

    def count_subword(self):
        """Подсчитывает количество подслов"""
        return len(self.set_subword)
