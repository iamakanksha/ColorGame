import wikipedia
import sys
#taking command line arguments
search_term= sys.argv[1]
dump_file=sys.argv[2]

try:
    link=wikipedia.page(str(search_term)).url

except wikipedia.exceptions.PageError as e:
    link=str(e)
#duming links in a text file
with open(str(dump_file),"a+") as file:
    file.write(link+ "\n")