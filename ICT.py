def compress(original):
  results =""
  current_run_char = ""
  run_length = 0

  for i in range(len(original)):
    if i == 0:
      current_run_char = original[i]
      run_length = 1
    else:
      current_char = original[i]
      if current_char == current_run_char:
        run_length += 1
      else:
        results += current_run_char + str(run_length)
        current_run_char = current_char
        run_length = 1
  results += current_run_char + str(run_length)
  return results

def decompress(ct):
  results = ""
  for i in range(0, len(ct), 2):
    character = ct[i]
    run_length = int(ct[i+1]) 
    for j in range(run_length):
      results += character
  return results

original_text = input("Please, enter your text here: ")
print(original_text)
print("")

ct = compress(original_text)
print(ct)
print("")

dt = decompress(ct)
print(dt)
print("")

if original_text == dt:
  print("Success! The decompressed text is the same to original one!")
