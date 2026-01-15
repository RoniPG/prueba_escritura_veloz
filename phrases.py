import random


PHRASES = [
    "La rapidez es amiga de la precisión.",
    "Practicar escritura mejora tu velocidad mental.",
    "Python es un gran lenguaje para comenzar a programar.",
    "Escribir código limpio ahorra tiempo en el futuro.",
    "La práctica constante mejora la velocidad de escritura.",
    "La concentración es clave para escribir sin errores.",
    "Aprender a programar requiere paciencia y constancia.",
    "Un buen desarrollador practica todos los días.",
    "La velocidad sin precisión no sirve de mucho.",
    "Escribir bien es tan importante como escribir rápido.",
    "Cada error es una oportunidad para aprender.",
    "La lógica clara produce código más mantenible.",
    "La repetición fortalece la memoria muscular.",
    "Un teclado es la herramienta principal del programador.",
    "La mejora continua nace de la práctica diaria.",
    "Pensar antes de escribir reduce los errores.",
    "La experiencia se construye línea a línea.",
    "La constancia supera al talento sin disciplina.",
    "Un pequeño avance diario genera grandes resultados.",
    "La atención a los detalles marca la diferencia."
]



def get_random_phrase() -> str:
    """Devuelve una frase aleatoria de la lista PHRASES."""
    return random.choice(PHRASES)
