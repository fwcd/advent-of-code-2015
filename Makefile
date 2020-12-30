OUTDIR = $(CURDIR)/out
SRCDIR = $(CURDIR)/src

$(OUTDIR)/%: $(SRCDIR)/%.c $(OUTDIR)
	$(CC) -o $(OUTDIR)/% $(SRCDIR)/%.c

$(OUTDIR):
	mkdir $(OUTDIR)
