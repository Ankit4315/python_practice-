import time 

timestame = time.strftime('%H:%M:%S')
print(timestame)
timestame = int(time.strftime('%H'))


if timestame > 4 and timestame < 10:
  print("good morning")

if timestame > 10 and timestame < 16:
  print("good afternon")

if timestame > 16 and timestame < 22:
  print("good evining")

if timestame > 22 and timestame < 6:
  print("good night")























