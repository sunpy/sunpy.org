# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = SunPy
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

deploy:
	git branch -f gh-pages && \
	git checkout gh-pages && \
	git reset --hard && \
	git commit --allow-empty -m "Initializing gh-pages branch" && \
	git push origin gh-pages && \
	git checkout master && \
	git worktree add -B gh-pages _build/html origin/gh-pages && \
	cd _build/html && git add --all && git commit -m "Publishing to gh-pages" && cd ..// && \
	git push --force origin gh-pages

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
