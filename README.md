# HSMA-7 Module 2G: Creating a DES interface with Streamlit - Part 1

This repository contains materials for module 2H:

* `app/`
    * `app/singlepage/` - simple one page app which runs simulation and displays results.
    * `app/multipage/` - added a home page and demonstrates set-up with `st.navigation()`.
    * Within each of these is a copy of the model used by the app (`model.py`).

* `exercises/` - exercise materials.

* `slides/` - Quarto slides.
    * `slides/slides.qmd` - main slides file.
    * `slides/code/` - Python examples, kept separate to make the slides file easier to read and search.
    * `template` - templates and assets for creating the HSMA slide style.

The slides are deployed on GitHub pages via GitHub actions and can be viewed via the browser at: <https://hsma-programme.github.io/hsma7_2g_streamlit_part1>.

The example apps are deployed with Streamlit Community Cloud and can be viewed at:

* <https://hsma-des-simple.streamlit.app>
* <https://hsma-des-multipage.streamlit.app>

<br>

## Viewing the example app locally

Activate the HSMA `des` GitHub environment. The environment file required is available in <https://github.com/hsma-chief-elf/H7_Phase_1_Artefacts>: `DES_2/environment/environment.yml`.

> **Note:** A record of the packages needed is also available in this repository under `app/requirements.txt` as it is required for deployment.

```
mamba activate des
```

To view the single page app:

```
streamlit run app/singlepage/app.py
```

To view the multipage app:

```
streamlit run app/multipage/app.py
```

<br>

## Viewing the slides locally

The slides environment is defined in `slides/environment.yml`. It is similar to the HSMA `des` environment, but with a few extra dependencies required for rendering the slides. A `requirements.txt` is also provided for use by GitHub actions.

```
mamba env create --file slides/environment.yml
mamba activate hsma7_streamlit_slides
```

To view the slides:

```
quarto preview slides/slides.qmd
```
