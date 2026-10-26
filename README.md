# W4Studica documentation

MkDocs builds the guides at `/`. Doxygen Awesome **Base** builds a standalone
C++ API reference at `/apidocs/`, with its own class tree, symbol search, source
browser and light/dark toggle. The MkDocs theme does not wrap the API pages.

The site introduction is available in English at `/` and Korean at `/ko/`.
Place translated pages in the corresponding `docs/en/` and `docs/ko/` folders.
The standard Material language selector switches between matching page
translations. API reference and GitHub links are in the navigation.

The API source commit and displayed version are pinned in `apidocs/source.json`.
Inputs are WPILib public headers, Studica driver headers and W4Studica VMX
integration headers. The VMX HAL SDK is never an input. Library source files are
read without modification. Java API docs are not part of this first setup.

## Local build

Install Python dependencies from `requirements.txt`, plus Doxygen (1.9.8 or newer),
Graphviz and Git. Check out the pinned allwpilib commit alongside this repository,
then build in this order:

```sh
python -m mkdocs build --strict
python scripts/build_apidocs.py --allwpilib ../allwpilib
python -m http.server 8000 --directory site --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/apidocs/`. Rebuilding MkDocs clears `site/`, so always
run the API builder afterward. Generated HTML is ignored by Git. Parser warnings
are saved to `.site/apidocs-warnings.log`, outside the public site. The builder
checks required pages, theme checksums and accidental local paths before replacing
the generated API directory. `build-info.json` records the source, theme and tool.

GitHub Actions uses the same build order and deploys the combined `site/` artifact.
The vendored Doxygen Awesome 2.5.0 theme is MIT licensed; its pinned source and
file checksums are in `apidocs/theme/SOURCE.json`. Only the base CSS is loaded.
