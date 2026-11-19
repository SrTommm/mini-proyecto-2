"""
MINIPROYECTO 2 - SISTEMA DE GESTIÓN DE RESIDUOS

ARCHIVO DE INTERFAZ GRÁFICA

Este archivo contiene la interfaz gráfica del programa y se
entrega completamente implementado por el docente.

IMPORTANTE:
- No modificar ni eliminar las funciones de este archivo.
- No agregar elementos gráficos ni programar funcionalidades
  adicionales en este archivo.
- El desarrollo del estudiante debe realizarse exclusivamente
  en el archivo logica.py.
- La interfaz utiliza las funciones de logica.py para consultar
  los puntos de generación, evaluar y registrar jornadas,
  consultar el historial y comparar resultados.

Los archivos interfaz.py y logica.py deben permanecer en la
misma carpeta para que el programa funcione correctamente.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import logica


class AplicacionResiduos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de gestión y planificación de residuos")
        self.root.geometry("1180x780")
        self.root.minsize(980, 650)

        self.historial = []
        self.puntos = logica.obtener_puntos()

        self._configurar_estilos()
        self._crear_interfaz()
        self._cargar_puntos()
        self._actualizar_historial()

    def _configurar_estilos(self):
        estilo = ttk.Style()
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass
        estilo.configure("Titulo.TLabel", font=("Arial", 17, "bold"))
        estilo.configure("Subtitulo.TLabel", font=("Arial", 12, "bold"))
        estilo.configure("Dato.TLabel", font=("Arial", 10, "bold"))
        estilo.configure("Treeview", rowheight=27)
        estilo.configure("Treeview.Heading", font=("Arial", 9, "bold"))

    def _crear_interfaz(self):
        encabezado = ttk.Frame(self.root, padding=(18, 14))
        encabezado.pack(fill="x")
        ttk.Label(
            encabezado,
            text="Sistema de gestión y planificación de residuos",
            style="Titulo.TLabel"
        ).pack(anchor="w")
        ttk.Label(
            encabezado,
            text="Consulta los puntos de generación, evalúa jornadas y compara alternativas."
        ).pack(anchor="w", pady=(4, 0))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        self.tab_puntos = ttk.Frame(self.tabs, padding=14)
        self.tab_planificacion = ttk.Frame(self.tabs, padding=14)
        self.tab_resultados = ttk.Frame(self.tabs, padding=14)

        self.tabs.add(self.tab_puntos, text="1. Puntos de generación")
        self.tabs.add(self.tab_planificacion, text="2. Planificación")
        self.tabs.add(self.tab_resultados, text="3. Resultados y comparación")

        self._crear_tab_puntos()
        self._crear_tab_planificacion()
        self._crear_tab_resultados()

    def _crear_tab_puntos(self):
        ttk.Label(
            self.tab_puntos, text="Puntos de generación disponibles",
            style="Subtitulo.TLabel"
        ).pack(anchor="w", pady=(0, 6))
        ttk.Label(
            self.tab_puntos,
            text="Consulte las cantidades de residuos generadas en cada punto. Los valores están expresados en kilogramos."
        ).pack(anchor="w", pady=(0, 12))

        columnas = ("punto", "papel", "plastico", "vidrio", "organicos", "no_aprovechables", "total")
        self.tabla_puntos = ttk.Treeview(
            self.tab_puntos, columns=columnas, show="headings", height=12
        )
        titulos = {
            "punto": "Punto", "papel": "Papel/cartón", "plastico": "Plástico",
            "vidrio": "Vidrio", "organicos": "Orgánicos",
            "no_aprovechables": "No aprovechables", "total": "Total"
        }
        anchos = {
            "punto": 205, "papel": 115, "plastico": 105, "vidrio": 95,
            "organicos": 105, "no_aprovechables": 155, "total": 90
        }
        for col in columnas:
            self.tabla_puntos.heading(col, text=titulos[col])
            self.tabla_puntos.column(col, width=anchos[col], anchor="center")
        self.tabla_puntos.pack(fill="both", expand=True)

        ttk.Label(
            self.tab_puntos,
            text="Información ficticia definida para la simulación académica.",
            foreground="#555555"
        ).pack(anchor="w", pady=(10, 0))

    def _crear_tab_planificacion(self):
        ttk.Label(
            self.tab_planificacion, text="Planificar una jornada",
            style="Subtitulo.TLabel"
        ).pack(anchor="w", pady=(0, 6))
        ttk.Label(
            self.tab_planificacion,
            text="Seleccione uno o varios puntos. Cada punto seleccionado se atiende en su totalidad."
        ).pack(anchor="w", pady=(0, 10))

        restricciones = ttk.Frame(self.tab_planificacion)
        restricciones.pack(fill="x", pady=(0, 10))
        self._tarjeta_dato(restricciones, "Capacidad máxima", "160 kg").pack(side="left", fill="x", expand=True, padx=(0, 6))
        self._tarjeta_dato(restricciones, "Presupuesto máximo", "$305.000").pack(side="left", fill="x", expand=True, padx=6)
        self._tarjeta_dato(restricciones, "Transporte por punto", "$45.000").pack(side="left", fill="x", expand=True, padx=(6, 0))

        self.marco_seleccion = ttk.LabelFrame(
            self.tab_planificacion, text="Puntos disponibles", padding=10
        )
        self.marco_seleccion.pack(fill="x", pady=(0, 10))

        self.variables_puntos = {}
        for nombre in self.puntos:
            variable = tk.BooleanVar(value=False)
            self.variables_puntos[nombre] = variable
            ttk.Checkbutton(
                self.marco_seleccion, text=nombre, variable=variable
            ).pack(anchor="w", pady=2)

        acciones = ttk.Frame(self.tab_planificacion)
        acciones.pack(fill="x", pady=(0, 10))
        ttk.Button(
            acciones, text="Evaluar y registrar jornada",
            command=self._evaluar_jornada
        ).pack(side="left")
        ttk.Button(
            acciones, text="Limpiar selección",
            command=self._limpiar_seleccion
        ).pack(side="left", padx=8)

        self.marco_resultado = ttk.LabelFrame(
            self.tab_planificacion, text="Resultado de la evaluación", padding=10
        )
        self.marco_resultado.pack(fill="both", expand=True)
        self.texto_resultado = tk.Text(
            self.marco_resultado, height=13, wrap="word",
            state="disabled", font=("Arial", 10)
        )
        self.texto_resultado.pack(fill="both", expand=True)

    @staticmethod
    def _tarjeta_dato(parent, titulo, valor):
        tarjeta = ttk.LabelFrame(parent, text=titulo, padding=(10, 6))
        ttk.Label(tarjeta, text=valor, font=("Arial", 11, "bold")).pack(anchor="w")
        return tarjeta

    def _crear_tab_resultados(self):
        ttk.Label(
            self.tab_resultados, text="Historial de jornadas",
            style="Subtitulo.TLabel"
        ).pack(anchor="w", pady=(0, 5))
        ttk.Label(
            self.tab_resultados,
            text="Todas las jornadas evaluadas se conservan durante la ejecución, incluso si no cumplen las restricciones."
        ).pack(anchor="w", pady=(0, 10))

        columnas = ("id", "puntos", "peso", "costo", "capacidad", "aprovechamiento", "estado")
        self.tabla_historial = ttk.Treeview(
            self.tab_resultados, columns=columnas, show="headings",
            selectmode="extended", height=9
        )
        titulos = {
            "id": "Jornada", "puntos": "Puntos seleccionados", "peso": "Peso (kg)",
            "costo": "Costo total ($)", "capacidad": "Capacidad utilizada",
            "aprovechamiento": "Aprovechamiento", "estado": "Viabilidad"
        }
        anchos = {
            "id": 75, "puntos": 260, "peso": 90, "costo": 125,
            "capacidad": 135, "aprovechamiento": 135, "estado": 100
        }
        for col in columnas:
            self.tabla_historial.heading(col, text=titulos[col])
            self.tabla_historial.column(col, width=anchos[col], anchor="center")
        self.tabla_historial.tag_configure("viable", foreground="#176b35")
        self.tabla_historial.tag_configure("no_viable", foreground="#a32626")
        self.tabla_historial.pack(fill="both", expand=True)

        acciones = ttk.Frame(self.tab_resultados)
        acciones.pack(fill="x", pady=9)
        ttk.Button(
            acciones, text="Comparar jornadas seleccionadas",
            command=self._comparar_jornadas
        ).pack(side="left")
        ttk.Button(
            acciones, text="Actualizar historial",
            command=self._actualizar_historial
        ).pack(side="left", padx=8)

        self.marco_comparacion = ttk.LabelFrame(
            self.tab_resultados, text="Comparación de jornadas", padding=10
        )
        self.marco_comparacion.pack(fill="both", expand=True)
        self.tabla_comparacion = ttk.Treeview(
            self.marco_comparacion, show="tree headings", height=7
        )
        self.tabla_comparacion.heading("#0", text="Indicador")
        self.tabla_comparacion.column("#0", width=210, anchor="w")
        self.tabla_comparacion.pack(fill="both", expand=True)

    def _cargar_puntos(self):
        for fila in self.tabla_puntos.get_children():
            self.tabla_puntos.delete(fila)

        for nombre, datos in self.puntos.items():
            total = sum(datos.values())
            self.tabla_puntos.insert(
                "", "end",
                values=(
                    nombre, datos["papel_carton"], datos["plastico"],
                    datos["vidrio"], datos["organicos"],
                    datos["no_aprovechables"], total
                )
            )

    def _limpiar_seleccion(self):
        for variable in self.variables_puntos.values():
            variable.set(False)

    def _evaluar_jornada(self):
        seleccionados = [
            nombre for nombre, variable in self.variables_puntos.items()
            if variable.get()
        ]
        if not seleccionados:
            messagebox.showwarning(
                "Selección requerida", "Seleccione al menos un punto de generación."
            )
            return

        try:
            jornada = logica.evaluar_jornada(seleccionados, self.puntos)
            jornada = logica.registrar_jornada(jornada, self.historial)
            self._mostrar_texto(
                self.texto_resultado, self._formatear_jornada(jornada)
            )
            self._actualizar_historial()
        except NotImplementedError as error:
            messagebox.showinfo("Funcionalidad pendiente", str(error))
        except Exception as error:
            messagebox.showerror("Error", f"No fue posible evaluar la jornada:\n{error}")

    def _actualizar_historial(self):
        for fila in self.tabla_historial.get_children():
            self.tabla_historial.delete(fila)

        try:
            jornadas = logica.obtener_historial(self.historial)
            for jornada in jornadas:
                viable = jornada["viable"]
                self.tabla_historial.insert(
                    "", "end", iid=str(jornada["id"]),
                    tags=("viable" if viable else "no_viable",),
                    values=(
                        jornada["id"], ", ".join(jornada["puntos"]),
                        jornada["peso_total"], f'{jornada["costo_total"]:,.0f}',
                        f'{jornada["porcentaje_capacidad"]:.1f}%',
                        f'{jornada["porcentaje_aprovechamiento"]:.1f}%',
                        "Viable" if viable else "No viable"
                    )
                )
        except NotImplementedError as error:
            messagebox.showinfo("Funcionalidad pendiente", str(error))
        except Exception as error:
            messagebox.showerror("Error", f"No fue posible actualizar el historial:\n{error}")

    def _comparar_jornadas(self):
        seleccion = self.tabla_historial.selection()
        if len(seleccion) < 2:
            messagebox.showwarning(
                "Selección insuficiente",
                "Seleccione al menos dos jornadas. Puede usar Ctrl o Shift para seleccionar varias."
            )
            return

        ids = [int(item) for item in seleccion]
        try:
            jornadas = logica.obtener_historial(self.historial)
            seleccionadas = [j for j in jornadas if j["id"] in ids]
            resultado = logica.comparar_jornadas(seleccionadas)
            self._mostrar_comparacion(seleccionadas, resultado)
        except NotImplementedError as error:
            messagebox.showinfo("Funcionalidad pendiente", str(error))
        except Exception as error:
            messagebox.showerror("Error", f"No fue posible comparar las jornadas:\n{error}")

    def _mostrar_comparacion(self, jornadas, resultado):
        # La función de lógica retorna un diccionario:
        # {"indicadores": [nombres], "valores": {id_jornada: [valores]}}
        for item in self.tabla_comparacion.get_children():
            self.tabla_comparacion.delete(item)

        self.tabla_comparacion["columns"] = tuple(
            f"j{j['id']}" for j in jornadas
        )
        for jornada in jornadas:
            columna = f"j{jornada['id']}"
            self.tabla_comparacion.heading(columna, text=f"Jornada {jornada['id']}")
            self.tabla_comparacion.column(columna, width=140, anchor="center")

        indicadores = resultado["indicadores"]
        valores = resultado["valores"]
        for indice, indicador in enumerate(indicadores):
            fila = [
                valores[jornada["id"]][indice] for jornada in jornadas
            ]
            self.tabla_comparacion.insert(
                "", "end", text=indicador, values=fila
            )

    def _formatear_jornada(self, jornada):
        cantidades = jornada["cantidades_por_tipo"]
        nombres = {
            "papel_carton": "Papel y cartón",
            "plastico": "Plástico",
            "vidrio": "Vidrio",
            "organicos": "Orgánicos",
            "no_aprovechables": "No aprovechables"
        }
        lineas = [
            f'JORNADA {jornada["id"]}',
            f'Puntos seleccionados: {", ".join(jornada["puntos"])}',
            "",
            "CANTIDADES RECOLECTADAS"
        ]
        for clave, nombre in nombres.items():
            lineas.append(f"  - {nombre}: {cantidades[clave]} kg")
        lineas.extend([
            "",
            "COSTOS",
            f'  - Tratamiento: ${jornada["costo_tratamiento"]:,.0f}',
            f'  - Transporte: ${jornada["costo_transporte"]:,.0f}',
            f'  - Total: ${jornada["costo_total"]:,.0f}',
            "",
            "INDICADORES Y VIABILIDAD",
            f'  - Peso total: {jornada["peso_total"]} kg',
            f'  - Capacidad utilizada: {jornada["porcentaje_capacidad"]:.1f}%',
            f'  - Aprovechamiento potencial: {jornada["porcentaje_aprovechamiento"]:.1f}%',
            f'  - Estado: {"VIABLE" if jornada["viable"] else "NO VIABLE"}',
            f'  - Restricciones incumplidas: {", ".join(jornada["restricciones_incumplidas"]) or "Ninguna"}'
        ])
        return "\n".join(lineas)

    @staticmethod
    def _mostrar_texto(widget, contenido):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", contenido)
        widget.configure(state="disabled")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionResiduos(ventana)
    ventana.mainloop()
