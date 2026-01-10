# Horloge de Mamie 

Ce projet consiste à développer une horloge en terminal qui :
- affiche l’heure au format **hh:mm:ss** et s’actualise **toutes les secondes** jusqu’à l’arrêt du programme, 
- permet de **régler/afficher une heure** à partir d’un tuple **(heures, minutes, secondes)** via une fonction dédiée, 
- permet de **régler une alarme** (tuple) et d’afficher un message lorsque l’heure courante correspond à l’alarme. 

Bonus implémentés :
- affichage **12h / 24h** avec **AM/PM** en mode 12h,
- **pause** de l’horloge (suspension de l’actualisation jusqu’à reprise). 

Notre version ajoute aussi une interface plus ergonomique en terminal (menu fixe + une seule ligne d’état mise à jour) et un **son d’alarme**.

---

## Utilisation

### Lancer le programme :
```
python main.py
```

### Commandes :
```
p : pause / reprise (si l’alarme sonne : p l’arrête et coupe le son)

m : changer le mode (12h / 24h)

a : régler l’alarme (HH:MM ou HH:MM:SS, ou none)

q : quitter
```

### Prérequis : 
```
Windows (lecture non bloquante via msvcrt)

Python

Pour le son : pygame
```

### Installation de la dépendance audio :
```
bash
pip install pygame
Le fichier alarm.mp3 doit être au même niveau que main.py.
```

### Structure du projet : 
```
main.py : orchestration, états, commandes et affichage

display_hour.py : mise à jour d’une seule ligne d’affichage

tick_time.py : incrément du temps simulé (1 seconde)

format_time.py : formatage 12h/24h (+ AM/PM)

models.py : validation d’heure + normalisation du mode

set_alarm_time.py : saisie/parsing de l’alarme

check_alarm.py : déclenchement de l’alarme (comparaison)

pause_resume.py : gestion pause/reprise

alarm_sound.py : gestion du son (pygame)

alarm.mp3 : son d’alarme
```

---

## [![forthebadge](data:image/svg+xml;base64,PHN2ZyBkYXRhLXYtM2M4N2I3YjQ9IiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTM4LjMxMDUxMjU0MjcyNDYiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxMzguMzEwNTEyNTQyNzI0NiAzNSIgY2xhc3M9ImJhZGdlLXN2ZyI+PGRlZnMgZGF0YS12LTNjODdiN2I0PSIiPjwhLS0tLT48IS0tLS0+PCEtLS0tPjwvZGVmcz48cmVjdCBkYXRhLXYtM2M4N2I3YjQ9IiIgd2lkdGg9Ijg1Ljk5ODgwOTgxNDQ1MzEyIiBoZWlnaHQ9IjM1IiBmaWxsPSIjZjU4MjVjIi8+PHJlY3QgZGF0YS12LTNjODdiN2I0PSIiIHg9Ijg1Ljk5ODgwOTgxNDQ1MzEyIiB3aWR0aD0iNTIuMzExNzAyNzI4MjcxNDg0IiBoZWlnaHQ9IjM1IiBmaWxsPSIjZmZhODU3Ii8+PCEtLS0tPjx0ZXh0IGRhdGEtdi0zYzg3YjdiND0iIiB4PSI0Mi45OTk0MDQ5MDcyMjY1NiIgeT0iMTcuNSIgZHk9IjAuMzVlbSIgZm9udC1zaXplPSIxMiIgZm9udC1mYW1pbHk9IlJvYm90bywgc2Fucy1zZXJpZiIgZmlsbD0iI0ZGRkZGRiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgbGV0dGVyLXNwYWNpbmc9IjIiIGZvbnQtd2VpZ2h0PSI2MDAiIGZvbnQtc3R5bGU9Im5vcm1hbCIgdGV4dC1kZWNvcmF0aW9uPSJub25lIiBmaWxsLW9wYWNpdHk9IjEiIGZvbnQtdmFyaWFudD0ibm9ybWFsIiBzdHlsZT0idGV4dC10cmFuc2Zvcm06IHVwcGVyY2FzZTsiPlLDiUFMSVPDiSA8L3RleHQ+PCEtLS0tPjx0ZXh0IGRhdGEtdi0zYzg3YjdiND0iIiB4PSIxMTIuMTU0NjYxMTc4NTg4ODciIHk9IjE3LjUiIGR5PSIwLjM1ZW0iIGZvbnQtc2l6ZT0iMTIiIGZvbnQtZmFtaWx5PSJNb250c2VycmF0LCBzYW5zLXNlcmlmIiBmaWxsPSIjRkZGRkZGIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iOTAwIiBsZXR0ZXItc3BhY2luZz0iMiIgZm9udC1zdHlsZT0ibm9ybWFsIiB0ZXh0LWRlY29yYXRpb249Im5vbmUiIGZpbGwtb3BhY2l0eT0iMSIgZm9udC12YXJpYW50PSJub3JtYWwiIHN0eWxlPSJ0ZXh0LXRyYW5zZm9ybTogdXBwZXJjYXNlOyI+UEFSPC90ZXh0PjwhLS0tLT48L3N2Zz4=)](https://forthebadge.com)

**Antuat Abdallah** | **Ahamada Assmine** | **Noémie Feraud**