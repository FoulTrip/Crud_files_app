import { useState } from "react";
import { Toaster, toast } from "sonner";
import axios from "axios";
import ListFiles from "./components/ListFiles";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload/",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      response.status == 200
        ? toast.success("Archivo subido exitosamente")
        : toast.error("Error al subir el archivo");
    } catch (error) {
      toast.error("The database connection has failed");
    }
  };

  return (
    <>
      <Toaster richColors position="top-center" />
      <div>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload}>Subir Archivo</button>
      </div>
      <ListFiles />
    </>
  );
}

export default App;
