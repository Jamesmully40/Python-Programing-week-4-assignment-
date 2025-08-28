# Writing and reading a PDF file
file=open("output.pdf", "w") 
# Writing some text to the PDF file
file.write("I love python programming, it is very easy to learn.")
#  opening the file in read mode
file=open("output.pdf", "r")
content=file.read()
#  printing the content of the file
print(content)
# Closing the file
file.close()