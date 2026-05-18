from rich import print as rprint, pretty, inspect
from rich.console import Console
"""
from rich.panel import Panel
pretty.install()
["Rich and pretty", True]
rprint("[bold blue]Hello[/bold blue] [italic yellow]World![/italic yellow]", locals())
Panel.fit("[bold yellow] eae, mano ", border_style="red")
"""
console = Console()

console.print([1,2,3])

console.print("[blue underline]isso parece um link :p")
console.print(locals())
console.print("FOO", style="blue on white")