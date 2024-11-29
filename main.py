from fastapi import FastAPI

app = FastAPI()
app.title ="Fastapi SENA" 
app.version= "2.0.0"

@app.get('/', tags=['home'])
def home ():
    return "hello fastapi"

@app.post('/', tags=['Musica'])
def Musica ():
    return "until i found you"

@app.put('/', tags=['Comida'])
def Comida ():
    return "arroz con pollo"

@app.delete('/', tags=['Deporte'])
def Deporte ():
    return "Futbol"



