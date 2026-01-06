import typer
import time
from todo.storage import load_tasks, save_tasks

app = typer.Typer(help="Task Manager CLI")

tasks = load_tasks()

@app.command()
def add(description: str):
    """Adicionar uma nova tarefa"""
    print(time.ctime())
    tasks.append({
        "id": len(tasks) + 1,
        "description": description,
        "status": False,
        "createdAt": time.ctime()
    })
    
    save_tasks(tasks)
    typer.echo("✅ Tarefa adicionada!")

@app.command()
def update(id: int, description: str):
    """update tarefa"""
    if id < 1 or id > len(tasks):
        typer.echo("❌ ID inválido")
        return

    tasks[id - 1]["description"] = description
    tasks[id - 1]["updatedAt"] = time.ctime()
    save_tasks(tasks)

    typer.echo(f"📝 Tarefa {id} editada")

@app.command()
def remove(id: int):
    """Remover tarefa"""
    if id < 1 or id > len(tasks):
        typer.echo("❌ ID inválido")
        return
        
    removed = tasks.pop(id - 1)
    save_tasks(tasks)

    typer.echo(f"🗑️ Tarefa removida: {removed['description']}")

@app.command()
def list():
    """Listar tarefas"""
    if not tasks:
        typer.echo("📭 Nenhuma tarefa encontrada")
        return
    
    for i, task in enumerate(tasks, start=1):
        if task["status"] == "progress":
            status = "📝"
        elif task["status"] == "done":
            status = "✔️"
        else:
            status = "❌"
        typer.echo(f"{i}. {status} {task['description']}")

@app.command()
def mark(id: int, status: str):
    """Marcar tarefa como concluída"""
    if id < 1 or id > len(tasks):
        typer.echo("❌ ID inválido")
        return
    
    if status == "progress":
        tasks[id -1]["status"] = "progress"
        typer.echo("📝 Tarefa em progresso")
    elif status == "done":
        tasks[id -1]["status"] = "done"
        typer.echo("🎉 Tarefa concluída!")
    save_tasks(tasks)

@app.command()
def list_done():
    """Listar tarefas"""
    if not tasks:
        typer.echo("📭 Nenhuma tarefa encontrada")
        return
    
    for i, task in enumerate(tasks, start=1):
        if task["status"] == "done":
            typer.echo(f"{i}. ✔️ {task['description']}")

@app.command()
def list_not_done():
    """Listar tarefas"""
    if not tasks:
        typer.echo("📭 Nenhuma tarefa encontrada")
        return
    
    for i, task in enumerate(tasks, start=1):
        if not task["status"]:
            typer.echo(f"{i}. ❌ {task['description']}")

@app.command()
def list_progress():
    """Listar tarefas"""
    if not tasks:
        typer.echo("📭 Nenhuma tarefa encontrada")
        return
    
    for i, task in enumerate(tasks, start=1):
        if task["status"] == "progress":
            typer.echo(f"{i}. 📝 {task['description']}")
