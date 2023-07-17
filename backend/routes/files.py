from fastapi import APIRouter, UploadFile, File, Response, HTTPException
from pymongo import MongoClient
from gridfs import GridFS
from bson.objectid import ObjectId

files = APIRouter()

# MongoDB Conection
client = MongoClient('mongodb://localhost:27017')
database = client['file_db']
fs = GridFS(database)
            

@files.post("/upload")
async def post_file(file: UploadFile = File(...)):
    try:
        # Guardo el archivo en la base de datos utilizando GridFS
        file_id = fs.put(file.file, filename = file.filename)
        return {"file_id": str(file_id)}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
@files.get("/documents")
def get_files():
    try:
        # Obténgo la lista de todos los archivos almacenados en la base de datos
        files = database.fs.files.find()
        file_list = [{"_id": str(file["_id"]), "filename": file["filename"]} for file in files]
        return file_list
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    
@files.get("/download/{file_id}")
async def download_file(file_id: str):
    try:
        # Obtengo el ObjectId del archivo a partir del parámetro en formato de cadena
        file_obj_id = ObjectId(file_id)
        
        # verifico si el archivo existe en la base de datos
        if fs.exists(file_obj_id):
            # Obtengo el archivo desde la base de datos
            file_obj = fs.get(file_obj_id)
            
            # Configuro los encabezados de la respuesta para la descarga
            response = Response(content = file_obj, media_type = "application/octet-stream")
            response.headers["Content-Disposition"] = f"attachment"; filename = {file_obj.filename}
            
            return response
        else:
            raise HTTPException(status_code=404, detail="File not found.")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    