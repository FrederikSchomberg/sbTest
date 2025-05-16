
# Projektdokumentation kompilieren 

## Voraussetzungen

- LaTeX ist installiert
    - Windows: MikTeX
    - Linux: TeX Live
- Optional: VS Code oder Overleaf als Editor

---

## Kompilieren

### Windows

1. CMD oder PowerShell öffnen.
2. In den Projektordner wechseln:
    ```bash
    cd Pfad\zum\Projekt
    ```
3. Dokument kompilieren:
    ```bash
    pdflatex dokumentation.tex
    ```
4. Ggf. mehrmals ausführen für Inhaltsverzeichnis etc.

---

### Linux

1. Terminal öffnen.
2. Falls nicht bereits geschehen LaTeX installieren:
    ```bash
    sudo apt install textlive-full
    ```
3. Projektordner öffnen:
    ```bash
    cd /pfad/zu/Projekt
    ```
4. Dokument bauen:
    ```bash
    pdflatex dokumentation.tex
    ```

---