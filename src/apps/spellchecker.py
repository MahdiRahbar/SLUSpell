# -*- coding: utf-8 -*-

# Spell_Checker
# Developers: --
# License: -



class SpellChecker():
    def __init__(self, input_text, language_selector, formality_selector):
        self.input_text = input_text
        self.language_selector = language_selector
        self.formality_selector = formality_selector

    def call(self):
        Checked_text = "Yay! It works!"
        return Checked_text