import cipher

class Caesar(cipher.Cipher):
  """Represents the Caesar cipher."""
  def __init__(self,shift):
    """Initializes the shift."""
    super().__init__()
    self._shift = shift
    
  def _encrypt_letter(self,letter):
    """Returns each letter will be encrypted for Caesar cipher."""
    location = self._alphabet.index(letter)
    encrypted_position = location + self._shift
    if encrypted_position > 25:
      encrypted_position -= 26
    return self._alphabet[encrypted_position]
    
  def _decrypt_letter(self,letter):
    """Returns each letter will be decrypted for Caesar cipher."""
    location = self._alphabet.index(letter)
    decrypted_position = location - self._shift
    if decrypted_position < 0:
      decrypted_position += 26
    return self._alphabet[decrypted_position]
    