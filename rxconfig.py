import reflex as rx

config = rx.Config(
    app_name="mi_primera_pagina_web",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)