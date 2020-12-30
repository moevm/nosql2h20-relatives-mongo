import React, { useState } from "react";
import '../App.css';
import axios from 'axios'

let data = "start"

axios.get("/api/fulltree")
.then(response => data = JSON.stringify(response.data) )

export default function Export() {
    return (
        <div>
          {data}
        </div>
    );
}
