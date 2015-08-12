
TEXT=wagahaiwa_nekodearu.txt
PYTHON=python2
TMP=temp.txt
WORD=word.txt
DATA=database.txt

default: ai.py wagahaiwa_nekodearu.txt
	#head --bytes=100 $(TEXT) > $(TMP)
	head --lines=200 $(TEXT) | tail --lines=5 > $(TMP)
	$(PYTHON) ai.py $(TMP) >> $(WORD)
	rm $(TMP)

word:
	cat $(WORD) >> $(DATA)
	cat $(DATA) | sort | uniq > $(TMP)
	cp $(TMP) $(DATA)
	rm -f $(TMP)
