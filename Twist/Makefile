all:
	make twist1
	make twist2
	make twist3
	make twist4
	make twist5

	make detwist1
	make detwist2
	make detwist3
	make detwist4
	make detwist5

twist1:
	cat samples/twist1.txt | python3 twister.py > twisted/twist1.txt

twist2:
	cat samples/twist2.txt | python3 twister.py > twisted/twist2.txt

twist3:
	cat samples/twist3.txt | python3 twister.py > twisted/twist3.txt

twist4:
	cat samples/twist4.txt | python3 twister.py > twisted/twist4.txt

twist5:
	cat samples/twist5.txt | python3 twister.py > twisted/twist5.txt

detwist1:
	cat twisted/twist1.txt | python3 detwister.py woerterliste.txt > detwisted/twist1.txt

detwist2:
	cat twisted/twist2.txt | python3 detwister.py woerterliste.txt > detwisted/twist2.txt

detwist3:
	cat twisted/twist3.txt | python3 detwister.py woerterliste.txt > detwisted/twist3.txt

detwist4:
	cat twisted/twist4.txt | python3 detwister.py woerterliste.txt > detwisted/twist4.txt

detwist5:
	cat twisted/twist5.txt | python3 detwister.py woerterliste.txt > detwisted/twist5.txt


