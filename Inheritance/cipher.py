class Cipher:
  """Represents for the user's encrypt and decrypt.
  Attribute:
    alphabet(str): storing the list of A-Z.
  """
  def __init__(self):
    self._alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def encrypt_message(self,message):
    """Return the encrypted message."""
    encrypted_string = ""
    for i in message.upper():
      if i in self._alphabet:
        encrypted_string += self._encrypt_letter(i)
      else:
        encrypted_string += str(i)
    return encrypted_string
    
  def decrypt_message(self,message):
    """Return the decrypted message."""
    decrypted_string = ""
    for i in message:
      if i in self._alphabet:
        decrypted_string += self._decrypt_letter(i)
      else:
        decrypted_string += str(i)
    return decrypted_string

  def _encrypt_letter(self,letter):
    """Return each letter in the message after encrypted."""
    location = self._alphabet.index(letter)
    encrypted_position = 25 - location
    return self._alphabet[encrypted_position]
        
    
  def _decrypt_letter(self,letter):
    """Return each letter in the message after decrypted."""
    location = self._alphabet.index(letter)
    decrypted_position = 25 - location
    return self._alphabet[decrypted_position]
