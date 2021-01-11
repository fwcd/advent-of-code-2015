OUTDIR = $(CURDIR)/out
SRCDIR = $(CURDIR)/src

.PHONY:
all: $(OUTDIR)/day20-part1

$(OUTDIR)/%: $(SRCDIR)/%.c $(OUTDIR)
	$(CC) -Wall -Ofast -o $@ $<

$(OUTDIR):
	mkdir -p $(OUTDIR)
