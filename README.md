# Prometheus Learning Lab

> Ce dépôt est uniquement à des fins d'apprentissage.

Ce projet regroupe des configurations et expérimentations autour de **Prometheus** et de son écosystème de monitoring.

## Ce qu'on y trouve

| Dossier / Fichier | Description |
|---|---|
| `prometheus.yml` | Configuration principale de Prometheus |
| `alerting_rules/` | Règles d'alertes Prometheus |
| `alert_manager/` | Configuration d'Alertmanager (routes, receivers) |
| `recording_rules/` | Règles d'enregistrement pour pré-calculer des métriques |
| `Application Instrumentation/` | Exemples d'instrumentation d'applications |
| `docker_instrumentation/` | Monitoring de conteneurs Docker |
| `blackbox_exporter/` | Sondage externe HTTP/TCP avec Blackbox Exporter |
| `Mysqld_exporter/` | Export de métriques MySQL |
| `request_sender.sh` | Script pour générer du trafic de test |

## Stack utilisée

- **Prometheus** — collecte et stockage des métriques
- **Alertmanager** — gestion et routage des alertes
- **Blackbox Exporter** — monitoring boîte noire
- **MySQL Exporter** — métriques base de données
- **Docker** — conteneurisation des services
