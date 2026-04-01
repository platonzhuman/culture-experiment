
.PHONY: create-practice remove-practice req


create-practice:
ifndef NAME
	$(error NAME if not defined)
endif
	mkdir -p $(NAME)
	cp PracticeMakefile $(NAME)/Makefile

remove-practice:
ifndef NAME
	$(error NAME if not defined)
endif
	rm -rf $(NAME)

req:
	pipreqs . --diff requirements.txt