# Yeelo Homeopathy – GMB Integration

This repo connects our local SEO landing pages and Google My Business profile.

## Linked Repos
- [seo-json-data](https://github.com/yeelohomeopathy/seo-json-data) → JSON for Sohna villages & locations
- [gmb-integration](https://github.com/yeelohomeopathy/gmb-integration) → Scripts, templates, SEO automation

# GMB Integration – Yeelo Homeopathy

Scripts and documentation for integrating Yeelo Homeopathy’s Google Business Profile (GMB) with local SEO landing pages.  

## Features
- Push local JSON → GMB Posts
- Sync reviews & store hours
- Auto-generate landing pages for villages
- Schema markup for LocalBusiness + Product

## Usage
1. Add your credentials to `/gmb-api-auth/credentials.json`
2. Run scripts from `/scripts/` to sync data with GMB
3. Deploy generated landing pages to WordPress/Laravel

## Related Repos
- [seo-json-data](https://github.com/yeelohomeopathy/seo-json-data)

gmb-integration/
│── README.md
│── requirements.txt
│── config.example.json
│
├── gmb-api-auth/
│   └── credentials.json   # (you replace with Google OAuth2 creds)
│
├── scripts/
│   ├── auth.py            # Google API authentication handler
│   ├── sync_reviews.py    # Fetch latest reviews from GMB
│   ├── sync_hours.py      # Update store hours
│   ├── push_local_pages.py# Auto-generate local landing pages
│   ├── sitemap_generator.py# Build sitemap.xml for products + locations
│   ├── 404_monitor.py     # Check for 404s and auto-redirect mapping
│   ├── analytics_events.py# Push GA4/GTM 404 + conversion events
│   └── utils.py           # Shared helpers
│
├── templates/
│   ├── landing_page_template.md   # SEO content template
│   ├── schema_template.jsonld     # JSON-LD (LocalBusiness + Product)
│   ├── 404_template.html          # Smart 404 page (with CTA + directions)
│   └── sticky_nap.html            # Sticky NAP banner snippet
│
└── docs/
    ├── setup_guide.md     # Step-by-step integration guide
    ├── gmb_api_setup.md   # How to enable Google My Business API
    └── seo_playbook.md    # Local SEO & GMB checklist
