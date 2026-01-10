# Horloge de Mamie 

Ce projet consiste à développer une horloge en terminal qui :

* **affiche l’heure** au format `hh:mm:ss` et s’actualise **toutes les secondes** jusqu’à l’arrêt du programme, 
* **permet de régler/afficher une heure** à partir d’un tuple `(heures, minutes, secondes)` via une fonction dédiée, 
* **permet de régler une alarme** (tuple) et d’afficher un message lorsque l’heure courante correspond à l’alarme. 

### Bonus implémentés :

* affichage `12h / 24h` avec `AM/PM` en mode 12h,
* **pause** de l’horloge (suspension de l’actualisation jusqu’à reprise). 

Notre version ajoute aussi une interface plus ergonomique en terminal (menu fixe + une seule ligne d’état mise à jour) et un **son d’alarme**.

---

## Utilisation

### Lancement du programme 

```
python main.py
```

### Commandes :
```
p : pause / reprise (si l’alarme sonne : p l’arrête et coupe le son)

m : changer le mode (12h / 24h)

a : régler l’alarme (HH:MM ou HH:MM:SS, ou none)

s : quitter
```

### Prérequis 

* **OS:** Windows (requis pour la lecture non bloquante de touche via `msvcrt`).
* **Python 3.x**
* **Dependances:** `pygame` (pour l'audio).

### Installation:

1.  Cloner le repertoire 
2.  Installer la librairie audio requise :
    ```bash
    pip install pygame
    ```
3.  Etre sûr que le fichier `alarm.mp3` est au même niveau que `main.py`.

### Structure du projet : 

* **main.py** : orchestration, états, commandes et affichage

* **display_hour.py** : mise à jour d’une seule ligne d’affichage

* **tick_time.py** : incrément du temps simulé (1 seconde)

* **format_time.py** : formatage 12h/24h (+ AM/PM)

* **models.py** : validation d’heure + normalisation du mode

* **set_alarm_time.py** : saisie/parsing de l’alarme

* **check_alarm.py** : déclenchement de l’alarme (comparaison)

* **pause_resume.py** : gestion pause/reprise

* **alarm_sound.py** : gestion du son (pygame)

* **alarm.mp3** : son d’alarme


## [![Réalisé par](https://img.shields.io/badge/R%C3%89ALIS%C3%89-PAR-orange?style=for-the-badge)](https://forthebadge.com)

**Antuat Abdallah** | **Ahamada Assmine** | **Noémie Feraud**