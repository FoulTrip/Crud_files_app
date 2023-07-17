import React, { useEffect, useState } from "react";
import axios from "axios";
import { toast } from "sonner";

function ListFiles() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/documents");
        console.log(response.data)
        setFiles(response.data);
      } catch (error) {
        console.error(error)
        toast(error)
      }
    };

    fetchFiles();

  }, []);

  return (
    <>
      <div>
        <h3>Archivos en la nube</h3>
        <ul>
            {files.map((file) => (
                <li key={file._id}>
                    <a href={`http://127.0.0.1:8000/download/${file._id}`}>
                        {file.filename}
                    </a>
                </li>
            ))}
        </ul>
      </div>
    </>
  );
}

export default ListFiles;
