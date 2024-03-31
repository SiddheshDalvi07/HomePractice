




source_file_path = 'source.txt'
destination_file_path = 'destination.txt'


source_file = open(source_file_path, 'r')
content = source_file.read()
print("Source file :",content)
source_file.close()

destination_file = open(destination_file_path, 'w')
destination_file.write(content)
destination_file.close()

print("Content copied successfully from", source_file_path, "to", destination_file_path)

destination_file = open(destination_file_path, 'r')
print("Destination file :",destination_file.read())
destination_file.close()
