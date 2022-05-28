class Player:
    """Хранит информацию об игроке"""

    def __init__(self, name):
        self.name = name
        self.used_words = []

    def get_used_words(self):
        """Возвращает использованные слова"""
        return len(self.used_words)

    def count_used_words(self):
        """Возвращает количество использованных слов"""
        return len(self.used_words)

    def add_word(self, word):
        """Добавляет слова в использованные слова"""
        self.used_words.append(word)

    def check_word_is_new(self, word):
        """Проверяет использования данного слова до этого"""
        if word not in self.used_words:
            return True
        return False
