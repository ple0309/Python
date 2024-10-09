#Author: Jaden Le, Peter Tawfik
#Student ID: Jaden-032592883, Peter-033266933
#Date: 10/07/2024
#Description: Encrypting and Decrypting the message from the user's input.

import cipher
import caesar
import check_input


def main():
  ci = cipher.Cipher() #Create cipher object.
  file = open("message.txt", 'a')
  
  print("Secret Decoder Ring:")
  print("1. Encrypt")
  print("2. Decrypt")
  input_en_or_de = check_input.get_int_range("",1,2) #Encrypt or Decrypt.
  print("Enter encryption type:")
  print("1. Atbash")
  print("2. Caesar")
  input_at_or_ca = check_input.get_int_range("",1,2) #Atbash or Caesar.

  #If it is Encrypt.
  if input_en_or_de == 1:
    file = open("message.txt", 'w')
    message = str(input("Enter message: "))

    #If it is Atbash.
    if input_at_or_ca == 1:
      file.write(ci.encrypt_message(message))

    #If it is Caesar.
    else:
      shift = check_input.get_int_range("Enter shift: ",0,25)
      ca = caesar.Caesar(shift)
      file.write(ca.encrypt_message(message))
      
    file.close()
    print("Encrypted message saved to \"message.txt\".")

  #If it is Decrypt.
  else:
    file = open("message.txt", 'r')
    str_in_file = file.read()

    #If it is Atbash.
    if input_at_or_ca == 1:
      print(f"Decrypted message: {ci.decrypt_message(str_in_file)} ")

    #If it is Caesar.
    else:
      shift = check_input.get_int_range("Enter shift: ",0,25)
      ca = caesar.Caesar(shift)
      print(f"Decrypted message: {ca.decrypt_message(str_in_file)} ")
    file.close()

      
main()