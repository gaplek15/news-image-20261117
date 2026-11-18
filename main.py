"""THE WORLD — front page for 17 November 2026.

One picture, one day. This script does nothing clever: it hands over the
front page exactly as it was drawn, byte for byte.

What the page holds: the Kerch bridge between Crimea and Russia, hit for a
second day in a row, traffic shut, the span badly damaged — Kyiv called it
an operation without precedent, and Moscow answered by striking bridges
around Kyiv. Far away, an Iranian drone went for an American radar site in
Bahrain and was shot down with no one hurt, while Washington's spies warned
Tehran might be weighing something far dirtier against Trump officials.
Beijing confirmed the first three-way sit-down of Xi, Trump and Putin,
set for Thursday in Shenzhen on the APEC sidelines, as Trump flew into
Manila on his way there. Japan scrambled jets after Russian planes crossed
into its airspace, Estonia said it will seal its Russian border crossings
from 1 December after a bomb plot against a drone factory, and London
sanctioned eight firms building Israeli settlements while a 72-year-old
woman was killed by settlers near Jericho. The West pressed Israel to open
Gaza's crossings, the Houthis pushed on in Yemen, the US lost its measles
elimination status, Microsoft explained a worldwide outage, Depardieu
admitted a sexual assault allegation, and a forensics expert cast doubt on
the Epstein death story. Markets slid, Nvidia stole the spotlight, and oil
was squeezed between Middle East exports and tanker attacks.

The program below copies the bundled front page to the output folder.
No network, no clock, no randomness — the same input always gives the
same output. Deterministic by design: run it twice, get the same file.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # The output directory comes from the harness environment.
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "news.png"
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
