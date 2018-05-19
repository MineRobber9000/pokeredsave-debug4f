mod.sav: main.o
	python linker.py main.o
	python hacker.py

main.o: main.asm
	rgbasm -o main.o main.asm

.PHONY: clean
clean:
	rm *.bin mod.sav main.o
	rm -rf __pycache__
