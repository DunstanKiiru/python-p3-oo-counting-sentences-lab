#!/usr/bin/env python3


class MyString:
  def __init__(self, value = ""):
    self.value = ""
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
    else:
      self._value = new_value
    
        

  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    temporary_string = self.value.replace("?", ".").replace("!", ".")
    list = temporary_string.split(".")
    sentences = [l.strip() for l in list if l.strip()]
    return len(sentences)

