"""Writes svg/hero/<slug>.svg — the 'live screen' graphic for each product page (700 x 290),
plus svg/cover-map.svg. Chats and screens are illustrations and carry an EXAMPLE tag;
the only real numbers drawn here are measured ones from Part A (0.91 s, 82/100, 27/27, 92, 100, 11)."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kit import (C, DISPLAY, BODY, Doc, t, mono, rect, line, path, circle, bars, tick, chip, button,  # noqa: E402
                 phone, window, bubble, wave, callout, example_tag, arrow, node)

W, H = 700, 290
OUT = Path(__file__).resolve().parent


def lines(x, y, rows, size=9.5, fill=C["ink"], gap=12.5, weight=400, family=BODY, anchor="start"):
    return "".join(t(x, y + i * gap, r, size, fill, family, weight, anchor) for i, r in enumerate(rows))


def thumb(x, y, w, h, color=C["cyan"]):
    """Tiny photo placeholder: frame, sun, hills."""
    return (rect(x, y, w, h, 4, C["bg3"], C["line2"], .8)
            + circle(x + w * .72, y + h * .32, h * .12, C["orange2"], opacity=.9)
            + path(f"M{x + 2} {y + h - 3} L{x + w * .35} {y + h * .45} L{x + w * .55} {y + h * .7} "
                   f"L{x + w * .72} {y + h * .55} L{x + w - 2} {y + h - 3} Z", color, 1, fill=C["bg4"]))


def qr_grid(x, y, cell, n=11, seed=7):
    s = []
    for i in range(n):
        for j in range(n):
            finder = (i < 3 and j < 3) or (i < 3 and j >= n - 3) or (i >= n - 3 and j < 3)
            on = finder or ((i * 7 + j * 13 + seed * (i ^ j)) % 5 < 2)
            if finder and (i in (1,) and j in (1, n - 2) or (i == n - 2 and j == 1)):
                on = False
            if on:
                s.append(rect(x + j * cell, y + i * cell, cell - .6, cell - .6, .6, C["ink"], None))
    return "".join(s)


# ---------------------------------------------------------------- 01
def personal_ai_assistant(d):
    d.halo(350, 150, 260, 150, C["cyan"], .20)
    d.halo(470, 210, 170, 110, C["purple"], .28)
    px, py = 275, 6
    d.add(phone(px, py, 150, 278, C["cyan"]))
    d.add(circle(299, 38, 9, C["cyanDeep"], C["cyan"], 1),
          path("M299 33v10M294 38h10", C["cyan"], 1.2),
          t(314, 36, "Your assistant", 10, C["ink"], DISPLAY, 700),
          mono(314, 47, "online", 9, C["green2"]),
          line(282, 55, 418, 55, C["line"]))
    # morning brief
    d.add(bubble(284, 62, 132, 92, "in"),
          mono(292, 77, "07:30 Briefing", 9, C["cyan"]))
    rows = [("New enquiries", "12", C["ink"]), ("Bookings", "3", C["ink"]),
            ("Follow-ups due", "4", C["orange2"]), ("All systems", "OK", C["green2"])]
    for i, (k, v, col) in enumerate(rows):
        y = 94 + i * 15
        d.add(t(292, y, k, 9.5, C["grey"]), t(408, y, v, 10, col, DISPLAY, 700, "end"))
    # voice note from owner
    d.add(bubble(326, 162, 90, 26, "out"),
          path("M335 170 l7 5 l-7 5 z", C["cyan"], 1.1, fill=C["cyan"]),
          wave(348, 175, 60, 13, 16, C["cyan"], 2, 1.4))
    # approval
    d.add(bubble(284, 196, 132, 70, "in"),
          lines(292, 212, ["Dealer reminder drafted.", "Send it now?"], 9.5),
          button(291, 238, 58, 18, "Approve", "green", size=9.5),
          button(354, 238, 52, 18, "Not now", "ghost", size=9.5))
    d.add(example_tag(314, 268))
    # callouts
    d.add(callout(284, 78, 196, 40, "Morning briefing", "left", sub="on time, every day"),
          callout(326, 175, 196, 150, "Voice notes in", "left", sub="English, Hindi, Hinglish"),
          callout(291, 247, 196, 240, "Asks before anything risky", "left", C["green2"], sub="one tap to approve"),
          callout(416, 95, 504, 52, "Remembers your business", "right", sub="prices, people, rules"),
          callout(416, 130, 504, 128, "Works on a schedule", "right", sub="silent unless something's wrong"),
          callout(416, 228, 504, 204, "Does work in your apps", "right", C["purple"]))
    x = 514
    for lab, col in (("CRM", C["cyan"]), ("Sheets", C["green2"]), ("Gmail", C["orange2"])):
        s, w = chip(x, 222, lab, col)
        d.add(s)
        x += w + 6


# ---------------------------------------------------------------- 02
def whatsapp_connect(d):
    d.halo(360, 150, 230, 140, C["cyan"], .22)
    d.halo(120, 150, 120, 120, C["green"], .14)
    # phone with QR
    d.add(phone(52, 22, 128, 244, C["green2"]),
          mono(116, 62, "Link a device", 9, C["grey"], "middle"),
          rect(74, 74, 84, 84, 6, C["bg2"], C["line2"], .8),
          qr_grid(80, 80, 6.6),
          t(116, 182, "Scan once", 11, C["ink"], DISPLAY, 700, "middle"),
          t(116, 197, "or type an", 9.5, C["grey"], BODY, 400, "middle"),
          t(116, 209, "8-character code", 9.5, C["grey"], BODY, 400, "middle"),
          mono(116, 240, "Same day", 9, C["green2"], "middle"))
    # link to hub
    d.add(arrow(186, 146, 296, 146, C["green2"], 1.3, "4 4"))
    # hub
    d.add(circle(350, 146, 62, C["cyan"], opacity=.06), circle(350, 146, 48, C["bg1"], C["cyan"], 1.4),
          circle(350, 146, 55, "none", C["cyan"], .6, opacity=.4),
          t(350, 142, "Your", 12, C["ink"], DISPLAY, 700, "middle"),
          t(350, 157, "number", 12, C["ink"], DISPLAY, 700, "middle"))
    x = 262
    for lab in ("Sales", "Support", "Branch 2"):
        s, w = chip(x, 222, lab, C["cyan"])
        d.add(s)
        x += w + 8
    d.add(mono(350, 258, "Many numbers, one control room", 9, C["grey"], "middle"))
    # destinations
    dests = [("Team inbox", C["cyan"]), ("AI agent", C["purple"]), ("CRM", C["blue"]), ("Automations", C["orange2"])]
    for i, (lab, col) in enumerate(dests):
        y = 34 + i * 62
        d.add(path(f"M398 146 C 470 146, 470 {y + 18}, 540 {y + 18}", col, 1.1, opacity=.8),
              circle(470, (146 + y + 18) / 2, 2.2, col),
              rect(540, y, 140, 36, 8, C["bg1"], col, 1),
              circle(558, y + 18, 5, col, opacity=.9),
              t(572, y + 22, lab, 11, C["ink"], BODY, 600))
    d.add(mono(610, 282, "Every chat saved", 9, C["grey"], "middle"))


# ---------------------------------------------------------------- 03
def inbox(d):
    d.halo(360, 150, 260, 150, C["blue"], .20)
    x0, y0, w, h = 150, 10, 420, 270
    d.add(window(x0, y0, w, h, "Team inbox"))
    # channels
    chans = [("WhatsApp", C["green2"], "12"), ("Instagram", C["purple"], "5"), ("Facebook", C["blue"], "2"),
             ("Website", C["cyan"], "3"), ("Email", C["grey"], "1")]
    d.add(line(x0 + 100, y0 + 22, x0 + 100, y0 + h, C["line"]))
    for i, (lab, col, n) in enumerate(chans):
        y = y0 + 44 + i * 26
        d.add(circle(x0 + 16, y - 3, 4, col), t(x0 + 26, y, lab, 9.5, C["ink"]),
              t(x0 + 92, y, n, 9.5, C["grey"], DISPLAY, 600, "end"))
    # conversation list
    lx = x0 + 100
    d.add(line(lx + 150, y0 + 22, lx + 150, y0 + h, C["line"]))
    st = [("Open", C["cyan"]), ("Pending", C["orange2"]), ("Open", C["cyan"]), ("Resolved", C["green2"]),
          ("Snoozed", C["grey"])]
    for i, (lab, col) in enumerate(st):
        y = y0 + 30 + i * 46
        if i == 0:
            d.add(rect(lx + 4, y - 2, 142, 42, 6, C["bg3"], C["cyan"], .8))
        d.add(circle(lx + 18, y + 12, 8, C["bg4"], C["line2"], .8), bars(lx + 32, y + 5, [60, 88], 4.5, 11))
        s, _ = chip(lx + 32, y + 22, lab, col, 9, 5, 14)
        d.add(s, circle(lx + 134, y + 10, 6, C["purpleDeep"], C["purple"], .8))
    # thread
    tx = lx + 150
    d.add(rect(tx + 8, y0 + 30, 154, 18, 5, C["cyanDeep"], None),
          mono(tx + 16, y0 + 42, "Priya is replying", 9, C["cyan"]))
    d.add(bubble(tx + 8, y0 + 58, 110, 34, "in"), bars(tx + 16, y0 + 68, [86, 60], 4.5, 11))
    d.add(bubble(tx + 52, y0 + 100, 110, 34, "out"), bars(tx + 60, y0 + 110, [90, 52], 4.5, 11, C["cyan"]))
    d.add(rect(tx + 8, y0 + 144, 154, 42, 8, C["orangeDeep"], C["orange"], .8),
          mono(tx + 16, y0 + 158, "Private note", 9, C["orange2"]),
          t(tx + 16, y0 + 175, "@Priya call not picked", 9.5, C["ink"]))
    d.add(rect(tx + 8, y0 + 230, 154, 26, 13, C["bg2"], C["line2"], .8),
          bars(tx + 20, y0 + 241, [80], 4.5), circle(tx + 150, y0 + 243, 7, C["cyan"]))
    d.add(example_tag(x0 + 14, y0 + h - 26))
    d.add(callout(x0 + 16, y0 + 69, 128, 44, "Every channel", "left", sub="in one list"),
          callout(lx + 134, y0 + 40, 128, 132, "One owner per chat", "left", C["purple"], sub="auto-assigned"),
          callout(lx + 60, y0 + 219, 128, 218, "Clear status", "left", C["green2"], sub="open to resolved"),
          callout(tx + 162, y0 + 39, 588, 44, "Collision alerts", "right"),
          callout(tx + 162, y0 + 165, 588, 160, "Private notes", "right", C["orange2"], sub="@mentions"))


# ---------------------------------------------------------------- 04
def instagram_automation(d):
    d.halo(160, 150, 170, 140, C["purple"], .30)
    d.halo(560, 150, 170, 130, C["orange"], .16)
    # step labels
    for x, lab in ((20, "01 Comment"), (262, "02 DM"), (500, "03 Call + CRM")):
        d.add(mono(x, 14, lab, 9, C["cyan"]))
    # post + comments
    d.add(rect(20, 24, 200, 258, 14, C["bg1"], C["line2"], 1.2),
          rect(30, 34, 180, 92, 8, C["purpleDeep"], None),
          path("M30 110 L80 70 L112 96 L140 76 L210 118", C["purple"], 1.4),
          circle(170, 58, 11, C["orange2"], opacity=.85),
          path("M112 72 l14 9 l-14 9 z", C["ink"], 1, fill=C["ink"], opacity=.8))
    for i, txt in enumerate(("price?", "details pls")):
        y = 140 + i * 30
        d.add(circle(40, y + 9, 7, C["bg4"], C["line2"], .8), bars(52, y + 2, [40], 4),
              t(52, y + 17, txt, 10, C["ink"], BODY, 500))
    d.add(rect(34, 202, 172, 44, 8, C["cyanDeep"], C["cyan"], .8),
          mono(42, 216, "Auto reply", 9, C["cyan"]),
          t(42, 234, "Sent you the details in DM", 9.5, C["ink"]))
    d.add(example_tag(34, 256))
    d.add(arrow(226, 150, 256, 150, C["cyan"], 1.3))
    # DM flow
    d.add(rect(262, 24, 210, 258, 14, C["bg1"], C["line2"], 1.2),
          bubble(274, 38, 150, 28, "in"), bars(282, 48, [120], 4.5), bars(282, 57, [80], 4.5))
    for i in range(3):
        x = 274 + i * 64
        d.add(rect(x, 76, 58, 78, 7, C["bg3"], C["line2"], .8), thumb(x + 4, 80, 50, 34, C["purple"]),
              bars(x + 6, 122, [40, 28], 4, 9), rect(x + 6, 140, 46, 9, 4.5, C["cyanDeep"], C["cyan"], .6))
    x = 274
    for lab in ("2 people", "Dec", "Call me"):
        s, w = chip(x, 166, lab, C["cyan"], 9, 6, 16)
        d.add(s)
        x += w + 5
    d.add(bubble(318, 196, 142, 28, "out"), t(328, 214, "My number: 98•• ••• •••", 9.5, C["ink"]),
          mono(274, 250, "Every DM ends with", 9, C["grey"]), mono(274, 263, "a phone number", 9, C["grey"]))
    d.add(arrow(478, 150, 500, 150, C["cyan"], 1.3))
    # call + crm
    d.add(rect(506, 24, 180, 124, 14, C["bg1"], C["orange"], 1.2),
          circle(546, 70, 20, C["orangeDeep"], C["orange2"], 1.2),
          path("M538 62 h5 l3 7 -3 2 a14 14 0 0 0 7 7 l2 -3 7 3 v5 a3 3 0 0 1 -3 3 A24 24 0 0 1 535 65 a3 3 0 0 1 3 -3z",
               C["orange2"], 1.2),
          t(576, 66, "AI call-back", 11, C["ink"], DISPLAY, 700),
          t(576, 80, "within minutes", 9.5, C["grey"]),
          wave(522, 118, 150, 18, 30, C["orange2"], 4, 1.5))
    d.add(rect(506, 158, 180, 124, 14, C["bg1"], C["line2"], 1.2),
          mono(518, 176, "New lead · CRM", 9, C["grey"]),
          bars(518, 188, [110, 80], 5, 12))
    s1, w1 = chip(518, 216, "Instagram", C["purple"])
    s2, _ = chip(524 + w1, 216, "Hot", C["orange"])
    s3, _ = chip(518, 240, "Task · due now", C["green2"])
    d.add(s1, s2, s3)


# ---------------------------------------------------------------- 05
def dashboard_websites(d):
    d.halo(170, 150, 190, 140, C["orange"], .14)
    d.halo(540, 150, 200, 150, C["cyan"], .22)
    x0, y0 = 16, 26
    d.add(window(x0, y0, 280, 240, "Your dashboard"))
    d.add(mono(x0 + 16, y0 + 44, "Package price", 9, C["grey"]),
          rect(x0 + 16, y0 + 50, 248, 28, 6, C["bg2"], C["orange2"], 1),
          t(x0 + 28, y0 + 69, "₹ 12,999", 12, C["ink"], DISPLAY, 700),
          line(x0 + 92, y0 + 56, x0 + 92, y0 + 72, C["orange2"], 1.4),
          mono(x0 + 16, y0 + 98, "Departure dates", 9, C["grey"]))
    x = x0 + 16
    for lab in ("12 Oct", "26 Oct", "9 Nov"):
        s, w = chip(x, y0 + 104, lab, C["cyan"])
        d.add(s)
        x += w + 6
    for i, (lab, on) in enumerate((("Show reviews", True), ("Diwali offer banner", True), ("FAQ section", False))):
        y = y0 + 142 + i * 24
        col = C["green2"] if on else C["line2"]
        d.add(t(x0 + 16, y + 4, lab, 9.5, C["ink"]),
              rect(x0 + 232, y - 6, 30, 15, 7.5, C["greenDeep"] if on else C["bg3"], col, .8),
              circle(x0 + (254 if on else 240), y + 1.5, 5, col))
    d.add(button(x0 + 176, y0 + 206, 88, 22, "Save", "orange", size=11))
    d.add(arrow(300, 150, 372, 150, C["orange2"], 1.4),
          mono(336, 140, "Live", 9, C["orange2"], "middle"), mono(336, 168, "at once", 9, C["grey"], "middle"))
    # website
    bx, by = 380, 10
    d.add(window(bx, by, 304, 270, "yourbusiness.com"),
          rect(bx + 10, by + 30, 284, 70, 6, C["blueDeep"], None),
          path(f"M{bx + 10} {by + 92} L{bx + 90} {by + 52} L{bx + 140} {by + 80} L{bx + 190} {by + 58} L{bx + 294} {by + 96}",
               C["cyan"], 1.2),
          circle(bx + 250, by + 50, 10, C["orange2"], opacity=.85),
          rect(bx + 10, by + 110, 180, 92, 8, C["bg3"], C["cyan"], 1),
          bars(bx + 22, by + 124, [120, 90], 5, 12),
          t(bx + 22, by + 166, "₹ 12,999", 14, C["cyan"], DISPLAY, 800),
          mono(bx + 102, by + 166, "per person", 9, C["grey"]),
          button(bx + 22, by + 176, 90, 18, "Hold my seat", "orange", size=9.5),
          bars(bx + 10, by + 216, [180, 150, 120], 4.5, 11))
    for i, (val, lab) in enumerate((("92", "Mobile"), ("100", "SEO"))):
        cx, cy, r = bx + 246, by + 132 + i * 66, 20
        frac = int(val) / 100
        if frac >= 1:
            arc = circle(cx, cy, r, "none", C["green2"], 3)
        else:
            ang = -math.pi / 2 + frac * 2 * math.pi
            ex, ey = cx + r * math.cos(ang), cy + r * math.sin(ang)
            arc = path(f"M{cx} {cy - r} A{r} {r} 0 {1 if frac > .5 else 0} 1 {ex:.2f} {ey:.2f}", C["green2"], 3)
        d.add(circle(cx, cy, r, "none", C["line"], 3), arc,
              t(cx, cy + 4.5, val, 12, C["ink"], DISPLAY, 800, "middle"),
              mono(cx, cy + r + 13, lab, 9, C["green2"], "middle"))
    d.add(example_tag(x0 + 12, y0 + 214))


# ---------------------------------------------------------------- 06
def ai_whatsapp_agent(d):
    d.halo(350, 150, 250, 150, C["green"], .16)
    d.halo(560, 190, 150, 100, C["orange"], .16)
    px = 275
    d.add(phone(px, 6, 150, 278, C["green2"]),
          circle(298, 38, 9, C["greenDeep"], C["green2"], 1),
          t(313, 36, "Your business", 10, C["ink"], DISPLAY, 700),
          mono(313, 47, "typing…", 9, C["green2"]),
          line(282, 55, 418, 55, C["line"]))
    d.add(bubble(284, 62, 118, 36, "in"),
          lines(292, 76, ["Goa trip ka price?", "4 log hain"], 9.5))
    d.add(bubble(298, 104, 118, 50, "out"),
          lines(306, 118, ["4 logon ke liye 3N/4D:"], 9.5),
          t(306, 136, "₹13,499", 12, C["cyan"], DISPLAY, 800), mono(360, 136, "/person", 9, C["grey"]),
          mono(306, 148, "From live sheet", 9, C["grey"]))
    d.add(bubble(298, 160, 118, 44, "out"))
    for i in range(3):
        d.add(thumb(304 + i * 37, 166, 33, 32, C["green2"]))
    d.add(rect(298, 210, 118, 22, 6, C["cyanDeep"], C["cyan"], .8),
          path("M306 214 h8 l3 3 v11 h-11 z", C["cyan"], 1),
          t(322, 225, "Itinerary.pdf", 9.5, C["ink"]))
    d.add(bubble(284, 238, 124, 36, "in"),
          lines(292, 252, ["Book karna hai.", "Advance kaise bhejein?"], 9.5))
    d.add(example_tag(208, 268))
    d.add(callout(284, 80, 196, 40, "Replies in Hinglish", "left", sub="and Hindi, English"),
          callout(298, 130, 196, 112, "Price from your live sheet", "left", sub="never invented"),
          callout(298, 182, 196, 184, "Photos and PDFs", "left", C["purple"]))
    # hand-over card
    d.add(path("M408 256 C 470 256, 470 200, 510 200", C["orange2"], 1.1, dash="3 3"),
          rect(510, 150, 176, 104, 10, C["bg1"], C["orange"], 1.2),
          mono(522, 168, "Hand-over alert", 9, C["orange2"]),
          t(522, 188, "Ready to pay", 12, C["ink"], DISPLAY, 700),
          t(522, 204, "4 people · Goa · Dec", 9.5, C["grey"]))
    s, _ = chip(522, 218, "Hot lead", C["orange"])
    d.add(s)
    d.add(callout(416, 70, 504, 60, "Shows typing… like a person", "right"),
          callout(416, 140, 504, 110, "Lead saved and scored", "right", C["green2"]))


# ---------------------------------------------------------------- 07
def ai_voice_calling_agent(d):
    d.halo(350, 100, 250, 110, C["purple"], .30)
    d.halo(350, 110, 160, 80, C["cyan"], .16)
    cx0, cy0, cw, ch = 150, 12, 400, 150
    d.add(rect(cx0, cy0, cw, ch, 16, C["bg1"], C["purple"], 1.2))
    for r, o in ((44, .12), (34, .22)):
        d.add(circle(222, 86, r, C["purple"], opacity=o))
    d.add(circle(222, 86, 25, C["purpleDeep"], C["cyan"], 1.4),
          path("M212 80 h6 l3 8 -4 2.5 a17 17 0 0 0 8.5 8.5 l2.5 -4 8 3 v6 a3.5 3.5 0 0 1 -3.5 3.5 A28 28 0 0 1 208.5 83.5 a3.5 3.5 0 0 1 3.5 -3.5z",
               C["cyan"], 1.3),
          t(222, 134, "AI caller", 11, C["ink"], DISPLAY, 700, "middle"),
          mono(222, 148, "In call 02:04", 9, C["green2"], "middle"))
    d.add(mono(280, 48, "Customer", 9, C["grey"]), wave(282, 68, 250, 26, 44, C["cyan"], 1, 1.8),
          mono(280, 104, "Agent", 9, C["grey"]), wave(282, 124, 250, 26, 44, C["purple"], 6, 1.8),
          mono(530, 150, "Stereo recording", 9, C["grey"], "end"))
    d.add(example_tag(cx0 + cw - 84, cy0 + 8))
    # timeline
    steps = [("Lead arrives", "form, DM, ad", C["grey"]), ("Called in ~1 min", "while still keen", C["cyan"]),
             ("First word 0.91 s", "after pickup", C["cyan"]), ("WhatsApp sent", "during the call", C["green2"]),
             ("Callback booked", "customer's own time", C["orange2"]), ("Score 82/100", "summary + task", C["purple"])]
    y = 206
    d.add(line(40, y, 660, y, C["line2"], 1.2))
    for i, (a, b, col) in enumerate(steps):
        x = 40 + i * 124
        d.add(circle(x, y, 8, C["bg"], col, 1.4), circle(x, y, 3, col),
              t(x, y + 26, a, 10.5, C["ink"], BODY, 600, "middle" if 0 < i < 5 else ("start" if i == 0 else "end")),
              t(x, y + 40, b, 9.5, C["grey"], BODY, 400, "middle" if 0 < i < 5 else ("start" if i == 0 else "end")))
        if i < 5:
            d.add(arrow(x + 14, y, x + 110, y, col, 1.2, opacity=.8))
    d.add(path("M350 162 L350 196", C["cyan"], 1, dash="2 3", opacity=.7))


# ---------------------------------------------------------------- 08
def crm(d):
    d.halo(260, 150, 260, 150, C["blue"], .20)
    d.halo(600, 150, 120, 130, C["orange"], .12)
    x0, y0 = 12, 10
    d.add(window(x0, y0, 470, 270, "Pipeline"))
    cols = ["New", "Contacted", "Site visit", "Won"]
    src = [("WhatsApp", C["green2"]), ("Instagram", C["purple"]), ("Website", C["cyan"]), ("Call", C["orange2"])]
    counts = [3, 3, 2, 2]
    for c, name in enumerate(cols):
        cx = x0 + 10 + c * 115
        d.add(mono(cx + 4, y0 + 42, name, 9, C["green2"] if name == "Won" else C["grey"]),
              rect(cx, y0 + 50, 108, 212, 8, C["bg2"], None))
        for k in range(counts[c]):
            y = y0 + 58 + k * 66
            lab, col = src[(c * 2 + k) % 4]
            d.add(rect(cx + 5, y, 98, 58, 7, C["bg3"], col if (c, k) == (0, 0) else C["line2"], .9),
                  bars(cx + 13, y + 10, [64, 44], 4.5, 10))
            s, _ = chip(cx + 12, y + 34, lab, col, 9, 5, 15)
            d.add(s)
            if name == "Won":
                d.add(tick(cx + 84, y + 10, 10))
            else:
                d.add(circle(cx + 90, y + 14, 6, C["bg4"], C["line2"], .8))
    d.add(example_tag(x0 + 386, y0 + 4))
    # follow-ups
    fx = 498
    d.add(rect(fx, 10, 190, 270, 12, C["bg1"], C["orange"], 1.1),
          mono(fx + 14, 32, "My follow-ups today", 9, C["orange2"]))
    times = ["10:30", "11:15", "12:00", "14:30", "16:00", "17:45"]
    for i, tm in enumerate(times):
        y = 52 + i * 36
        done = i < 2
        d.add(rect(fx + 14, y, 14, 14, 3.5, C["greenDeep"] if done else C["bg"], C["green2"] if done else C["line2"], 1))
        if done:
            d.add(tick(fx + 16, y + 1, 10, C["green2"], 1.5))
        d.add(bars(fx + 38, y + 1, [96 if i % 2 else 80, 60], 4.5, 10, C["line2"] if not done else C["line"]),
              mono(fx + 176, y + 11, tm, 9, C["grey"], "end"))
    d.add(mono(fx + 14, 270, "Every lead gets a task", 9, C["grey"]))


# ---------------------------------------------------------------- 09
def lead_capture_crm_sync(d):
    d.halo(340, 150, 200, 130, C["cyan"], .20)
    d.halo(590, 240, 110, 60, C["green"], .22)
    sources = [("WhatsApp 1", C["green2"]), ("WhatsApp 2", C["green2"]), ("Instagram", C["purple"]),
               ("Website", C["cyan"]), ("AI calls", C["orange2"]), ("Broadcasts", C["blue"])]
    for i, (lab, col) in enumerate(sources):
        y = 22 + i * 44
        s, w = chip(16, y, lab, col, 9, 8, 20)
        d.add(s, path(f"M{16 + w + 4} {y + 10} C 200 {y + 10}, 200 150, 240 150", col, 1, opacity=.75),
              circle(16 + w + 4, y + 10, 2.2, col))
    d.add(rect(240, 64, 196, 172, 14, C["bg1"], C["cyan"], 1.2),
          mono(256, 86, "Clean and tag", 9, C["cyan"]))
    for i, num in enumerate(("+91 98••• •••••", "098••• •••••", "98••• •••••")):
        y = 108 + i * 22
        d.add(t(256, y, num, 10, C["grey"], DISPLAY, 600),
              path(f"M362 {y - 4} C 380 {y - 4}, 380 164, 396 164", C["line2"], 1))
    d.add(rect(256, 176, 164, 26, 6, C["cyanDeep"], C["cyan"], .9),
          t(268, 194, "98••• •••••", 11, C["ink"], DISPLAY, 700),
          mono(412, 194, "one person", 9, C["cyan"], "end"),
          mono(256, 224, "Update, never duplicate", 9, C["grey"]))
    d.add(arrow(440, 150, 486, 150, C["cyan"], 1.4))
    d.add(rect(490, 40, 196, 150, 12, C["bg1"], C["line2"], 1.2),
          mono(504, 60, "CRM record", 9, C["grey"]),
          circle(516, 84, 10, C["bg4"], C["line2"], .8), bars(534, 78, [100, 70], 4.5, 11))
    s1, _ = chip(504, 110, "Source · Instagram", C["purple"])
    s2, _ = chip(504, 134, "Task · due now", C["orange"])
    s3, _ = chip(504, 158, "Brand · correct book", C["cyan"])
    d.add(s1, s2, s3)
    # audit lamps
    d.add(rect(490, 208, 196, 70, 12, C["bg1"], C["green2"], 1),
          mono(504, 228, "Daily lead audit", 9, C["grey"]))
    for i, (col, lit) in enumerate(((C["green2"], True), (C["orange2"], False), (C["red"], False))):
        cx = 514 + i * 26
        d.add(circle(cx, 254, 9, col, opacity=1 if lit else .18))
        if lit:
            d.add(circle(cx, 254, 15, col, opacity=.18))
    d.add(t(672, 260, "27/27", 16, C["green2"], DISPLAY, 800, "end"))


# ---------------------------------------------------------------- 10
def bookings_payment_followups(d):
    d.halo(350, 60, 300, 70, C["cyan"], .14)
    d.halo(520, 210, 190, 90, C["green"], .16)
    steps = [("Seat hold", C["green2"], True), ("Advance paid", C["green2"], True), ("Reminder", C["orange2"], None),
             ("Balance paid", C["line2"], False), ("Invoice", C["line2"], False)]
    y = 44
    for i, (lab, col, done) in enumerate(steps):
        x = 60 + i * 145
        if i < 4:
            d.add(line(x + 14, y, x + 131, y, C["green2"] if done else C["line2"], 1.4, None if done else "3 4"))
        d.add(circle(x, y, 13, C["greenDeep"] if done else (C["orangeDeep"] if done is None else C["bg1"]), col, 1.4))
        if done:
            d.add(tick(x - 5, y - 5, 10))
        elif done is None:
            d.add(circle(x, y, 4, C["orange2"]))
        d.add(t(x, y + 32, lab, 10.5, C["ink"] if done is not False else C["grey"], BODY, 600, "middle"))
    # receipt
    rx, ry = 40, 96
    d.add(rect(rx, ry, 290, 184, 12, C["bg1"], C["line2"], 1.2),
          mono(rx + 16, ry + 22, "Booking register", 9, C["grey"]))
    rows = [("Trip total", "₹ 54,000", C["ink"]), ("Paid", "₹ 20,000", C["green2"]),
            ("Balance due", "₹ 34,000", C["orange2"]), ("Coupon", "DIWALI10", C["cyan"])]
    for i, (k, v, col) in enumerate(rows):
        yy = ry + 50 + i * 26
        d.add(t(rx + 16, yy, k, 10, C["grey"]), t(rx + 274, yy, v, 12, col, DISPLAY, 700, "end"),
              line(rx + 16, yy + 9, rx + 274, yy + 9, C["line"], .8))
    d.add(rect(rx + 16, ry + 152, 150, 20, 4, C["greenDeep"], C["green2"], .9),
          mono(rx + 91, ry + 166, "Advance collected", 9, C["green2"], "middle"))
    # whatsapp reminder
    wx, wy = 370, 104
    d.add(bubble(wx, wy, 300, 92, "out"),
          mono(wx + 12, wy + 18, "WhatsApp reminder", 9, C["cyan"]),
          lines(wx + 12, wy + 38, ["Hi! Your balance of ₹34,000 is due on 20 Oct.", "Pay safely by UPI or card:"], 10),
          button(wx + 12, wy + 64, 100, 20, "Pay now", "orange", size=10))
    d.add(rect(wx, wy + 104, 190, 36, 8, C["bg1"], C["line2"], 1),
          path(f"M{wx + 14} {wy + 112} h12 l5 5 v14 h-17 z", C["red"], 1.1),
          t(wx + 40, wy + 126, "Invoice-1042.pdf", 10, C["ink"], BODY, 600))
    d.add(mono(wx + 202, wy + 126, "Branded invoice", 9, C["grey"]))
    d.add(example_tag(wx, wy + 152), mono(wx + 84, wy + 164, "Stops the moment it's paid", 9, C["green2"]))


# ---------------------------------------------------------------- 11
def whatsapp_broadcasts(d):
    d.halo(360, 150, 220, 150, C["cyan"], .18)
    d.halo(610, 150, 110, 130, C["green"], .18)
    d.add(rect(14, 94, 176, 104, 12, C["bg1"], C["cyan"], 1.2),
          mono(28, 114, "One base message", 9, C["cyan"]),
          bars(28, 126, [140, 120, 132, 70], 5, 12))
    d.add(mono(28, 190, "Rewritten per person", 9, C["grey"]))
    times = ["10:02", "10:07", "10:11", "10:19", "10:26", "10:34"]
    widths = [[110, 80], [96, 104], [120, 60], [88, 112], [104, 90], [116, 74]]
    for i, tm in enumerate(times):
        y = 14 + i * 45
        d.add(path(f"M190 146 C 240 146, 240 {y + 17}, 282 {y + 17}", C["cyan"], .9, opacity=.6),
              bubble(282, y, 172, 34, "out"), bars(292, y + 10, widths[i], 4.5, 11, C["cyan"]),
              mono(446, y + 14, tm, 9, C["grey"], "end"))
        if i == 2:
            d.add(mono(446, y + 28, "typing…", 9, C["green2"], "end"))
    d.add(mono(368, 286, "Human pace · random gaps", 9, C["grey"], "middle"))
    outs = [("Reply → AI agent", C["purple"], 30), ("Reply → team inbox", C["cyan"], 92),
            ("Saved as a lead", C["green2"], 154), ("STOP → removed", C["red"], 216)]
    for lab, col, y in outs:
        d.add(arrow(456, y + 16, 500, y + 16, col, 1.1, opacity=.9),
              rect(506, y, 180, 34, 8, C["bg1"], col, 1),
              circle(522, y + 17, 4.5, col), t(534, y + 21, lab, 10.5, C["ink"], BODY, 600))
    d.add(example_tag(14, 208))


# ---------------------------------------------------------------- 12
def lead_finder(d):
    d.halo(140, 110, 150, 110, C["purple"], .26)
    d.halo(500, 150, 220, 150, C["cyan"], .18)
    d.add(mono(18, 26, "You type in chat", 9, C["grey"]),
          bubble(18, 36, 240, 70, "out"),
          lines(30, 58, ["Find 50 marketing heads at", "real estate firms in Pune"], 11.5, C["ink"], 16, 500))
    d.add(bubble(18, 118, 200, 44, "in"),
          lines(30, 136, ["On it. Your list will be in", "the sheet by morning."], 9.5))
    s, _ = chip(18, 176, "Hiring now · 6 companies", C["orange2"])
    d.add(s, mono(18, 214, "Job posts = buying signal", 9, C["grey"]))
    d.add(arrow(262, 72, 292, 72, C["cyan"], 1.4))
    # sheet
    sx, sy, sw = 296, 12, 392
    d.add(window(sx, sy, sw, 268, "Leads · Google Sheet"))
    heads = [("Name", 12), ("Title", 100), ("Company", 208), ("Work email", 292)]
    for lab, off in heads:
        d.add(mono(sx + off, sy + 42, lab, 9, C["grey"]))
    d.add(line(sx, sy + 50, sx + sw, sy + 50, C["line"]))
    titles = ["Marketing Head", "Head of Marketing", "Marketing Manager", "CMO", "Brand Manager", "Growth Lead"]
    for i, ttl in enumerate(titles):
        y = sy + 66 + i * 32
        d.add(bars(sx + 12, y - 6, [70], 5), t(sx + 100, y, ttl, 9.5, C["ink"]),
              bars(sx + 208, y - 6, [62], 5), bars(sx + 292, y - 6, [60], 5, fill=C["cyan"]))
        if i == 4:
            s, _ = chip(sx + 358, y - 12, "Check", C["orange2"], 9, 4, 14)
            d.add(s)
        else:
            d.add(tick(sx + 364, y - 9, 10))
        d.add(line(sx + 8, y + 14, sx + sw - 8, y + 14, C["line"], .6))
    d.add(rect(sx + 12, sy + 236, 200, 22, 6, C["purpleDeep"], C["purple"], .8),
          mono(sx + 22, sy + 251, "First message drafted", 9, C["ink"]))
    d.add(example_tag(sx + sw - 84, sy + 238))


# ---------------------------------------------------------------- 13
def cold_email_engine(d):
    d.halo(160, 170, 180, 120, C["cyan"], .16)
    d.halo(590, 150, 120, 120, C["green"], .20)
    x0, base = 34, 238
    d.add(mono(x0, 26, "Sending ramp", 9, C["grey"]))
    hs = [26, 26, 20, 36, 54, 76, 100, 128, 156]
    labels = ["Warm", "up", "W1", "W2", "W3", "W4", "W5", "W6", "W7"]
    for i, h in enumerate(hs):
        x = x0 + i * 28
        warm = i < 2
        d.add(rect(x, base - h, 20, h, 4, C["purpleDeep"] if warm else C["cyanDeep"],
                   C["purple"] if warm else C["cyan"], 1),
              mono(x + 10, base + 16, labels[i], 9, C["purple"] if warm else C["grey"], "middle"))
    d.add(line(x0 - 6, base, x0 + 256, base, C["line2"]),
          path(f"M{x0 + 66} {base - 30} L{x0 + 234} {base - 166}", C["green2"], 1.2, dash="3 4"),
          mono(x0, base + 40, "Two weeks warm-up, then slow and steady", 9, C["grey"]))
    # inbox card
    ix = 318
    d.add(rect(ix, 30, 196, 230, 12, C["bg1"], C["line2"], 1.2),
          rect(ix + 12, 44, 82, 22, 6, C["greenDeep"], C["green2"], .9), mono(ix + 53, 59, "Inbox", 9, C["green2"], "middle"),
          rect(ix + 100, 44, 82, 22, 6, C["bg2"], C["line2"], .8), mono(ix + 141, 59, "Spam 0", 9, C["grey"], "middle"))
    for i in range(5):
        y = 80 + i * 34
        d.add(circle(ix + 24, y + 10, 7, C["bg4"], C["line2"], .8), bars(ix + 38, y + 4, [120 - i * 8, 90], 4.5, 10))
    d.add(mono(ix + 12, 250, "Plain text, real names", 9, C["grey"]))
    # reply alert
    ax = 530
    d.add(arrow(516, 146, 530, 146, C["green2"], 1.2),
          rect(ax + 4, 60, 154, 170, 14, C["bg1"], C["green2"], 1.2),
          mono(ax + 16, 80, "WhatsApp alert", 9, C["green2"]),
          t(ax + 16, 100, "Real reply", 12, C["ink"], DISPLAY, 700),
          bubble(ax + 14, 110, 134, 50, "in"),
          lines(ax + 22, 128, ["“Sounds good — can", "we talk Tuesday?”"], 9.5))
    s, _ = chip(ax + 14, 172, "Sequence stopped", C["green2"])
    d.add(s, example_tag(ax + 14, 202))


# ---------------------------------------------------------------- 14
def ai_carousel_studio(d):
    d.halo(330, 150, 200, 140, C["purple"], .24)
    d.halo(600, 150, 110, 120, C["orange"], .14)
    d.add(phone(14, 12, 150, 266, C["purple"]),
          mono(89, 50, "Carousel studio", 9, C["grey"], "middle"),
          bubble(34, 62, 118, 50, "out"),
          lines(42, 78, ["Topic:", "Monsoon treks", "near Pune"], 9.5, C["ink"], 12),
          bubble(24, 122, 118, 36, "in"),
          lines(32, 136, ["Researched. 3 versions", "of every slide ready."], 9))
    d.add(example_tag(52, 250))
    d.add(arrow(170, 140, 196, 140, C["cyan"], 1.3))
    for i, lab in enumerate("ABC"):
        x = 204 + i * 88
        picked = i == 1
        d.add(rect(x, 54, 78, 98, 8, C["bg3"], C["cyan"] if picked else C["line2"], 1.4 if picked else .9),
              rect(x + 8, 62, 62, 40, 4, C["purpleDeep"] if i != 2 else C["blueDeep"], None),
              path(f"M{x + 8} {96} L{x + 30} {76} L{x + 44} {90} L{x + 70} {70}", C["purple"] if i != 2 else C["cyan"], 1.2),
              bars(x + 8, 110, [58, 44, 30], 5, 10),
              mono(x + 39, 172, lab, 9, C["cyan"] if picked else C["grey"], "middle"))
        if picked:
            d.add(circle(x + 70, 54, 10, C["green"]), tick(x + 65, 49, 10, C["bg"], 2))
    d.add(mono(336, 196, "Tap to pick the best version", 9, C["grey"], "middle"),
          rect(204, 214, 254, 44, 8, C["bg1"], C["line2"], .9),
          mono(216, 232, "Caption + hashtags", 9, C["grey"]), bars(216, 240, [200], 4.5))
    d.add(arrow(464, 140, 494, 140, C["cyan"], 1.3))
    for i in range(5):
        x, y = 512 + i * 12, 40 + i * 8
        d.add(rect(x, y, 110, 136, 9, C["bg1"], C["cyan"] if i == 4 else C["line2"], 1))
    d.add(rect(566, 60, 94, 58, 5, C["purpleDeep"], None),
          path("M566 110 L590 88 L606 104 L630 80 L660 104", C["orange2"], 1.3),
          bars(572, 130, [80, 60], 5, 11))
    d.add(button(520, 204, 150, 26, "Post now", "orange", size=12),
          tick(524, 247, 10), mono(540, 256, "Live on Instagram", 9, C["green2"]))


# ---------------------------------------------------------------- 15
def ai_video_factory(d):
    d.halo(350, 130, 320, 130, C["purple"], .20)
    d.halo(620, 130, 90, 120, C["orange"], .14)
    # film strip band
    d.add(rect(8, 22, 684, 212, 10, C["bg1"], C["line"], 1))
    for i in range(34):
        d.add(rect(18 + i * 20, 28, 10, 7, 1.5, C["bg4"], None), rect(18 + i * 20, 221, 10, 7, 1.5, C["bg4"], None))
    labels = [("Script", "fresh topic"), ("Voice", "Hindi or English"), ("Scenes", "consistent characters"),
              ("Captions", "word by word"), ("Publish", "Shorts and Reels")]
    for i, (lab, sub) in enumerate(labels):
        x, y, w, h = 34 + i * 132, 44, 100, 170
        d.add(rect(x, y, w, h, 8, C["bg2"], C["purple"] if i != 4 else C["orange"], 1))
        if i == 0:
            d.add(bars(x + 10, y + 16, [80, 70, 76, 50, 72, 64, 40, 70, 58], 4.5, 14, C["line2"]))
        elif i == 1:
            d.add(circle(x + 50, y + 60, 18, C["purpleDeep"], C["purple"], 1),
                  path(f"M{x + 46} {y + 52} v10 a4 4 0 0 0 8 0 v-10 a4 4 0 0 0 -8 0 z M{x + 42} {y + 62} a8 8 0 0 0 16 0 M{x + 50} {y + 70} v4",
                       C["ink"], 1.2),
                  wave(x + 10, y + 120, 80, 30, 20, C["purple"], 2, 1.8))
        elif i in (2, 3):
            d.add(rect(x + 6, y + 6, w - 12, h - 12, 6, C["blueDeep"], None),
                  circle(x + 68, y + 40, 12, C["ink"], opacity=.85),
                  path(f"M{x + 6} {y + 128} L{x + 34} {y + 92} L{x + 56} {y + 116} L{x + 72} {y + 100} L{x + 94} {y + 128}",
                       C["purple"], 1.3, fill=C["purpleDeep"]))
            if i == 3:
                d.add(rect(x + 12, y + 134, 76, 18, 4, C["bg"], None, opacity=.85),
                      t(x + 22, y + 147, "aur", 10, C["ink"], DISPLAY, 700),
                      rect(x + 44, y + 137, 38, 13, 3, C["orange2"], None),
                      t(x + 63, y + 147, "tab", 10, C["bg"], DISPLAY, 800, "middle"))
        else:
            d.add(circle(x + 50, y + 70, 24, C["orangeDeep"], C["orange2"], 1.3),
                  path(f"M{x + 44} {y + 58} l18 12 l-18 12 z", C["orange2"], 1.2, fill=C["orange2"]))
            s1, _ = chip(x + 14, y + 112, "Shorts", C["red"])
            s2, _ = chip(x + 14, y + 136, "Reels", C["purple"])
            d.add(s1, s2)
        d.add(mono(x + w / 2, 256, lab, 9, C["ink"], "middle"), t(x + w / 2, 272, sub, 9.5, C["grey"], BODY, 400, "middle"))
        if i < 4:
            d.add(arrow(x + w + 6, y + h / 2, x + w + 26, y + h / 2, C["cyan"], 1.3))
    d.add(mono(598, 16, "1080 × 1920", 9, C["grey"]))


# ---------------------------------------------------------------- 16
def automate(d):
    d.halo(330, 150, 260, 150, C["blue"], .20)
    d.halo(520, 60, 120, 60, C["green"], .18)

    def box(x, y, w, h, kicker, title, col):
        return (rect(x, y, w, h, 10, C["bg1"], col, 1.2) + mono(x + 12, y + 18, kicker, 9, col)
                + t(x + 12, y + 36, title, 11, C["ink"], DISPLAY, 700))

    d.add(box(12, 118, 132, 50, "Trigger", "New enquiry", C["cyan"]),
          arrow(146, 143, 186, 143, C["cyan"], 1.3),
          box(190, 110, 148, 66, "AI decides", "Hot, warm or cold?", C["purple"]),
          t(202, 166, "reads voice notes too", 9.5, C["grey"]))
    # approval branch
    d.add(path("M338 130 C 370 130, 370 50, 400 50", C["orange2"], 1.2), mono(372, 104, "money?", 9, C["orange2"]),
          rect(404, 22, 172, 58, 10, C["bg1"], C["orange"], 1.2),
          mono(416, 40, "Human approval", 9, C["orange2"]),
          t(416, 60, "Refund ₹2,400?", 11, C["ink"], DISPLAY, 700),
          button(520, 46, 46, 18, "Yes", "green", size=9.5))
    actions = [("WhatsApp welcome sent", C["green2"]), ("CRM record + follow-up task", C["blue"]),
               ("Owner alert on Telegram", C["orange2"])]
    for i, (lab, col) in enumerate(actions):
        y = 104 + i * 46
        d.add(path(f"M338 150 C 370 150, 370 {y + 17}, 404 {y + 17}", col, 1.1, opacity=.85),
              rect(404, y, 172, 34, 8, C["bg1"], col, 1),
              circle(420, y + 17, 4.5, col), t(432, y + 21, lab, 9.5, C["ink"], BODY, 600))
    # run log
    lx = 592
    d.add(rect(lx, 22, 96, 250, 10, C["bg1"], C["line2"], 1), mono(lx + 10, 40, "Run log", 9, C["grey"]))
    for i, tm in enumerate(("10:02", "10:05", "10:11", "10:19", "10:26", "10:34", "10:41", "10:58")):
        y = 60 + i * 26
        d.add(tick(lx + 10, y - 8, 9), mono(lx + 26, y, tm, 9, C["ink"]))
        if i == 6:
            d.add(mono(lx + 70, y, "!", 9, C["orange2"]))
    d.add(mono(12, 270, "Logged · alerts before customers notice", 9, C["grey"]), example_tag(12, 212))


# ---------------------------------------------------------------- 17
def care(d):
    d.halo(350, 145, 200, 150, C["green"], .20)
    d.halo(350, 145, 120, 100, C["cyan"], .14)
    d.add(path("M0 150 H250 L268 150 L280 108 L296 196 L312 128 L324 150 H700", C["cyan"], 1.4, opacity=.55))
    d.add(path("M350 52 L412 76 V140 C412 190 386 222 350 236 C314 222 288 190 288 140 V76 Z", C["green2"], 1.6,
               fill=C["bg1"]),
          path("M322 146 h14 l8 -18 l12 34 l8 -16 h14", C["green2"], 1.8),
          mono(350, 262, "Watched daily", 9, C["green2"], "middle"))
    # status list
    d.add(rect(14, 40, 214, 206, 12, C["bg1"], C["line2"], 1.2),
          mono(28, 62, "Morning health check", 9, C["grey"]))
    for i, lab in enumerate(("WhatsApp numbers", "Team inbox sync", "CRM and leads", "Automations", "Backups")):
        y = 90 + i * 32
        d.add(circle(34, y - 4, 5, C["green2"]), circle(34, y - 4, 9, C["green2"], opacity=.18),
              t(48, y, lab, 10.5, C["ink"], BODY, 500), mono(214, y, "OK", 9, C["green2"], "end"))
    # backup calendar
    bx = 470
    d.add(rect(bx, 40, 216, 206, 12, C["bg1"], C["line2"], 1.2),
          mono(bx + 14, 62, "Nightly backups", 9, C["grey"]))
    for k in range(28):
        r_, c_ = divmod(k, 7)
        x, y = bx + 16 + c_ * 27, 76 + r_ * 30
        done = k >= 17
        d.add(rect(x, y, 22, 22, 5, C["greenDeep"] if done else C["bg2"], C["green2"] if done else C["line"], .9))
        if done:
            d.add(tick(x + 6, y + 6, 10, C["green2"], 1.5))
    d.add(t(bx + 14, 214, "11 in a row", 13, C["green2"], DISPLAY, 800),
          mono(bx + 14, 232, "Off-site, verified", 9, C["grey"]))


# ---------------------------------------------------------------- cover map
FAMILY_COL = {"flagship": C["orange"], "talk": C["cyan"], "ai": C["purple"], "sell": C["blue"],
              "grow": C["green2"], "run": C["ink"]}


MAP_NAME = {  # README "Short name" column
    "01": "Personal AI Assistant", "02": "WhatsApp Connect", "03": "Inbox", "04": "Instagram Automation",
    "05": "Dashboard Websites", "06": "AI WhatsApp Agent", "07": "Voice Agent", "08": "CRM", "09": "Lead Capture",
    "10": "Bookings", "11": "Broadcasts", "12": "Lead Finder", "13": "Cold Email", "14": "Carousel Studio",
    "15": "Video Factory", "16": "Automate", "17": "Care"}


def cover_map(products):
    d = Doc("cover", 760, 560)
    cx, cy, R = 380, 280, 192
    d.halo(cx, cy, 330, 270, C["purple"], .26, "hp")
    d.halo(cx, cy, 220, 200, C["cyan"], .22, "hc")
    for r, o in ((R + 46, .10), (R, .22), (132, .16), (90, .22)):
        d.add(circle(cx, cy, r, "none", C["cyan"], .8, opacity=o))
    n = len(products)
    icon_dir = OUT / "icons"
    pts = []
    for i, p in enumerate(products):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        pts.append((x, y, a, p))
    # spokes and neighbour links
    for i, (x, y, a, p) in enumerate(pts):
        col = FAMILY_COL[p["family"]]
        d.add(line(cx + 90 * math.cos(a), cy + 90 * math.sin(a), x - 22 * math.cos(a), y - 22 * math.sin(a),
                   col, 1, opacity=.45))
        mid = (cx + 132 * math.cos(a), cy + 132 * math.sin(a))
        d.add(circle(*mid, 2.4, col, opacity=.9))
    for (x1, y1, _, p1), (x2, y2, _, p2) in zip(pts, pts[1:] + pts[:1]):
        same = p1["family"] == p2["family"]
        d.add(line(x1, y1, x2, y2, FAMILY_COL[p1["family"]] if same else C["line2"], 1.1 if same else .7,
                   None if same else "2 4", .8 if same else .6))
    for x, y, a, p in pts:
        col = FAMILY_COL[p["family"]]
        big = p.get("flagship")
        r = 27 if big else 22
        d.add(circle(x, y, r + 8, col, opacity=.12), circle(x, y, r, C["bg1"], col, 1.6 if big else 1.2))
        icon = (icon_dir / f"{p['slug']}.svg").read_text()
        inner = icon[icon.index(">") + 1: icon.rindex("</svg>")]
        s = 1.25 if big else 1.0
        d.add(f'<g transform="translate({x - 12 * s:.1f} {y - 12 * s:.1f}) scale({s})" stroke="{col}" '
              f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none" color="{col}">{inner}</g>')
        lx, ly = x + (r + 14) * math.cos(a), y + (r + 14) * math.sin(a)
        anchor = "middle" if abs(math.cos(a)) < .3 else ("start" if math.cos(a) > 0 else "end")
        dy = 4 if abs(math.sin(a)) < .5 else (14 if math.sin(a) > 0 else -4)
        d.add(mono(lx, ly + dy - 12 if dy < 0 else ly + dy, p["code"], 9, col, anchor),
              t(lx, (ly + dy + 2) if dy < 0 else ly + dy + 13, MAP_NAME[p["code"]], 11.5, C["ink"], BODY, 600, anchor))
    # core
    d.add(circle(cx, cy, 70, C["cyan"], opacity=.08), circle(cx, cy, 58, C["bg"], C["cyan"], 1.6),
          circle(cx, cy, 64, "none", C["purple"], 1, opacity=.6),
          t(cx, cy + 4, "WAKFLOW", 15, C["ink"], DISPLAY, 800, "middle", ls=1.5),
          mono(cx, cy + 22, "One system", 9, C["cyan"], "middle"))
    return d.render()


SCENES = {
    "personal-ai-assistant": personal_ai_assistant, "whatsapp-connect": whatsapp_connect, "inbox": inbox,
    "instagram-automation": instagram_automation, "dashboard-websites": dashboard_websites,
    "ai-whatsapp-agent": ai_whatsapp_agent, "ai-voice-calling-agent": ai_voice_calling_agent, "crm": crm,
    "lead-capture-crm-sync": lead_capture_crm_sync, "bookings-payment-followups": bookings_payment_followups,
    "whatsapp-broadcasts": whatsapp_broadcasts, "lead-finder": lead_finder, "cold-email-engine": cold_email_engine,
    "ai-carousel-studio": ai_carousel_studio, "ai-video-factory": ai_video_factory, "automate": automate,
    "care": care,
}


def main():
    import yaml
    products = yaml.safe_load((OUT.parent / "content" / "products.yaml").read_text())["products"]
    (OUT / "hero").mkdir(exist_ok=True)
    for slug, fn in SCENES.items():
        d = Doc(slug, W, H)
        fn(d)
        (OUT / "hero" / f"{slug}.svg").write_text(d.render())
    (OUT / "cover-map.svg").write_text(cover_map(products))
    print(f"{len(SCENES)} heroes + cover map")


if __name__ == "__main__":
    main()
