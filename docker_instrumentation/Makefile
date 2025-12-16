# Variables pour éviter les répétitions
IMAGE_NAME=prometheus/custom_app
PORT=5001

# La règle par défaut (quand on tape juste 'make')
all: build run

# 1. Construire l'image
build:
	sudo docker build -t $(IMAGE_NAME):latest .

# 2. Lancer le conteneur
run:
	sudo docker run -d -p $(PORT):$(PORT) --name my_app $(IMAGE_NAME):latest

# 3. Arrêter et supprimer le conteneur proprement
stop:
	sudo docker rm -f my_app || true

# 4. Tout refaire : Stop -> Build -> Run
redeploy: stop build run

# 5. Voir les logs
logs:
	sudo docker logs -f my_app