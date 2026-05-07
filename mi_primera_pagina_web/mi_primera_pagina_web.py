import reflex as rx


class State(rx.State):
    contador: int = 0
    mensaje: str = "Estado del hospital: tranquilo por ahora."

    def activar_codigo(self):
        self.contador += 1
        if self.contador == 1:
            self.mensaje = "Código azul activado. El equipo médico entra en acción."
        elif self.contador == 2:
            self.mensaje = "Emergencia atendida. La presión aumenta en Seattle Grace."
        else:
            self.mensaje = f"Has activado {self.contador} emergencias. ¡Día intenso en cirugía!"


def tarjeta(titulo, texto, color):
    return rx.box(
        rx.vstack(
            rx.text(titulo, font_weight="bold", font_size="18px", color=color),
            rx.text(texto, color="#475569", text_align="center"),
            spacing="2",
            align="center",
        ),
        background="rgba(255,255,255,0.92)",
        border_radius="20px",
        padding="24px",
        width="260px",
        box_shadow="0 18px 45px rgba(15, 23, 42, 0.18)",
    )


def index():
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.badge("Fan Project", color_scheme="blue", size="3"),
                rx.badge("Sin spoilers después de 8x15", color_scheme="red", size="3"),
                rx.badge("Reflex + Poetry", color_scheme="green", size="3"),
                spacing="3",
            ),

            rx.heading(
                "Grey's Anatomy",
                font_size="72px",
                color="white",
                text_align="center",
                font_weight="900",
            ),

            rx.text(
                "Seattle Grace Mercy West — una página interactiva inspirada en drama médico, amistad y decisiones de vida o muerte.",
                color="#dbeafe",
                font_size="22px",
                text_align="center",
                max_width="850px",
            ),

            rx.box(
                rx.vstack(
                    rx.text("Panel de Emergencias", color="#1e293b", font_size="26px", font_weight="bold"),
                    rx.text(State.mensaje, color="#334155", font_size="18px", text_align="center"),
                    rx.text(f"Códigos activados: {State.contador}", color="#0f172a", font_size="34px", font_weight="bold"),
                    rx.button(
                        "Activar código azul",
                        on_click=State.activar_codigo,
                        size="4",
                        color_scheme="blue",
                        border_radius="999px",
                    ),
                    spacing="4",
                    align="center",
                ),
                background="rgba(255,255,255,0.95)",
                border_radius="28px",
                padding="38px",
                width="520px",
                box_shadow="0 25px 70px rgba(15, 23, 42, 0.28)",
            ),

            rx.hstack(
                tarjeta("Temporada", "Avance actual: 8x15", "#2563eb"),
                tarjeta("Hospital", "Seattle Grace Mercy West", "#0f766e"),
                tarjeta("Interacción", "Botón con cambio de estado", "#9333ea"),
                spacing="5",
                wrap="wrap",
                justify="center",
            ),

            rx.text(
                "“It’s a beautiful day to save lives.”",
                color="#e0f2fe",
                font_size="20px",
                font_style="italic",
            ),

            rx.text(
                "Desarrollado por Jael Castillo usando Reflex Framework.",
                color="#cbd5e1",
                font_size="14px",
            ),

            spacing="6",
            align="center",
        ),
        min_height="100vh",
        width="100%",
        padding="50px",
        background="radial-gradient(circle at top left, #38bdf8, transparent 30%), linear-gradient(135deg, #020617, #0f172a, #1e3a8a)",
    )


app = rx.App()
app.add_page(index)