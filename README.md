# VMX on WPI and W4Studica documentation

The home page introduces both projects. The **VMX on WPI** guides live under
`/vmxonwpi/` and cover WPILib 2026, the VMX2026 extension, and the Ubuntu-based
robot setup. The separate **W4Studica** guides live under `/W4Studica/` and cover
their WPILib 2027 beta. Their setup steps, extensions, and release streams are
different; do not treat either guide as a copy of the other.

Doxygen builds the W4Studica C++ API reference at `/W4Studica/apidocs/`. It is
not duplicated under VMX on WPI because that API is for the separate W4Studica
2027 codebase. English and Korean pages are in matching `docs/en/` and `docs/ko/`
folders; the Material language selector switches between page translations.

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

Open `http://127.0.0.1:8000/` for the portal or
`http://127.0.0.1:8000/W4Studica/apidocs/` for the W4Studica API. Rebuilding MkDocs clears `site/`, so always
run the API builder afterward. Generated HTML is ignored by Git. Parser warnings
are saved to `.site/apidocs-warnings.log`, outside the public site. The builder
checks required pages, theme checksums and accidental local paths before replacing
the generated API directory. `build-info.json` records the source, theme and tool.

GitHub Actions uses the same build order and deploys the combined `site/` artifact.
The vendored Doxygen Awesome 2.5.0 theme is MIT licensed; its pinned source and
file checksums are in `apidocs/theme/SOURCE.json`. Only the base CSS is loaded.
