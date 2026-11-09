"""Genera _site/ con el contenido del repo convertido a HTML navegable.

Uso local para leer el repo abriendo los archivos directamente en el
navegador (doble clic, sin servidor). _site/ no se sube a git
(ver .gitignore) -- el contenido fuente de verdad son los .md.
"""

import json
import math
import re
import shutil
from html import escape, unescape
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_site"

# ---------------------------------------------------------------------------
# Iconos brutalistas (SVG a mano, viewBox 0 0 100 100, adaptados al tema vía
# variables CSS). Se usan en la cabecera, el pie de página y las tarjetas.
# ---------------------------------------------------------------------------


def _spiral_points(turns=2.3, steps=70, r_max=42, cx=50, cy=50):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        theta = t * turns * 2 * math.pi
        r = t * r_max
        x = cx + r * math.cos(theta)
        y = cy + r * math.sin(theta)
        pts.append(f"{x:.1f},{y:.1f}")
    return " ".join(pts)


ICONS = {
    "cube": (
        '<polygon points="50,5 90,27.5 90,72.5 50,95 10,72.5 10,27.5" class="icon-stroke" />'
        '<polyline points="50,5 50,50 90,72.5" class="icon-stroke" />'
        '<polyline points="10,72.5 50,50 10,27.5" class="icon-stroke" />'
    ),
    "target": (
        '<circle cx="50" cy="50" r="42" class="icon-stroke" />'
        '<circle cx="50" cy="50" r="26" class="icon-stroke" />'
        '<circle cx="50" cy="50" r="10" class="icon-fill" />'
    ),
    "clover": (
        '<circle cx="50" cy="28" r="22" class="icon-stroke" />'
        '<circle cx="72" cy="50" r="22" class="icon-stroke" />'
        '<circle cx="50" cy="72" r="22" class="icon-stroke" />'
        '<circle cx="28" cy="50" r="22" class="icon-stroke" />'
    ),
    "sparkle": (
        '<path d="M50,4 L61,39 L96,50 L61,61 L50,96 L39,61 L4,50 L39,39 Z" class="icon-fill" />'
    ),
    "spiral": (f'<polyline points="{_spiral_points()}" class="icon-stroke icon-round" />'),
    "arch": (
        '<path d="M20,35 L20,69 A14,14 0 0 1 6,83" class="icon-stroke icon-round" />'
        '<path d="M38,12 L38,69 A14,14 0 0 1 24,83" class="icon-stroke icon-round" />'
        '<path d="M62,12 L62,69 A14,14 0 0 0 76,83" class="icon-stroke icon-round" />'
        '<path d="M80,35 L80,69 A14,14 0 0 0 94,83" class="icon-stroke icon-round" />'
    ),
    "fingerprint": (
        '<path d="M8,92 A42,42 0 0 1 92,92" class="icon-stroke icon-round" />'
        '<path d="M22,92 A28,28 0 0 1 78,92" class="icon-stroke icon-round" />'
        '<path d="M36,92 A14,14 0 0 1 64,92" class="icon-stroke icon-round" />'
    ),
    "stripes": (
        '<line x1="8" y1="38" x2="38" y2="8" class="icon-stroke" />'
        '<line x1="8" y1="60" x2="60" y2="8" class="icon-stroke" />'
        '<line x1="8" y1="82" x2="82" y2="8" class="icon-stroke" />'
        '<line x1="26" y1="92" x2="92" y2="26" class="icon-stroke" />'
        '<line x1="48" y1="92" x2="92" y2="48" class="icon-stroke" />'
    ),
    "bars": (
        '<rect x="8" y="14" width="84" height="13" class="icon-fill" />'
        '<rect x="8" y="34" width="55" height="13" class="icon-fill" />'
        '<rect x="8" y="54" width="84" height="13" class="icon-fill" />'
        '<rect x="8" y="74" width="55" height="13" class="icon-fill" />'
    ),
    "menu": (
        '<line x1="10" y1="22" x2="90" y2="22" class="icon-stroke" />'
        '<line x1="10" y1="50" x2="90" y2="50" class="icon-stroke" />'
        '<line x1="10" y1="78" x2="90" y2="78" class="icon-stroke" />'
    ),
    "close": (
        '<line x1="15" y1="15" x2="85" y2="85" class="icon-stroke" />'
        '<line x1="85" y1="15" x2="15" y2="85" class="icon-stroke" />'
    ),
}

BAND_ICONS = ["stripes", "spiral", "fingerprint", "bars", "clover", "arch", "target", "sparkle", "cube"]


def icon(name: str, cls: str = "") -> str:
    inner = ICONS[name]
    extra = f" {cls}" if cls else ""
    return f'<svg viewBox="0 0 100 100" class="icon icon-{name}{extra}" aria-hidden="true">{inner}</svg>'


def icon_row(count: int) -> str:
    seq = (BAND_ICONS * (count // len(BAND_ICONS) + 1))[:count]
    icons = "".join(f'<span class="band-icon">{icon(name)}</span>' for name in seq)
    return f'<div class="icon-row">{icons}</div>'


def icon_band(count: int, rows: int = 2) -> str:
    row_html = icon_row(count)
    return row_html * rows


# ---------------------------------------------------------------------------
# Menu lateral: panel deslizante con acceso directo a cada seccion, presente
# en todas las paginas (icono de hamburguesa junto al selector de tema).
# ---------------------------------------------------------------------------

MENU_LINKS = [
    ("cube", "Portada", "index.html"),
    ("target", "01 - Fundamentos de economia", "01-fundamentos-economia/README.html"),
    ("spiral", "02 - Portfolio e inversion", "02-portfolio-inversion/README.html"),
    ("sparkle", "03 - Negocio: medicina estetica", "03-negocio-medicina-estetica/README.html"),
    ("arch", "Plan de estudio", "plan-de-estudio.html"),
    ("clover", "Glosario", "01-fundamentos-economia/05-glosario.html"),
]


def side_menu(root_prefix: str) -> str:
    items = []
    for icon_name, label, href in MENU_LINKS:
        items.append(
            f'<a class="side-menu-item" href="{root_prefix}{href}">'
            f"{icon(icon_name)}<span>{escape(label)}</span></a>"
        )
    return f"""<div class="side-menu-backdrop" id="sideMenuBackdrop"></div>
<nav class="side-menu" id="sideMenu" aria-label="Menu de navegacion">
  <div class="side-menu-head">
    <span class="side-menu-title">Indice</span>
    <button class="menu-toggle" id="sideMenuClose" type="button" aria-label="Cerrar menu">{icon("close")}</button>
  </div>
  {"".join(items)}
</nav>"""


# ---------------------------------------------------------------------------
# Collage de fondo: fragmentos recortados de las imagenes, atenuados y en
# escala de grises como una pagina de revista, dispersos detras del
# contenido, fijada en pantalla mientras se hace scroll (inspirado en
# webdesign.kernjosh.com, en clave brutalista: sombra dura siguiendo la
# silueta en vez de tarjeta con borde).
# ---------------------------------------------------------------------------

# Cada pieza: archivo, alt, posicion inicial (agrupada al centro) y final
# (dispersa), como (sx, sy, sr) -> (ex, ey, er) en % / grados, mas el ancho.
SCATTER_ITEMS = [
    ("hero-puno-billetes-l.png", "Puno con billetes", 46, 40, -15, 2, 66, -6, 200),
    ("monedas-engranajes.png", "Engranajes", 54, 48, 12, 9, 4, 4, 190),
    ("hero-saco-dinero.png", "Saco de dinero", 44, 52, -8, 17, 58, -3, 230),
    ("vintage-naranja.png", "Naranja en collage", 56, 42, 15, 25, 80, 6, 160),
    ("arte-cara-sombrero.png", "Retrato en collage", 50, 46, 6, 30, 12, 5, 180),
    ("hero-globo-pulgar.png", "Pulgar arriba", 58, 38, -12, 39, 74, -4, 200),
    ("hero-planta-moneda.png", "Planta de monedas", 42, 44, 9, 46, 28, -3, 180),
    ("arq-edificio-tira.png", "Arquitectura brutalista", 48, 54, -5, 54, 4, 2, 250),
    ("vintage-pajaro-telefono.png", "Collage vintage", 53, 36, 16, 62, 50, -5, 230),
    ("monedas-pila.png", "Pila de monedas", 45, 40, -14, 72, 16, 3, 190),
    ("hero-mano-billetes-r.png", "Mano con billetes", 57, 50, 7, 84, 60, -2, 210),
    ("arq-sol.png", "Sol geometrico", 50, 44, -7, 93, 4, 4, 180),
]


# Subconjuntos mas pequenos para la cabecera de cada seccion (mismo
# mecanismo, menos piezas y menos recorrido de scroll).
SECTION_SCATTER = {
    "01-fundamentos-economia": [
        ("monedas-engranajes.png", "Engranajes", 46, 45, 10, 6, 66, -5, 170),
        ("monedas-pila.png", "Pila de monedas", 54, 50, -8, 20, 8, 4, 160),
        ("arq-sol.png", "Sol geometrico", 48, 42, 12, 50, 70, -6, 150),
        ("hero-planta-moneda.png", "Planta de monedas", 52, 55, -10, 85, 20, 5, 160),
    ],
    "02-portfolio-inversion": [
        ("hero-saco-dinero.png", "Saco de dinero", 48, 48, -9, 8, 55, -4, 200),
        ("hero-puno-billetes-l.png", "Puno con billetes", 54, 42, 11, 35, 10, 5, 170),
        ("hero-mano-billetes-r.png", "Mano con billetes", 46, 52, -12, 58, 70, -3, 180),
        ("monedas-pila.png", "Pila de monedas", 52, 46, 8, 88, 30, 4, 160),
    ],
    "03-negocio-medicina-estetica": [
        ("arte-cara-sombrero.png", "Retrato en collage", 48, 46, 9, 8, 60, -5, 160),
        ("vintage-pajaro-telefono.png", "Collage vintage", 54, 52, -11, 38, 8, 5, 190),
        ("arq-edificio-tira.png", "Arquitectura brutalista", 46, 42, 7, 62, 65, -4, 210),
        ("vintage-naranja.png", "Naranja en collage", 52, 50, -8, 88, 15, 4, 140),
    ],
}


def hero_scatter(items=None, track_vh: int = 200) -> str:
    items = items if items is not None else SCATTER_ITEMS
    pieces = []
    for filename, alt, sx, sy, sr, ex, ey, er, width in items:
        data = f'data-sx="{sx}" data-sy="{sy}" data-sr="{sr}" data-ex="{ex}" data-ey="{ey}" data-er="{er}"'
        style = f"left:{sx}%; top:{sy}%; width:{width}px; transform:translate(-50%,-50%) rotate({sr}deg)"
        pieces.append(
            f'<figure class="hero-scatter-piece" {data} style="{style}">'
            f'<img src="assets/img/collage/{filename}" alt="{escape(alt)}" loading="lazy"></figure>'
        )
    return (
        f'<div class="hero-scatter-track" style="height:{track_vh}vh"><div class="hero-scatter-pin">'
        f'<div class="hero-scatter-stage" aria-hidden="true">{"".join(pieces)}</div>'
        "</div></div>"
    )


FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
    "%3Cpolygon points='50,5 90,27.5 90,72.5 50,95 10,72.5 10,27.5' fill='none' stroke='%23111' stroke-width='7'/%3E"
    "%3Cpolyline points='50,5 50,50 90,72.5' fill='none' stroke='%23111' stroke-width='7'/%3E"
    "%3Cpolyline points='10,72.5 50,50 10,27.5' fill='none' stroke='%23111' stroke-width='7'/%3E"
    "%3C/svg%3E"
)

STYLE = """
<style>
  :root {
    color-scheme: light dark;
    --bg: #f7f5ef;
    --bg-alt: #ece8da;
    --ink: #111111;
    --muted: #55534c;
    --accent: #0033ff;
    --accent2: #d64545;
    --accent-ink: #ffffff;
    --bw: 3px;
    --shadow: 8px 8px 0 var(--ink);
    --shadow-sm: 4px 4px 0 var(--ink);
    --font-sans: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
    --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #0d0d0d;
      --bg-alt: #1a1a1a;
      --ink: #f5f5f0;
      --muted: #b5b3aa;
      --accent: #ffd400;
      --accent2: #5fb3ff;
      --accent-ink: #111111;
    }
  }
  :root[data-theme="dark"] {
    --bg: #0d0d0d;
    --bg-alt: #1a1a1a;
    --ink: #f5f5f0;
    --muted: #b5b3aa;
    --accent: #ffd400;
    --accent2: #5fb3ff;
    --accent-ink: #111111;
  }
  :root[data-theme="light"] {
    --bg: #f7f5ef;
    --bg-alt: #ece8da;
    --ink: #111111;
    --muted: #55534c;
    --accent: #0033ff;
    --accent2: #d64545;
    --accent-ink: #ffffff;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; }
  html {
    background-color: var(--bg);
    background-image: radial-gradient(color-mix(in srgb, var(--ink) 16%, transparent) 1.4px, transparent 1.4px);
    background-size: 24px 24px;
    background-attachment: fixed;
  }
  body {
    max-width: 860px; margin: 0 auto; padding: 0 20px 40px;
    font-family: var(--font-sans); line-height: 1.65; font-size: 17px;
    background: transparent; color: var(--ink);
  }

  .icon { width: 1em; height: 1em; display: inline-block; vertical-align: -0.15em; overflow: visible; }
  .icon-stroke { fill: none; stroke: currentColor; stroke-width: 7; }
  .icon-round { stroke-linecap: round; stroke-linejoin: round; }
  .icon-fill { fill: currentColor; stroke: none; }

  .progress { position: fixed; top: 0; left: 0; height: 6px; width: 0%; background: var(--accent); z-index: 30; }

  header.topbar {
    position: sticky; top: 0; z-index: 20; display: flex; align-items: center;
    justify-content: space-between; gap: 12px; padding: 16px 0; margin-bottom: 4px;
    background: var(--bg); border-bottom: var(--bw) solid var(--ink);
  }
  .brand { display: inline-flex; align-items: center; gap: 8px; font-family: var(--font-mono); font-weight: 800; letter-spacing: .04em;
    font-size: .95em; color: var(--ink); text-decoration: none; text-transform: uppercase; }
  .brand .icon { width: 1.3em; height: 1.3em; color: var(--accent); }
  .brand:hover { background: var(--accent); color: var(--accent-ink); }
  .brand:hover .icon { color: var(--accent-ink); }
  .theme-toggle {
    width: 40px; height: 40px; border: var(--bw) solid var(--ink); background: var(--bg-alt);
    cursor: pointer; font-size: 1.1em; box-shadow: var(--shadow-sm); flex: none;
  }
  .theme-toggle:hover { background: var(--accent); color: var(--accent-ink); transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }

  .header-actions { display: flex; gap: 10px; flex: none; }
  .menu-toggle {
    width: 40px; height: 40px; border: var(--bw) solid var(--ink); background: var(--bg-alt);
    cursor: pointer; box-shadow: var(--shadow-sm); flex: none; padding: 9px;
  }
  .menu-toggle .icon { width: 100%; height: 100%; }
  .menu-toggle:hover { background: var(--accent); color: var(--accent-ink); transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }

  .side-menu-backdrop {
    position: fixed; inset: 0; background: rgba(0, 0, 0, .5); z-index: 40;
    opacity: 0; pointer-events: none; transition: opacity .2s ease;
  }
  .side-menu {
    position: fixed; top: 0; right: 0; height: 100%; width: min(320px, 84vw); z-index: 41;
    background: var(--bg); border-left: var(--bw) solid var(--ink); box-shadow: -8px 0 0 rgba(0, 0, 0, .15);
    transform: translateX(100%); transition: transform .25s ease; display: flex; flex-direction: column;
    padding: 16px;
  }
  body.menu-open .side-menu { transform: translateX(0); }
  body.menu-open .side-menu-backdrop { opacity: 1; pointer-events: auto; }
  body.menu-open { overflow: hidden; }
  .side-menu-head { display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; }
  .side-menu-title { font-family: var(--font-mono); font-weight: 800; text-transform: uppercase; letter-spacing: .06em; font-size: .95em; }
  .side-menu-item {
    display: flex; align-items: center; gap: 12px; padding: 14px 12px; margin-bottom: 10px;
    border: 2px solid var(--ink); background: var(--bg-alt); color: var(--ink); text-decoration: none;
    font-family: var(--font-mono); font-weight: 700; font-size: .88em; text-transform: uppercase;
    letter-spacing: .02em; transition: transform .12s ease, box-shadow .12s ease, background .12s ease;
  }
  .side-menu-item .icon { width: 22px; height: 22px; color: var(--accent); flex: none; }
  .side-menu-item:hover { background: var(--accent); color: var(--accent-ink); transform: translate(-3px, -3px); box-shadow: var(--shadow-sm); }
  .side-menu-item:hover .icon { color: var(--accent-ink); }

  nav.crumb {
    display: flex; flex-wrap: wrap; align-items: center; gap: 6px;
    font-family: var(--font-mono); font-size: .8em; text-transform: uppercase;
    letter-spacing: .03em; margin: 18px 0 6px; color: var(--muted);
  }
  nav.crumb a { color: var(--ink); border-bottom: 2px solid var(--accent); text-decoration: none; padding-bottom: 1px; }
  nav.crumb a:hover { background: var(--accent); color: var(--accent-ink); }

  main.content { padding-top: 10px; position: relative; }

  .hero-scatter-track { position: relative; height: 200vh; margin: 4px 0 20px; }
  .hero-scatter-pin { position: sticky; top: 0; height: 100vh; overflow: hidden; }
  .hero-scatter-stage { position: relative; width: 100%; height: 100%; }
  .hero-scatter-piece { position: absolute; margin: 0; will-change: left, top, transform; }
  .hero-scatter-piece img {
    display: block; width: 100%; height: auto;
    filter: drop-shadow(5px 5px 0 var(--ink));
  }
  @media (max-width: 600px) {
    .hero-scatter-piece { width: 32vw !important; }
    .hero-scatter-track { height: 160vh; }
  }

  h1 { font-size: 2.3em; font-weight: 900; text-transform: uppercase; letter-spacing: -.01em;
    line-height: 1.05; border-bottom: var(--bw) solid var(--ink); padding-bottom: .35em; margin: .6em 0 .7em; }
  h2 { font-size: 1.45em; font-weight: 800; text-transform: uppercase; margin-top: 2em;
    padding-left: 12px; border-left: 8px solid var(--accent); }
  h3 { font-size: 1.12em; font-weight: 700; margin-top: 1.6em; }

  .rotate-word {
    display: inline-block; background: var(--accent); color: var(--accent-ink);
    padding: 0 .22em; font-weight: 800; transition: opacity .25s ease, transform .25s ease;
  }
  .rotate-word.swap { opacity: 0; transform: translateY(-6px); }

  a { color: var(--ink); text-decoration: underline; text-decoration-color: var(--accent);
    text-decoration-thickness: 2px; text-underline-offset: 2px; }
  a:hover { background: var(--accent); color: var(--accent-ink); text-decoration: none; }

  code { font-family: var(--font-mono); background: var(--bg-alt); border: 2px solid var(--ink); padding: .1em .4em; font-size: .88em; }
  pre { font-family: var(--font-mono); background: var(--bg-alt); border: var(--bw) solid var(--ink);
    box-shadow: var(--shadow-sm); padding: 16px; overflow-x: auto; }
  pre code { border: none; padding: 0; background: none; }

  table { border-collapse: collapse; width: 100%; margin: 1.4em 0; border: var(--bw) solid var(--ink); }
  th, td { border: 2px solid var(--ink); padding: 10px 12px; text-align: left; }
  th { background: var(--ink); color: var(--bg); text-transform: uppercase; font-size: .85em; letter-spacing: .03em; }
  tr:nth-child(even) td { background: var(--bg-alt); }
  table { display: block; overflow-x: auto; }

  .content img { max-width: 100%; display: block; height: auto; margin: 1.8em auto; border: var(--bw) solid var(--ink); box-shadow: var(--shadow); }
  .content img + em { display: block; text-align: center; margin-top: -1.3em; margin-bottom: 1.8em; font-size: .82em; color: var(--muted); font-family: var(--font-mono); }

  blockquote { border-left: 8px solid var(--accent); margin: 1.4em 0; padding: .3em 1.2em; background: var(--bg-alt); }
  hr { border: none; border-top: var(--bw) solid var(--ink); margin: 2.4em 0; }

  .content ul, .content ol { list-style: none; padding-left: 0; margin: 1em 0; }
  .content li { position: relative; padding: 12px 14px 12px 44px; margin-bottom: 8px; border: 2px solid var(--ink); background: var(--bg-alt); }
  .content ol { counter-reset: item; }
  .content ol > li { counter-increment: item; }
  .content ol > li::before { content: counter(item, decimal-leading-zero); position: absolute; left: 12px; top: 12px; font-family: var(--font-mono); font-weight: 800; }
  .content ul > li::before { content: "\\2192"; position: absolute; left: 16px; top: 10px; color: var(--accent); font-weight: 800; }
  .content li:has(a):hover { background: var(--accent); }
  .content li:has(a):hover a { color: var(--accent-ink); background: none; }
  .content li > ul, .content li > ol { margin-top: 10px; }

  details.toc { border: var(--bw) solid var(--ink); background: var(--bg-alt); margin: 0 0 2em; box-shadow: var(--shadow-sm); }
  details.toc summary { cursor: pointer; padding: 12px 16px; font-weight: 800; text-transform: uppercase;
    letter-spacing: .03em; font-size: .82em; list-style: none; }
  details.toc summary::-webkit-details-marker { display: none; }
  details.toc summary::before { content: "\\25B8  "; color: var(--accent); }
  details.toc[open] summary::before { content: "\\25BE  "; }
  details.toc ul { list-style: none; margin: 0; padding: 0 16px 4px; }
  details.toc li { border: none; background: none; padding: 4px 0 4px 14px; margin: 0; }
  details.toc li.h3 { padding-left: 30px; font-size: .92em; opacity: .85; }
  details.toc li::before { display: none; }
  details.toc a { text-decoration: none; border-bottom: 2px solid transparent; }
  details.toc a:hover { background: none; color: var(--accent); border-bottom-color: var(--accent); }
  .toc-actions { display: flex; gap: 8px; padding: 4px 16px 14px; }
  .toc-actions button {
    font-family: var(--font-mono); font-size: .72em; text-transform: uppercase; font-weight: 800;
    border: 2px solid var(--ink); background: var(--bg); color: var(--ink); padding: 6px 10px; cursor: pointer;
  }
  .toc-actions button:hover { background: var(--accent); color: var(--accent-ink); }

  details.section { margin: 0; }
  details.section > summary {
    cursor: pointer; list-style: none; display: flex; align-items: baseline; justify-content: space-between; gap: 10px;
    font-size: 1.45em; font-weight: 800; text-transform: uppercase; margin-top: 2em;
    padding: 2px 10px 2px 12px; border-left: 8px solid var(--accent);
  }
  details.section > summary::-webkit-details-marker { display: none; }
  details.section > summary::after {
    content: "\\25BE"; font-size: .55em; color: var(--accent); flex: none; transition: transform .15s ease;
  }
  details.section:not([open]) > summary::after { transform: rotate(-90deg); }
  details.section > summary:hover { background: var(--bg-alt); }
  .section-body { padding-top: .2em; }

  .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 20px; margin: 28px 0 36px; }
  .card { display: flex; flex-direction: column; gap: 8px; padding: 22px; border: var(--bw) solid var(--ink);
    background: var(--bg-alt); box-shadow: var(--shadow); text-decoration: none; color: var(--ink);
    transition: transform .12s ease, box-shadow .12s ease, background .12s ease, color .12s ease; }
  .card:hover { transform: translate(-4px, -4px); box-shadow: 12px 12px 0 var(--ink); background: var(--accent); color: var(--accent-ink); }
  .card-top { display: flex; align-items: center; justify-content: space-between; }
  .card-num { font-family: var(--font-mono); font-size: 2.4em; font-weight: 900; line-height: 1; }
  .card-top .icon { width: 2em; height: 2em; color: var(--accent); }
  .card:hover .icon { color: var(--accent-ink); }
  .card-title { font-size: 1.1em; font-weight: 800; text-transform: uppercase; letter-spacing: .02em; }
  .card-desc { font-size: .92em; opacity: .88; line-height: 1.5; }

  .chart { margin: 1.6em 0; padding: 18px; border: var(--bw) solid var(--ink); background: var(--bg-alt); box-shadow: var(--shadow-sm); }
  .chart figcaption { font-family: var(--font-mono); font-weight: 800; text-transform: uppercase; font-size: .82em;
    letter-spacing: .03em; margin-bottom: 12px; }
  .chart-svg { width: 100%; height: auto; display: block; overflow: visible; }
  .chart-axis { stroke: var(--ink); stroke-width: 2; }
  .chart-grid { stroke: var(--ink); stroke-width: 1; opacity: .15; }
  .chart-label { fill: var(--ink); font-family: var(--font-mono); font-size: 12px; font-weight: 700; }
  .chart-label-sm { font-size: 10px; font-weight: 600; opacity: .75; }
  .chart-value { fill: var(--ink); font-family: var(--font-mono); font-size: 12px; font-weight: 800; }
  .chart-bar { fill: var(--accent); stroke: var(--ink); stroke-width: 2; transition: fill .1s ease; }
  .chart-bar:hover { fill: var(--ink); }
  .chart-line-0 { stroke: var(--accent); stroke-width: 3; }
  .chart-line-1 { stroke: var(--accent2); stroke-width: 3; }
  .chart-dot-0 { fill: var(--accent); stroke: var(--bg-alt); stroke-width: 2; }
  .chart-dot-1 { fill: var(--accent2); stroke: var(--bg-alt); stroke-width: 2; }
  .chart-seg-0 { fill: var(--accent); }
  .chart-seg-1 { fill: var(--accent2); }
  .chart-seg-2 { fill: var(--ink); }
  .chart-seg-3 { fill: var(--muted); }
  .chart-stacked rect { stroke: var(--bg-alt); stroke-width: 3; }
  .chart-legend { display: flex; flex-wrap: wrap; gap: 6px 16px; margin-top: 10px; font-family: var(--font-mono); font-size: .78em; }
  .chart-legend-item { display: inline-flex; align-items: center; gap: 6px; }
  .chart-swatch { width: 12px; height: 12px; display: inline-block; border: 2px solid var(--ink); background: var(--accent); }
  .chart-swatch.chart-swatch-0, .chart-swatch.chart-seg-0 { background: var(--accent); }
  .chart-swatch.chart-swatch-1, .chart-swatch.chart-seg-1 { background: var(--accent2); }
  .chart-swatch.chart-seg-2 { background: var(--ink); }
  .chart-swatch.chart-seg-3 { background: var(--muted); }

  .calc { margin: 1.6em 0; padding: 20px; border: var(--bw) solid var(--ink); background: var(--bg-alt); box-shadow: var(--shadow); }
  .calc-title { font-family: var(--font-mono); font-weight: 800; text-transform: uppercase; font-size: .85em; margin-bottom: 14px; }
  .calc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin-bottom: 16px; }
  .calc-field label { display: block; font-family: var(--font-mono); font-size: .72em; text-transform: uppercase; font-weight: 700; margin-bottom: 4px; opacity: .8; }
  .calc-field input { width: 100%; font-family: var(--font-mono); font-size: 1em; padding: 8px 10px; border: 2px solid var(--ink); background: var(--bg); color: var(--ink); }
  .calc-field input:focus { outline: 3px solid var(--accent); outline-offset: 1px; }
  .calc-result { display: flex; flex-wrap: wrap; gap: 24px; padding-top: 14px; border-top: 2px dashed var(--ink); }
  .calc-stat .num { font-family: var(--font-mono); font-weight: 900; font-size: 1.6em; }
  .calc-stat .lbl { font-family: var(--font-mono); font-size: .72em; text-transform: uppercase; opacity: .75; }

  .glossary-filter { margin-bottom: 1.4em; }
  .glossary-filter input { width: 100%; font-family: var(--font-mono); font-size: 1em; padding: 12px 14px;
    border: var(--bw) solid var(--ink); background: var(--bg-alt); color: var(--ink); box-shadow: var(--shadow-sm); }
  .glossary-filter input:focus { outline: 3px solid var(--accent); outline-offset: 1px; }
  .glossary-empty { display: none; padding: 14px; border: 2px dashed var(--ink); font-family: var(--font-mono); font-size: .85em; }

  footer.sitefoot {
    position: relative; overflow: hidden; margin-top: 60px; padding: 34px 0 18px; min-height: 130px;
    border-top: var(--bw) solid var(--ink);
    display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;
  }
  .icon-band {
    position: absolute; inset: 0; z-index: 0; display: flex; flex-direction: column;
    justify-content: space-evenly; align-items: center; gap: 8px; pointer-events: none;
  }
  .icon-row { display: flex; justify-content: space-evenly; align-items: center; width: 100%; gap: 10px; }
  .icon-row .band-icon { display: inline-flex; flex: none; width: 26px; height: 26px; }
  .icon-row .icon { width: 100%; height: 100%; color: var(--ink); opacity: .16; }
  footer.sitefoot .foot-brand, footer.sitefoot .foot-note {
    position: relative; z-index: 1; background: var(--bg); padding: 2px 14px;
  }
  footer.sitefoot .foot-brand { font-family: var(--font-mono); font-weight: 800; text-transform: uppercase; letter-spacing: .06em; font-size: .85em; }
  footer.sitefoot .foot-note { font-family: var(--font-mono); font-size: .72em; color: var(--muted); margin-top: 2px; }

  .top-btn {
    position: fixed; right: 20px; bottom: 20px; width: 46px; height: 46px; border: var(--bw) solid var(--ink);
    background: var(--bg-alt); font-size: 1.3em; cursor: pointer; opacity: 0; pointer-events: none;
    transform: translateY(10px); transition: opacity .15s ease, transform .15s ease; box-shadow: var(--shadow-sm); z-index: 20;
  }
  .top-btn.show { opacity: 1; pointer-events: auto; transform: none; }
  .top-btn:hover { background: var(--accent); color: var(--accent-ink); }

  @media (max-width: 480px) {
    h1 { font-size: 1.8em; }
    .cards { grid-template-columns: 1fr; }
    details.section > summary { font-size: 1.2em; }
  }
</style>
"""

SCRIPT = """
<script>
(function () {
  var root = document.documentElement;
  try {
    var stored = localStorage.getItem('lf-theme');
    if (stored) root.setAttribute('data-theme', stored);
  } catch (e) {}

  function current() {
    var attr = root.getAttribute('data-theme');
    if (attr) return attr;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  var btn = document.getElementById('themeToggle');
  function updateBtn() { if (btn) btn.textContent = current() === 'dark' ? '\\u2600' : '\\u25CF'; }
  updateBtn();
  if (btn) btn.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('lf-theme', next); } catch (e) {}
    updateBtn();
  });

  var menuOpenBtn = document.getElementById('sideMenuOpen');
  var menuCloseBtn = document.getElementById('sideMenuClose');
  var menuBackdrop = document.getElementById('sideMenuBackdrop');
  function setMenu(open) {
    document.body.classList.toggle('menu-open', open);
    if (menuOpenBtn) menuOpenBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (menuOpenBtn) menuOpenBtn.addEventListener('click', function () { setMenu(true); });
  if (menuCloseBtn) menuCloseBtn.addEventListener('click', function () { setMenu(false); });
  if (menuBackdrop) menuBackdrop.addEventListener('click', function () { setMenu(false); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') setMenu(false);
  });

  var bar = document.getElementById('progress');
  var topBtn = document.getElementById('topBtn');
  function onScroll() {
    var h = document.documentElement;
    var scrolled = h.scrollTop || document.body.scrollTop;
    var height = (h.scrollHeight || document.body.scrollHeight) - h.clientHeight;
    var pct = height > 0 ? (scrolled / height) * 100 : 0;
    if (bar) bar.style.width = pct + '%';
    if (topBtn) { if (scrolled > 400) topBtn.classList.add('show'); else topBtn.classList.remove('show'); }
  }
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  if (topBtn) topBtn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });

  document.querySelectorAll('.content a[href^="http"]').forEach(function (a) {
    a.setAttribute('target', '_blank');
    a.setAttribute('rel', 'noopener');
  });

  var content = document.querySelector('.content');
  var headings = content ? content.querySelectorAll('summary[id], h3[id]') : [];
  if (headings.length > 2) {
    var toc = document.createElement('details');
    toc.className = 'toc';
    toc.open = true;
    var summary = document.createElement('summary');
    summary.textContent = 'En esta pagina (' + headings.length + ')';
    toc.appendChild(summary);
    var list = document.createElement('ul');
    headings.forEach(function (h, i) {
      if (!h.id) h.id = 'sec-' + i;
      var li = document.createElement('li');
      li.className = h.tagName.toLowerCase() === 'h3' ? 'h3' : 'h2';
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      li.appendChild(a);
      list.appendChild(li);
    });
    toc.appendChild(list);

    var sections = content.querySelectorAll('details.section');
    if (sections.length > 1) {
      var actions = document.createElement('div');
      actions.className = 'toc-actions';
      var expandBtn = document.createElement('button');
      expandBtn.type = 'button';
      expandBtn.textContent = 'Expandir todo';
      expandBtn.addEventListener('click', function () {
        sections.forEach(function (s) { s.open = true; });
      });
      var collapseBtn = document.createElement('button');
      collapseBtn.type = 'button';
      collapseBtn.textContent = 'Colapsar todo';
      collapseBtn.addEventListener('click', function () {
        sections.forEach(function (s) { s.open = false; });
      });
      actions.appendChild(expandBtn);
      actions.appendChild(collapseBtn);
      toc.appendChild(actions);
    }

    content.insertBefore(toc, content.firstChild);
  }

  var filterInput = document.getElementById('glossaryFilter');
  if (filterInput) {
    var items = Array.prototype.slice.call(document.querySelectorAll('.content li'));
    var empty = document.getElementById('glossaryEmpty');
    filterInput.addEventListener('input', function () {
      var q = filterInput.value.trim().toLowerCase();
      var visible = 0;
      items.forEach(function (li) {
        var match = !q || li.textContent.toLowerCase().indexOf(q) !== -1;
        li.hidden = !match;
        if (match) visible++;
      });
      if (empty) empty.style.display = visible === 0 ? 'block' : 'none';
    });
  }

  document.querySelectorAll('.calc').forEach(function (calc) {
    var principal = calc.querySelector('[data-role="principal"]');
    var monthly = calc.querySelector('[data-role="monthly"]');
    var rate = calc.querySelector('[data-role="rate"]');
    var years = calc.querySelector('[data-role="years"]');
    var outTotal = calc.querySelector('[data-role="out-total"]');
    var outContrib = calc.querySelector('[data-role="out-contrib"]');
    var outGain = calc.querySelector('[data-role="out-gain"]');
    if (!principal || !outTotal) return;
    function fmt(n) {
      return Math.round(n).toLocaleString('es-ES') + '\\u20ac';
    }
    function recalc() {
      var p = parseFloat(principal.value) || 0;
      var m = parseFloat(monthly.value) || 0;
      var r = (parseFloat(rate.value) || 0) / 100;
      var y = parseFloat(years.value) || 0;
      var months = Math.round(y * 12);
      var monthlyRate = r / 12;
      var value = p;
      var contributed = p;
      for (var i = 0; i < months; i++) {
        value = value * (1 + monthlyRate) + m;
        contributed += m;
      }
      outTotal.textContent = fmt(value);
      outContrib.textContent = fmt(contributed);
      outGain.textContent = fmt(value - contributed);
    }
    [principal, monthly, rate, years].forEach(function (el) {
      if (el) el.addEventListener('input', recalc);
    });
    recalc();
  });

  var rotateWord = document.querySelector('.rotate-word');
  if (rotateWord) {
    var rwWords = rotateWord.getAttribute('data-words').split(',');
    var rwIdx = 0;
    setInterval(function () {
      rotateWord.classList.add('swap');
      setTimeout(function () {
        rwIdx = (rwIdx + 1) % rwWords.length;
        rotateWord.textContent = rwWords[rwIdx];
        rotateWord.classList.remove('swap');
      }, 250);
    }, 2200);
  }

  var scatterTrack = document.querySelector('.hero-scatter-track');
  if (scatterTrack) {
    var scatterPieces = Array.prototype.slice.call(scatterTrack.querySelectorAll('.hero-scatter-piece'));
    var scatterTicking = false;
    function easeInOut(t) { return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; }
    function updateScatter() {
      scatterTicking = false;
      var rect = scatterTrack.getBoundingClientRect();
      var scrollable = rect.height - window.innerHeight;
      var progress = scrollable > 0 ? Math.min(1, Math.max(0, -rect.top / scrollable)) : 0;
      var eased = easeInOut(progress);
      scatterPieces.forEach(function (p) {
        var sx = parseFloat(p.dataset.sx), sy = parseFloat(p.dataset.sy), sr = parseFloat(p.dataset.sr);
        var ex = parseFloat(p.dataset.ex), ey = parseFloat(p.dataset.ey), er = parseFloat(p.dataset.er);
        var x = sx + (ex - sx) * eased;
        var y = sy + (ey - sy) * eased;
        var r = sr + (er - sr) * eased;
        p.style.left = x + '%';
        p.style.top = y + '%';
        p.style.transform = 'translate(-50%,-50%) rotate(' + r + 'deg)';
      });
    }
    function onScatterScroll() {
      if (!scatterTicking) { requestAnimationFrame(updateScatter); scatterTicking = true; }
    }
    window.addEventListener('scroll', onScatterScroll, { passive: true });
    window.addEventListener('resize', onScatterScroll);
    updateScatter();
  }
})();
</script>
"""

MD_FILES = sorted(ROOT.rglob("*.md"))

CARD_PATTERN = re.compile(r'<h2[^>]*><a href="([^"]+)">(.*?)</a></h2>\s*<p>(.*?)</p>', re.DOTALL)
CARD_GROUP_PATTERN = re.compile(r'(?:\s*<a class="card"[^>]*>.*?</a>)+', re.DOTALL)
CARD_ICONS = ["target", "cube", "sparkle", "clover", "spiral", "arch"]


def make_card(index_box: list):
    def _make(match: re.Match) -> str:
        href, title, desc = match.group(1), match.group(2), match.group(3)
        num_match = re.match(r"^(\d+)\s*[—-]\s*(.*)$", title)
        if num_match:
            num, label = num_match.group(1), num_match.group(2)
        else:
            num, label = "", title
        icon_name = CARD_ICONS[index_box[0] % len(CARD_ICONS)]
        index_box[0] += 1
        return (
            f'<a class="card" href="{href}">'
            f'<span class="card-top"><span class="card-num">{num}</span>{icon(icon_name)}</span>'
            f'<span class="card-title">{label}</span>'
            f'<span class="card-desc">{desc}</span>'
            "</a>"
        )

    return _make


def wrap_cards(html: str) -> str:
    html, count = CARD_PATTERN.subn(make_card([0]), html)
    if not count:
        return html
    return CARD_GROUP_PATTERN.sub(lambda m: f'<div class="cards">{m.group(0)}</div>', html, count=1)


H2_RE = re.compile(r'<h2 id="([^"]*)">(.*?)</h2>', re.DOTALL)


def wrap_sections_as_details(html: str) -> str:
    """Turn each H2 section into a collapsible <details open> block so long
    pages can be collapsed section by section, without changing the default
    (fully expanded) reading view."""
    matches = list(H2_RE.finditer(html))
    if not matches:
        return html
    parts = [html[: matches[0].start()]]
    for i, m in enumerate(matches):
        section_id, heading_html = m.group(1), m.group(2)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(html)
        body = html[start:end]
        parts.append(
            f'<details class="section" open><summary id="{section_id}">{heading_html}</summary>'
            f'<div class="section-body">{body}</div></details>'
        )
    return "".join(parts)


# ---------------------------------------------------------------------------
# Gráficas: bloques ```chart con JSON, convertidos a SVG en el propio build.
# ---------------------------------------------------------------------------

CHART_RE = re.compile(r'<pre><code class="language-chart">(.*?)</code></pre>', re.DOTALL)


def render_bar_chart(title: str, unit: str, data: dict) -> str:
    labels = list(data.keys())
    values = [float(v) for v in data.values()]
    max_abs = max((abs(v) for v in values), default=1) or 1
    row_h = 42
    top_pad = 6
    width = 640
    label_w = 190
    plot_w = width - label_w - 80
    height = top_pad * 2 + row_h * len(labels)
    rows = []
    for i, (label, value) in enumerate(zip(labels, values)):
        y = top_pad + i * row_h
        bar_w = max(3, (abs(value) / max_abs) * plot_w)
        val_text = f"{value:g}{unit}"
        rows.append(
            f'<text x="{label_w - 10}" y="{y + row_h / 2 + 5:.1f}" text-anchor="end" class="chart-label">{escape(label)}</text>'
            f'<rect x="{label_w}" y="{y + 7}" width="{bar_w:.1f}" height="{row_h - 14}" class="chart-bar">'
            f"<title>{escape(label)}: {escape(val_text)}</title></rect>"
            f'<text x="{label_w + bar_w + 10:.1f}" y="{y + row_h / 2 + 5:.1f}" class="chart-value">{val_text}</text>'
        )
    svg = f'<svg viewBox="0 0 {width} {height}" class="chart-svg" role="img" aria-label="{escape(title)}">{"".join(rows)}</svg>'
    return f"<figure class=\"chart\"><figcaption>{escape(title)}</figcaption>{svg}</figure>"


def render_stacked_chart(title: str, unit: str, data: dict) -> str:
    width, height = 640, 56
    total = sum(float(v) for v in data.values()) or 1
    x = 0.0
    segs, legend = [], []
    for i, (label, raw_value) in enumerate(data.items()):
        value = float(raw_value)
        w = (value / total) * width
        cls = f"chart-seg-{i % 4}"
        pct = value / total * 100
        segs.append(
            f'<rect x="{x:.1f}" y="0" width="{w:.1f}" height="{height}" class="{cls}">'
            f"<title>{escape(label)}: {value:g}{unit} ({pct:.0f}%)</title></rect>"
        )
        legend.append(
            f'<span class="chart-legend-item"><i class="chart-swatch {cls}"></i>'
            f"{escape(label)}: {value:g}{unit} ({pct:.0f}%)</span>"
        )
        x += w
    svg = (
        f'<svg viewBox="0 0 {width} {height}" class="chart-svg chart-stacked" '
        f'role="img" aria-label="{escape(title)}">{"".join(segs)}</svg>'
    )
    return f'<figure class="chart"><figcaption>{escape(title)}</figcaption>{svg}<div class="chart-legend">{"".join(legend)}</div></figure>'


def render_line_chart(title: str, unit: str, labels: list, series: dict) -> str:
    width, height = 640, 300
    margin_l, margin_r, margin_t, margin_b = 66, 16, 16, 34
    plot_w = width - margin_l - margin_r
    plot_h = height - margin_t - margin_b
    all_vals = [float(v) for vals in series.values() for v in vals]
    vmin, vmax = min(all_vals), max(all_vals)
    if vmin == vmax:
        vmin -= 1
        vmax += 1
    pad = (vmax - vmin) * 0.12
    vmin -= pad
    vmax += pad
    n = len(labels)

    def x_of(i):
        return margin_l + ((i / (n - 1)) if n > 1 else 0) * plot_w

    def y_of(v):
        return margin_t + (1 - (v - vmin) / (vmax - vmin)) * plot_h

    parts = []
    for t in range(5):
        val = vmin + (vmax - vmin) * t / 4
        y = y_of(val)
        parts.append(f'<line x1="{margin_l}" y1="{y:.1f}" x2="{width - margin_r}" y2="{y:.1f}" class="chart-grid" />')
        parts.append(
            f'<text x="{margin_l - 8}" y="{y + 4:.1f}" text-anchor="end" class="chart-label chart-label-sm">{val:,.0f}{unit}</text>'
        )
    for i, lab in enumerate(labels):
        parts.append(
            f'<text x="{x_of(i):.1f}" y="{height - margin_b + 18}" text-anchor="middle" class="chart-label chart-label-sm">{escape(str(lab))}</text>'
        )
    for si, (name, vals) in enumerate(series.items()):
        vals = [float(v) for v in vals]
        cls = f"chart-line-{si % 2}"
        pts = " ".join(f"{x_of(i):.1f},{y_of(v):.1f}" for i, v in enumerate(vals))
        parts.append(f'<polyline points="{pts}" fill="none" class="{cls}" />')
        for i, v in enumerate(vals):
            parts.append(
                f'<circle cx="{x_of(i):.1f}" cy="{y_of(v):.1f}" r="4" class="chart-dot-{si % 2}">'
                f"<title>{escape(name)} · {escape(str(labels[i]))}: {v:,.0f}{unit}</title></circle>"
            )
    parts.append(f'<line x1="{margin_l}" y1="{margin_t}" x2="{margin_l}" y2="{height - margin_b}" class="chart-axis" />')
    parts.append(
        f'<line x1="{margin_l}" y1="{height - margin_b}" x2="{width - margin_r}" y2="{height - margin_b}" class="chart-axis" />'
    )

    legend_html = ""
    if len(series) > 1:
        items = "".join(
            f'<span class="chart-legend-item"><i class="chart-swatch chart-swatch-{i % 2}"></i>{escape(name)}</span>'
            for i, name in enumerate(series.keys())
        )
        legend_html = f'<div class="chart-legend">{items}</div>'

    svg = f'<svg viewBox="0 0 {width} {height}" class="chart-svg" role="img" aria-label="{escape(title)}">{"".join(parts)}</svg>'
    return f"<figure class=\"chart\"><figcaption>{escape(title)}</figcaption>{svg}{legend_html}</figure>"


def render_chart(spec: dict) -> str:
    ctype = spec.get("type")
    title = spec.get("title", "")
    unit = spec.get("unit", "")
    try:
        if ctype == "bar":
            return render_bar_chart(title, unit, spec["data"])
        if ctype == "stacked":
            return render_stacked_chart(title, unit, spec["data"])
        if ctype == "line":
            return render_line_chart(title, unit, spec["labels"], spec["series"])
    except (KeyError, ValueError, ZeroDivisionError):
        return ""
    return ""


def replace_charts(html: str) -> str:
    def repl(m):
        raw = unescape(m.group(1))
        try:
            spec = json.loads(raw)
        except ValueError:
            return m.group(0)
        rendered = render_chart(spec)
        return rendered or m.group(0)

    return CHART_RE.sub(repl, html)


CALC_RE = re.compile(r'<pre><code class="language-calc">(.*?)</code></pre>', re.DOTALL)


def render_calc(spec: dict) -> str:
    title = escape(spec.get("title", "Calculadora"))
    principal = spec.get("principal", 0)
    monthly = spec.get("monthly", 0)
    rate = spec.get("rate", 7)
    years = spec.get("years", 10)
    return f"""<div class="calc">
  <div class="calc-title">{title}</div>
  <div class="calc-grid">
    <div class="calc-field"><label>Capital inicial (€)</label><input type="number" data-role="principal" value="{principal}" step="100"></div>
    <div class="calc-field"><label>Aportacion mensual (€)</label><input type="number" data-role="monthly" value="{monthly}" step="10"></div>
    <div class="calc-field"><label>Retorno anual (%)</label><input type="number" data-role="rate" value="{rate}" step="0.5"></div>
    <div class="calc-field"><label>Anos</label><input type="number" data-role="years" value="{years}" step="1"></div>
  </div>
  <div class="calc-result">
    <div class="calc-stat"><div class="num" data-role="out-total">-</div><div class="lbl">Valor final</div></div>
    <div class="calc-stat"><div class="num" data-role="out-contrib">-</div><div class="lbl">Total aportado</div></div>
    <div class="calc-stat"><div class="num" data-role="out-gain">-</div><div class="lbl">Ganancia</div></div>
  </div>
</div>"""


def replace_calcs(html: str) -> str:
    def repl(m):
        raw = unescape(m.group(1))
        try:
            spec = json.loads(raw)
        except ValueError:
            return m.group(0)
        return render_calc(spec)

    return CALC_RE.sub(repl, html)


LIST_ITEM_RE = re.compile(r"^(\s*)([-*+]|\d+\.)\s+")


def ensure_blank_line_before_lists(text: str) -> str:
    """python-markdown (unlike GitHub) needs a blank line before a list
    that follows a paragraph, or it merges the list into the paragraph
    as literal text. Insert one automatically instead of relying on
    every source file getting this exactly right."""
    lines = text.split("\n")
    out = []
    in_list = False
    for line in lines:
        is_blank = line.strip() == ""
        is_item = bool(LIST_ITEM_RE.match(line))
        is_continuation = (not is_item) and (not is_blank) and line[:1] in (" ", "\t") and in_list
        if is_item and not in_list and out and out[-1].strip() != "":
            out.append("")
        out.append(line)
        if is_item or is_continuation:
            in_list = True
        elif not is_blank:
            in_list = False
    return "\n".join(out)


def md_link_to_html(match, current_dir: Path) -> str:
    text, target = match.group(1), match.group(2)
    if target.startswith("http://") or target.startswith("https://") or target.startswith("#"):
        return match.group(0)
    if target.endswith(".md"):
        target = target[:-3] + ".html"
        return f"[{text}]({target})"
    return match.group(0)


def render_file(md_path: Path):
    rel = md_path.relative_to(ROOT)
    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: md_link_to_html(m, md_path.parent), text)
    text = ensure_blank_line_before_lists(text)
    body_html = markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])
    body_html = replace_charts(body_html)
    body_html = replace_calcs(body_html)

    depth = len(rel.parts) - 1
    root_prefix = "../" * depth
    if depth > 0:
        crumb = f'<nav class="crumb"><a href="{root_prefix}index.html">Indice</a> / {rel.parent.as_posix()}</nav>'
    else:
        crumb = ""
        body_html = wrap_cards(body_html)

    is_home = depth == 0 and rel.name == "README.md"
    if is_home:
        rotate_words = ["financiera", "económica", "personal", "profesional", "mental"]
        rotate_html = (
            f'<span class="rotate-word" data-words="{",".join(rotate_words)}">{rotate_words[0]}</span>'
        )
        body_html = body_html.replace("la libertad financiera.", f"la libertad {rotate_html}.", 1)

        marker = '<h2 id="contexto">'
        scatter_html = hero_scatter()
        if marker in body_html:
            body_html = body_html.replace(marker, scatter_html + marker, 1)
        else:
            body_html = re.sub(r"(<h1[^>]*>.*?</h1>)", r"\1" + scatter_html, body_html, count=1, flags=re.DOTALL)

    is_section_home = depth == 1 and rel.name == "README.md" and rel.parts[0] in SECTION_SCATTER
    if is_section_home:
        section_scatter_html = hero_scatter(SECTION_SCATTER[rel.parts[0]], track_vh=130)
        body_html = re.sub(
            r"(<h1[^>]*>.*?</h1>)", r"\1" + section_scatter_html, body_html, count=1, flags=re.DOTALL
        )

    is_glossary = rel.name == "05-glosario.md"
    if is_glossary:
        filter_html = (
            '<div class="glossary-filter">'
            '<input type="text" id="glossaryFilter" placeholder="Buscar un termino...">'
            "</div>"
        )
        body_html = re.sub(r"(<h1[^>]*>.*?</h1>)", r"\1" + filter_html, body_html, count=1, flags=re.DOTALL)

    body_html = wrap_sections_as_details(body_html)

    if is_glossary:
        body_html += '<p id="glossaryEmpty" class="glossary-empty">Ningun termino coincide con la busqueda.</p>'

    h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", body_html, re.DOTALL)
    title = re.sub(r"<[^>]+>", "", h1_match.group(1)).strip() if h1_match else rel.stem
    if is_home:
        title = "Libertad financiera"
    else:
        title = f"{title} | Libertad financiera"
    html = f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="{FAVICON}">
<title>{title}</title>{STYLE}</head><body>
<div class="progress" id="progress"></div>
<header class="topbar">
  <a class="brand" href="{root_prefix}index.html">{icon("cube")}Libertad financiera</a>
  <div class="header-actions">
    <button class="theme-toggle" id="themeToggle" aria-label="Cambiar tema" type="button">&#9679;</button>
    <button class="menu-toggle" id="sideMenuOpen" aria-label="Abrir menu" type="button">{icon("menu")}</button>
  </div>
</header>
{side_menu(root_prefix)}
{crumb}
<main class="content">
{body_html}
</main>
<footer class="sitefoot">
  <div class="icon-band">{icon_band(14)}</div>
  <div class="foot-brand">Libertad financiera</div>
  <div class="foot-note">Documento personal &middot; generado localmente &middot; no es asesoramiento profesional</div>
</footer>
<button class="top-btn" id="topBtn" aria-label="Subir" type="button">&uarr;</button>
{SCRIPT}
</body></html>"""

    out_path = OUT / rel.with_suffix(".html")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")


def copy_assets():
    src = ROOT / "assets"
    if not src.exists():
        return
    dst = OUT / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def main():
    copy_assets()

    for md_path in MD_FILES:
        render_file(md_path)

    root_readme_html = OUT / "README.html"
    index_html = OUT / "index.html"
    if root_readme_html.exists():
        index_html.write_text(root_readme_html.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"Generados {len(MD_FILES)} archivos en {OUT}")


if __name__ == "__main__":
    main()
