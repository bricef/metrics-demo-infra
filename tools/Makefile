

DIRECTORIES = $(sort $(dir $(wildcard */)))

NAMES = $(DIRECTORIES:%/=%) 

IMAGES = $(DIRECTORIES:%/=quay.io/brice/%) 


BRANCH = $(shell git rev-parse --abbrev-ref HEAD)
SHA = $(shell git rev-parse --short HEAD)

all: $(IMAGES)

quay.io/brice/%: 
	cd $(@:quay.io/brice/%=%); \
	docker build -t $@:$(BRANCH)-$(SHA) -t $@:$(BRANCH)-latest . ;\
	docker push $@:$(BRANCH)-$(SHA) ;\
	docker push $@:$(BRANCH)-latest
