.PHONY: install
install:
	cp .env.example .env
	sed -i '/^APP_PORT=/s/=.*/=8666/' .env
	sudo mkdir -p /srv/docker
	sudo cp -a $(PWD) /srv/docker/
	cp *.desktop ~/Desktop/
