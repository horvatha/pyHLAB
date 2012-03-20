Híradástechnika laborhoz pylab-os programok
=============================================

A programok a pylab (matplotlib + numpy) csomagok telepítése mellett
működnek Python2.x alatt. Ezek a programok telepítésre kerültek egy
`Lubuntus virtuális gépbeni <http://django.arek.uni-obuda.hu/lubuntu>`_,
mely VirtualBox-szal rögtön használható.

A programok telepítéséhez ennyi kell terminál indítása után::

  git pull http://github.com/horvatha/pyHLAB

Az ipythont a pylab opcióval indítsuk abban a könyvtárban, ahol a
használandó fájljaink vannak::

  cd adott_konyvtar     # belépés a megfelelő könyvtárba
  ipython -pylab

Az említett virtuális gépben az alábbi aliassal is lehet::

  pylab

Az ipythonon belül már importálhatóak és használhatóak a modulok::

  import sorok

Több modul önálló programként is futtatható a parancssorból::

  python t_fdomain.py
