import dbApp as db
import typer

app = typer.Typer()

def initialize():
    """INITIALIZE THE DATABASE CONNECTION"""
    db.get_database()

@app.command()
def insert(
    brand: str = typer.Option(..., prompt="Speaker brand"),
    model: str = typer.Option(..., prompt="Speaker model"),
    power: int = typer.Option(..., prompt="Speaker power", help="Enter an integer"),
    impedance: int = typer.Option(..., prompt="Speaker impedance", help="Enter an integer"),
):
    """Insert a new speaker."""
    db.insert_speaker(brand, model, power, impedance)

@app.command()
def delete(
    brand: str = typer.Option(..., prompt="Speaker brand"),
    model: str = typer.Option(..., prompt="Speaker model"),
):
    """Delete a speaker by brand and model."""
    db.drop_speaker_by_brand_model(brand, model)

@app.command()
def find_by_brand(brand: str = typer.Option(..., prompt="Speaker brand")):
    """Find speakers by brand."""
    speakers = db.find_speaker_by_brand(brand)
    if speakers:
        for speaker in speakers:
            typer.echo(speaker)
    else:
        typer.echo(f"No speakers found with brand '{brand}'")

if __name__ == '__main__':
    initialize()
    app()
    