 Híradástechnika laborhoz pylab-os programok
=============================================

A programok a pylab (matplotlib + numpy) csomagok telepítése mellett
működnek Python2 és talán Python3 alatt. Ezek a programok telepítésre kerültek egy
virtuális gépben mely VirtualBox-szal rögtön használható.

A programok telepítéséhez ennyi kell terminál indítása után::

  git pull http://github.com/horvatha/pyHLAB

Az ipythont a pylab opcióval indítsuk abban a könyvtárban, ahol a
használandó fájljaink vannak::

  cd adott_konyvtar     # belépés a megfelelő könyvtárba
  ipython3 --pylab

Az említett virtuális gépben az alábbi aliassal is lehet::

  pylab

Az ipythonon belül már importálhatóak és használhatóak a modulok::

  import sorok

Több modul önálló programként is futtatható a parancssorból::

  python t_fdomain.py
