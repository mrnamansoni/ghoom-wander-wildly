"""Writes svg/icons/<slug>.svg — one 24px line icon per product (stroke = currentColor)."""
from pathlib import Path

ICONS = {
    # chat bubble with a spark: an assistant that talks and acts
    "personal-ai-assistant": '<path d="M4 5.5h11a2.5 2.5 0 0 1 2.5 2.5v5.5a2.5 2.5 0 0 1-2.5 2.5H9l-4 3v-3H4a2.5 2.5 0 0 1-2.5-2.5V8A2.5 2.5 0 0 1 4 5.5z"/><path d="M19.5 2.5v4M17.5 4.5h4"/><path d="M6 10.5h7M6 13h4"/>',
    # phone linked to a node
    "whatsapp-connect": '<rect x="3" y="2.5" width="9" height="19" rx="2"/><path d="M6.5 18.5h2"/><path d="M12 12h4"/><circle cx="19" cy="12" r="2.6"/><path d="M19 9.4V6M19 14.6V18"/>',
    # inbox tray
    "inbox": '<path d="M3 13.5 5.5 5h13L21 13.5V19a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 19z"/><path d="M3 13.5h5l1.5 2.5h5l1.5-2.5h5"/>',
    # camera square with a speech tail
    "instagram-automation": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/>',
    # browser with a pencil
    "dashboard-websites": '<rect x="2.5" y="3.5" width="19" height="15" rx="2"/><path d="M2.5 7.5h19"/><path d="M8 15l6.5-6.5 1.8 1.8L9.8 16.8H8z"/>',
    # chat bubble with dots
    "ai-whatsapp-agent": '<path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z"/><circle cx="8.3" cy="12" r=".9" fill="currentColor"/><circle cx="12" cy="12" r=".9" fill="currentColor"/><circle cx="15.7" cy="12" r=".9" fill="currentColor"/>',
    # handset with sound waves
    "ai-voice-calling-agent": '<path d="M5 3.5h3l1.5 4-2 1.3a10 10 0 0 0 5 5l1.3-2 4 1.5v3a2 2 0 0 1-2 2A15.5 15.5 0 0 1 3 5.5a2 2 0 0 1 2-2z"/><path d="M15 3.5a6 6 0 0 1 5.5 5.5M15 7a2.8 2.8 0 0 1 2 2"/>',
    # pipeline columns
    "crm": '<rect x="3" y="3.5" width="5" height="17" rx="1.5"/><rect x="9.5" y="3.5" width="5" height="11" rx="1.5"/><rect x="16" y="3.5" width="5" height="7" rx="1.5"/>',
    # funnel
    "lead-capture-crm-sync": '<path d="M3 4h18l-7 8.5V19l-4 2v-8.5z"/>',
    # calendar with a tick
    "bookings-payment-followups": '<rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9h18M8 2.5v4M16 2.5v4"/><path d="m8.5 14.5 2.3 2.3 4.7-4.8"/>',
    # megaphone
    "whatsapp-broadcasts": '<path d="M3 10v4a1.5 1.5 0 0 0 1.5 1.5H7l7 4.5V4L7 8.5H4.5A1.5 1.5 0 0 0 3 10z"/><path d="M17.5 9a4 4 0 0 1 0 6M20 6.5a7.5 7.5 0 0 1 0 11"/>',
    # magnifier over a person
    "lead-finder": '<circle cx="10.5" cy="10.5" r="7"/><path d="m15.5 15.5 5 5"/><circle cx="10.5" cy="8.8" r="2.2"/><path d="M6.8 14.4a4.5 4.5 0 0 1 7.4 0"/>',
    # envelope with an arrow
    "cold-email-engine": '<rect x="2.5" y="5" width="15" height="12" rx="1.5"/><path d="m2.5 6.5 7.5 5.5 7.5-5.5"/><path d="M15.5 19.5h6M19 17l2.5 2.5L19 22"/>',
    # stacked slides
    "ai-carousel-studio": '<rect x="6.5" y="4" width="11" height="16" rx="1.8"/><path d="M4 6.5v11M20 6.5v11M1.5 9v6M22.5 9v6"/>',
    # play in a vertical frame
    "ai-video-factory": '<rect x="6" y="2.5" width="12" height="19" rx="2"/><path d="M10.5 9.2v5.6l4.4-2.8z"/>',
    # connected nodes
    "automate": '<circle cx="5" cy="6" r="2.5"/><circle cx="5" cy="18" r="2.5"/><circle cx="19" cy="12" r="2.5"/><path d="M7.5 6h3.5a3 3 0 0 1 3 3v0a3 3 0 0 0 2.5 3M7.5 18h3.5a3 3 0 0 0 3-3v0a3 3 0 0 1 2.5-3"/>',
    # shield with a pulse
    "care": '<path d="M12 2.5 4 5.5v6c0 5 3.4 8.6 8 10 4.6-1.4 8-5 8-10v-6z"/><path d="M7 12.5h2.5l1.5-3 2 5.5 1.5-2.5H17"/>',
}


def main():
    out = Path(__file__).resolve().parent / "icons"
    out.mkdir(exist_ok=True)
    for slug, body in ICONS.items():
        (out / f"{slug}.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>\n')
    print(f"{len(ICONS)} icons")


if __name__ == "__main__":
    main()
