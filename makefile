all:
	cd ~/work/gittest/remote && echo '22' >> 6 && git add . && git commit -m 'aasds'
	cd /home/lzg/work/checkupdate
	python run.py