# figure-colors

Fixed colour values for engineering figures (curves, maps, contour plots, 3D surfaces, box plots, scatter and parity plots, bar charts). The user picked these values on real data. Each time Claude draws a figure, it loads them from one file instead of choosing new colours.

- Categorical (different data classes): Paul Tol high-contrast `#004488 #DDAA33 #BB5566`, Paul Tol vibrant `#009988 #EE7733 #EE3377`, ordered groups Paul Tol iridescent `#81C4E7 #9398D2 #906388 #46353A`, accent `#C00000`.
- Magnitude (same data class): teal `#FFFFFF -> #628FA2 -> #014460`, light 70 % for 2D maps, five steps `#EAF0F3 #BED0D8 #91B1BE #6591A4 #497B91`, 20 to 85 % with alpha 0.85 for 3D surfaces.
- Rules: how to choose between magnitude, ordered and unordered groups, consistency within one document, exceptions (manuscript figures in greyscale), rejected colours and why.

The values live in `skills/figure-colors/scripts/palette.py`. Run `python palette.py --swatch out.png` to get a swatch. The skill itself (`skills/figure-colors/SKILL.md`) is written in Korean.

Install: see the [repository README](../../README.md).
