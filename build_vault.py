"""Генерирует UPG-раздел в Obsidian vault.

Что делает:
- Копирует *.md из full_versions/, patches/, tools/, project_tools/ в vault/UPG/
- Конвертирует project_tools/*.txt в .md при копировании
- Добавляет навигацию prev/next в full_versions и base-link в patches
- Генерит UPG.canvas — визуальную историю версий
- Обновляет Index.md с Mermaid-диаграммой эволюции

Запуск: python build_vault.py
Идемпотентно — можно гонять сколько угодно раз, старые nav-блоки перезатираются.
"""
import io
import json
import os
import re
import shutil
import sys
import uuid
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SRC = Path(r"M:\projects\UPG")
DST = Path(r"C:\Users\Corkusha\Documents\Obsidian Vault\UPG")

NAV_START = "<!-- upg-nav-begin -->"
NAV_END = "<!-- upg-nav-end -->"


def parse_ver(name: str) -> tuple[int, ...]:
    s = re.sub(r"^(UPG|PATCH)_v", "", name)
    s = re.sub(r" mb$", "", s)
    parts = tuple(int(x) for x in s.split("_"))
    return parts + (0,) * (3 - len(parts)) if len(parts) < 3 else parts


def is_mb(name: str) -> bool:
    return name.endswith(" mb")


def copy_tree():
    for sub in ("full_versions", "patches", "tools", "project_tools"):
        (DST / sub).mkdir(parents=True, exist_ok=True)
    for sub in ("full_versions", "patches", "tools"):
        for p in (SRC / sub).glob("*.md"):
            shutil.copy2(p, DST / sub / p.name)
    for p in (SRC / "project_tools").glob("*.md"):
        shutil.copy2(p, DST / "project_tools" / p.name)
    for p in (SRC / "project_tools").glob("*.txt"):
        shutil.copy2(p, DST / "project_tools" / (p.stem + ".md"))
    readme = SRC / "README.md"
    if readme.exists():
        shutil.copy2(readme, DST / "README.md")


def strip_old_nav(text: str) -> str:
    pattern = re.compile(
        re.escape(NAV_START) + r".*?" + re.escape(NAV_END),
        re.DOTALL,
    )
    return pattern.sub("", text).rstrip() + "\n"


def write_nav(path: Path, block: str) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    text = strip_old_nav(text)
    wrapped = f"\n{NAV_START}\n{block}\n{NAV_END}\n"
    path.write_text(text + wrapped, encoding="utf-8")


def inject_nav():
    fulls = sorted(
        (DST / "full_versions").glob("*.md"),
        key=lambda p: (parse_ver(p.stem), is_mb(p.stem), p.stem),
    )
    for i, cur in enumerate(fulls):
        prev = f"[[{fulls[i-1].stem}]]" if i > 0 else "_начало_"
        nxt = f"[[{fulls[i+1].stem}]]" if i + 1 < len(fulls) else "_конец_"
        block = (
            "## Навигация\n\n"
            f"{prev} ← **{cur.stem}** → {nxt}\n\n"
            "[[Index]] | [[Dashboard]]"
        )
        write_nav(cur, block)

    for p in sorted(
        (DST / "patches").glob("*.md"),
        key=lambda p: parse_ver(p.stem),
    ):
        pv = parse_ver(p.stem)
        base = None
        for f in fulls:
            if is_mb(f.stem):
                continue
            if parse_ver(f.stem) <= pv:
                base = f
        lines = ["## См. также", ""]
        if base:
            lines.append(f"- Базовая версия: [[{base.stem}]]")
        lines.append("- [[Index]]")
        lines.append("- [[Dashboard]]")
        write_nav(p, "\n".join(lines))


def build_canvas():
    fulls = sorted(
        (DST / "full_versions").glob("*.md"),
        key=lambda p: (parse_ver(p.stem), is_mb(p.stem), p.stem),
    )
    patches = sorted(
        (DST / "patches").glob("*.md"),
        key=lambda p: parse_ver(p.stem),
    )

    step_x = 340
    node_w, node_h = 260, 80

    mainline = [f for f in fulls if not is_mb(f.stem)]
    mb_by_base = {}
    for f in fulls:
        if not is_mb(f.stem):
            continue
        twin = f.stem.replace(" mb", "")
        mb_by_base[twin] = f

    x_of = {}
    for i, f in enumerate(mainline):
        x_of[f.stem] = i * step_x

    nodes = []
    edges = []

    def nid():
        return uuid.uuid4().hex[:16]

    node_ids = {}

    COL_FULL = "4"
    COL_MB = "6"
    COL_PATCH = "5"

    for f in mainline:
        i = nid()
        node_ids[f.stem] = i
        nodes.append({
            "id": i,
            "type": "file",
            "file": f"UPG/full_versions/{f.name}",
            "x": x_of[f.stem],
            "y": 0,
            "width": node_w,
            "height": node_h,
            "color": COL_FULL,
        })

    for prev_f, next_f in zip(mainline, mainline[1:]):
        edges.append({
            "id": nid(),
            "fromNode": node_ids[prev_f.stem],
            "fromSide": "right",
            "toNode": node_ids[next_f.stem],
            "toSide": "left",
        })

    for twin_name, mb_file in mb_by_base.items():
        if twin_name not in node_ids:
            continue
        mx = x_of[twin_name]
        i = nid()
        node_ids[mb_file.stem] = i
        nodes.append({
            "id": i,
            "type": "file",
            "file": f"UPG/full_versions/{mb_file.name}",
            "x": mx,
            "y": -220,
            "width": node_w,
            "height": node_h,
            "color": COL_MB,
        })
        edges.append({
            "id": nid(),
            "fromNode": i,
            "fromSide": "bottom",
            "toNode": node_ids[twin_name],
            "toSide": "top",
            "label": "mb",
        })

    patch_stack = {}
    for p in patches:
        pv = parse_ver(p.stem)
        base_stem = None
        for f in mainline:
            if parse_ver(f.stem) <= pv:
                base_stem = f.stem
        if base_stem is None:
            base_stem = mainline[0].stem
        px = x_of.get(base_stem, 0)
        level = patch_stack.get(base_stem, 0)
        patch_stack[base_stem] = level + 1
        py = 160 + level * (node_h + 20)
        i = nid()
        node_ids[p.stem] = i
        nodes.append({
            "id": i,
            "type": "file",
            "file": f"UPG/patches/{p.name}",
            "x": px,
            "y": py,
            "width": node_w,
            "height": node_h,
            "color": COL_PATCH,
        })
        edges.append({
            "id": nid(),
            "fromNode": node_ids[base_stem],
            "fromSide": "bottom",
            "toNode": i,
            "toSide": "top",
        })

    era_y = -400
    eras = [
        ("Era 1.x — Greeting Card PG", 1, 3),
        ("Era 4-6 — Image Prompt Generator", 4, 6),
        ("Era 7-8 — Universal PG (full)", 7, 8),
        ("Era 9.x — UPG short", 9, 9),
        ("Era 10 — current", 10, 10),
    ]
    for label, lo, hi in eras:
        xs = [x_of[f.stem] for f in mainline if lo <= parse_ver(f.stem)[0] <= hi]
        if not xs:
            continue
        mid = (min(xs) + max(xs)) // 2
        width = max(360, max(xs) - min(xs) + node_w)
        nodes.append({
            "id": nid(),
            "type": "text",
            "text": f"### {label}",
            "x": mid - width // 2,
            "y": era_y,
            "width": width,
            "height": 60,
            "color": "1",
        })

    title_node = {
        "id": nid(),
        "type": "text",
        "text": "# UPG — история версий\n\nЗелёные = full versions, фиолетовые = mb (сокращённые), оранжевые = patches.",
        "x": -40,
        "y": -560,
        "width": 560,
        "height": 120,
    }
    nodes.append(title_node)

    canvas = {"nodes": nodes, "edges": edges}
    (DST / "История версий.canvas").write_text(
        json.dumps(canvas, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def update_index_mermaid():
    idx = DST / "Index.md"
    if not idx.exists():
        return
    text = idx.read_text(encoding="utf-8")
    text = strip_old_nav(text)

    fulls = sorted(
        (DST / "full_versions").glob("*.md"),
        key=lambda p: (parse_ver(p.stem), is_mb(p.stem)),
    )
    mainline = [f for f in fulls if not is_mb(f.stem)]
    patches = sorted(
        (DST / "patches").glob("*.md"),
        key=lambda p: parse_ver(p.stem),
    )

    def safe_id(s: str) -> str:
        return re.sub(r"[^A-Za-z0-9]", "_", s)

    lines = ["```mermaid", "graph LR"]
    for f in mainline:
        lines.append(f'    {safe_id(f.stem)}["{f.stem}"]:::full')
    for prev_f, next_f in zip(mainline, mainline[1:]):
        lines.append(f"    {safe_id(prev_f.stem)} --> {safe_id(next_f.stem)}")
    for p in patches:
        pv = parse_ver(p.stem)
        base = None
        for f in mainline:
            if parse_ver(f.stem) <= pv:
                base = f
        if base is None:
            continue
        lines.append(f'    {safe_id(p.stem)}(("{p.stem}")):::patch')
        lines.append(f"    {safe_id(base.stem)} -.-> {safe_id(p.stem)}")
    lines.append("    classDef full fill:#2d5f3f,stroke:#5fbf7f,color:#fff")
    lines.append("    classDef patch fill:#8a4a1e,stroke:#d89560,color:#fff")
    lines.append("```")
    mermaid = "\n".join(lines)

    block = (
        f"\n{NAV_START}\n"
        "## 🕸 Граф эволюции\n\n"
        "Линейная цепочка full-версий (прямые стрелки) + патчи как ответвления (пунктир). "
        "Интерактивная карта — [[История версий.canvas]].\n\n"
        f"{mermaid}\n"
        f"{NAV_END}\n"
    )
    idx.write_text(text + block, encoding="utf-8")


def main():
    copy_tree()
    inject_nav()
    build_canvas()
    update_index_mermaid()
    fulls = len(list((DST / "full_versions").glob("*.md")))
    patches = len(list((DST / "patches").glob("*.md")))
    print(f"UPG vault rebuilt: {fulls} fulls, {patches} patches, canvas + mermaid ok")


if __name__ == "__main__":
    main()
