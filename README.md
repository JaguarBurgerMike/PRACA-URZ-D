# Monitor BIP Praca

## Cel projektu

Automatyczne monitorowanie ofert pracy i naborów publikowanych w BIP gmin z okolic Bochni.

Po wykryciu nowego ogłoszenia system:

1. Pobiera strony BIP.
2. Wyszukuje ogłoszenia.
3. Porównuje je z zapisanym stanem.
4. Wysyła powiadomienie na Discord.
5. Aktualizuje bazę danych.

---

## Technologie

* Python 3.12
* Playwright
* GitHub Actions
* Discord Webhook
* JSON

---

## Struktura plików

### monitor.py

Główny skrypt.

Odpowiada za:

* pobieranie stron BIP,
* wykrywanie nowych ogłoszeń,
* wysyłanie wiadomości na Discord,
* zapis do database.json.

### sites.json

Lista monitorowanych stron.

Przykład:

```json
{
  "Bochnia": "https://...",
  "Rzezawa": "https://..."
}
```

### database.json

Baza zapisanych ogłoszeń.

Na jej podstawie wykrywane są nowe wpisy.

### requirements.txt

Zawiera:

```text
playwright
requests
```

---

## Monitorowane gminy

* Bochnia
* Rzezawa
* Brzesko
* Drwinia
* Kłaj
* Gdów
* Łapanów
* Żegocina
* Lipnica Murowana
* Gnojnik
* Dębno

---

## Discord

Powiadomienia wysyłane są przez webhook Discord.

Sekret GitHub:

```text
DISCORD_WEBHOOK
```

Dodany w:

Settings → Secrets and variables → Actions

---

## GitHub Actions

Workflow uruchamia się:

* ręcznie (workflow_dispatch)
* automatycznie co 3 godziny

Cron:

```yaml
schedule:
  - cron: '0 */3 * * *'
```

---

## Aktualny status projektu

Działa:

* monitorowanie stron BIP,
* wykrywanie nowych ogłoszeń,
* zapis do database.json,
* Discord webhook,
* automatyczny commit bazy.

---

## Możliwe przyszłe ulepszenia

### Powiadomienia z linkiem

Dodanie bezpośredniego linku do ogłoszenia.

### Filtrowanie stanowisk

Powiadomienia tylko dla:

* budownictwa,
* inwestycji,
* drogownictwa,
* geodezji,
* administracji.

### Osobne kanały Discord

Oddzielne powiadomienia dla różnych gmin.

### Raport dzienny

Jedna zbiorcza wiadomość dziennie.

---

## Repozytorium

Projekt monitoruje oferty pracy z BIP i wysyła powiadomienia na Discord poprzez GitHub Actions.
