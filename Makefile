all: rebuild

build:

rebuild:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	docker build -t backend_base -f Dockerfile .

clean:
	rm -f requirements.txt

fclean: clean

re: fclean all

.PHONY: all build rebuild clean fclean re
