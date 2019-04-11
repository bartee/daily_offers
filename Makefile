# Print header output
define header
    @echo "================================================================================"
	@echo "$1"
    @echo "================================================================================"
endef

install:
	pip install -r requirements.txt

build:
	$(call header,"Installing dev dependencies...")
	pip install -r dev-requirements.txt

test: build
	@mkdir -p results
	$(call header,"Running python tests...")
	@py.test -q --junit-xml=results/junit.xml
