from googlesearch import search

def search_google(query):
    try:
        # Realiza la búsqueda en Google
        search_results = search(query, num=5, stop=5, pause=2)

        # Muestra los enlaces de los resultados
        print("Resultados de la búsqueda:")
        for i, link in enumerate(search_results, start=1):
            print(f"{i}. {link}")

    except Exception as e:
        print("Ocurrió un error:", e)

# Realiza la búsqueda
search_query = input("Ingrese su consulta: ")
search_google(search_query)
