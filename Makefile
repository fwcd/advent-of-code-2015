OUTDIR = $(CURDIR)/out
SRCDIR = $(CURDIR)/src

.PHONY:
all: $(OUTDIR)/day20

$(OUTDIR)/day20: $(SRCDIR)/day20.c $(OUTDIR)
	$(CC) -Wall -Ofast -o $(OUTDIR)/day20 $(SRCDIR)/day20.c

$(OUTDIR):
	mkdir -p $(OUTDIR)
